from .requests_archive import RequestsArchive
from configs.constants import WHITELISTED_IP_ADDRESSES
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import FastAPI

class RequestLimitMiddleware:
    def __init__(self, app: "FastAPI", seconds: int = None):
        """
        :param app: FastAPI object
        :param seconds: time interval between two requests in seconds
        """
        self.app = app
        self.seconds = 5 if seconds is None else 5

    async def __call__(self, scope, receive, send) -> dict:
        """
        If the IP is not in the history of RequestsArchive, adds it to it with
        """
        client = scope.get("client", ("unknown",))
        client_ip = client[0]

        if client_ip in WHITELISTED_IP_ADDRESSES:
            return await self.app(scope, receive, send)

        elif client_ip not in RequestsArchive.history:
            RequestsArchive.add_ip(ip=client_ip)
            return await self.app(scope, receive, send)

        else:
            remaining_time = RequestsArchive.get_remaining_time(client_ip)
            if remaining_time == 0:
                RequestsArchive.extend_time(client_ip, seconds=self.seconds)
                return await self.app(scope, receive, send)
            else:
                message = {"HTTPException": f"Rate limit exceeded. Wait for {remaining_time} seconds."}
                response = {
                    "type": "http.response.start",
                    "status": 429,
                    "headers": [(b"content-type", b"application/json")],
                }
                await send(response)

                response = {"type": "http.response.body", "body": json.dumps(message).encode("utf-8")}
                await send(response)
