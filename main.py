from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.middleware import RequestLimitMiddleware
from api.views import home_router, api_info_router, sample_data_router, giveaways_all_router, giveaway_queried_router


app = FastAPI()

# Connecting views
app.include_router(home_router)
app.include_router(sample_data_router)
app.include_router(api_info_router)

app.include_router(giveaways_all_router)
app.include_router(giveaway_queried_router)

# Enabling CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["GET"],
                   allow_headers=["*"], max_age=360)

# Enabling request limiting
app.add_middleware(RequestLimitMiddleware)


# Adding Swagger UI
@app.get("/docs", tags=["docs"])
async def get_openapi():
    return app.openapi()


# Adding ReDoc
@app.get("/redoc", tags=["redoc"])
async def redoc():
    return {"redoc": "This is ReDoc."}


if __name__ == '__main__':
    def pre_check():
        from database.cache import Cache

        if Cache.is_valid():
            return True

        else:
            from business_logic import Giveaways
            from logs import ErrorLogger, InfoLogger

            from selenium.common.exceptions import NoSuchDriverException
            from selenium.common.exceptions import SessionNotCreatedException
            from configs.errors import InvalidDriverPathException, NotMatchingDriverVersion
            from configs.errors.error_resolvers.selenium_webdriver_issue import WebdriverErrorResolver
            from logs import ErrorLogger

            try:
                # triggering the scrapper
                giveaways_data = Giveaways.get_current_giveaways()
                print(giveaways_data)

                Cache.write_data(giveaways_data['response'])
                InfoLogger.save_log(message=f"Current giveaways: {giveaways_data}")


            except NoSuchDriverException as error:
                ErrorLogger.save_error_log()
                if 'Unable to locate or obtain driver for chrome' in str(error):
                    WebdriverErrorResolver.user_option(error=InvalidDriverPathException)

            except SessionNotCreatedException as error:
                ErrorLogger.save_error_log()
                if "This version of ChromeDriver only supports Chrome version" in str(error):
                    WebdriverErrorResolver.user_option(error=NotMatchingDriverVersion)
            except Exception:
                ErrorLogger.save_error_log()
            return True

    if pre_check():
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
        # uvicorn main:app --port 8000 --host 127.0.0.1
