from abc import ABC
import logging
import sys
import traceback
from configs.constants import INFO_LOG_FILE_PATH, ERROR_LOG_FILE_PATH


class LoggerFactory:
    @staticmethod
    def create_logger(logger_name: str, level: int | logging.Logger, log_file_path: str) -> logging.Logger:
        custom_logger = logging.getLogger(name=logger_name)
        custom_logger.setLevel(level=level)

        custom_logger_file_handler = logging.FileHandler(filename=log_file_path, mode='a')
        custom_logger_file_handler.setLevel(level=level)

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        custom_logger_file_handler.setFormatter(fmt=formatter)
        custom_logger.addHandler(custom_logger_file_handler)
        return custom_logger


class LoggerDelivery:
    @staticmethod
    def get_logger(logger_name: str, level: int | logging.Logger, log_file_path: str) -> logging.Logger:
        return LoggerFactory.create_logger(logger_name, level, log_file_path)


# -----------------
class MyLogger(ABC):
    __slots__ = ('name', 'level', 'log_file')

    def get_logger(self) -> logging.Logger:
        return LoggerDelivery.get_logger(logger_name=self.name, level=self.level, log_file_path=self.log_file)


class InfoLoggerInterface(MyLogger):
    def __init__(self):
        self.name = "info_logger"
        self.level = logging.INFO
        self.log_file = INFO_LOG_FILE_PATH


class ErrorLoggerInterface(MyLogger):
    def __init__(self):
        self.name = "error_logger"
        self.level = logging.ERROR
        self.log_file = ERROR_LOG_FILE_PATH


# -----------------
class InfoLogger:
    logger: logging.Logger = InfoLoggerInterface().get_logger()

    @staticmethod
    def save_log(message: str):
        InfoLogger.logger.info(message)
        return None


class ErrorLogger:
    logger: logging.Logger = ErrorLoggerInterface().get_logger()

    @staticmethod
    def save_error_log():
        exception_type, exception_value, exception_traceback = sys.exc_info()

        traceback_str = ''.join(traceback.format_exception(exception_type, exception_value, exception_traceback))
        ErrorLogger.logger.error(traceback_str)
        return None
