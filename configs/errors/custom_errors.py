from configs.constants import WebDriverConstants

message = (f"Webdriver should be present by: {WebDriverConstants.CHROMEDRIVER_PATH} location"
           f"\nRead the howtofix file: {WebDriverConstants.DRIVER_FIX_FILE}."
           f"\nYou can run")


class InvalidDriverPathException(Exception):
    """Exception raised for an invalid path to the Selenium webdriver."""

    def __str__(self):
        return f"\n\nInvalid path to webdriver.\n{message}"


class NotMatchingDriverVersion(Exception):
    def __str__(self):
        return (f"\nThe version of webdriver doesn't match with the version of the installed browser.\n"
                f"{message}")
