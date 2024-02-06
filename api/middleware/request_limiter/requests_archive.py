import time
from configs.metaclasses import Singleton


class RequestsArchive(metaclass=Singleton):
    history = {}

    @classmethod
    def add_ip(cls, ip: str, seconds: int = None):
        """Adds the given ip to history with N seconds cooldown, by default it's 5. """
        seconds = 5 if seconds is None else seconds
        expiration_time = time.time() + seconds
        cls.history[ip] = {"waiting_time": seconds, "expiration_time": expiration_time}
        return cls

    @classmethod
    def extend_time(cls, ip: str, seconds: int = None):
        """Extends the cooldown of the given ip for N seconds, by default it's 5. """
        seconds = 5 if seconds is None else seconds

        if ip in cls.history:
            cls.history[ip]["expiration_time"] += seconds
        return cls

    @classmethod
    def get_remaining_time(cls, ip: str) -> int:
        """Returns the remaining cooldown for the ip in seconds"""
        if ip in cls.history:
            remaining_time = cls.history[ip]["expiration_time"] - time.time()
            return max(0, round(remaining_time))
        else:
            return 0
