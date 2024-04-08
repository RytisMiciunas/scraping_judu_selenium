import logging
import sys

from constans import emoji
from utilities import default_log_level


class LogClass:
    logger: logging.Logger

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # erase 'w' if dont want reset log file everytime
        file_handler = logging.FileHandler('log_file.log',
                                           encoding='UTF-8')
        formatter = (logging.Formatter
                     ("%(asctime)s: %(levelname)s: %(message)s"))
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.setLevel(self.setup_log_file_level())

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def setup_log_file_level(self):
        debug_level = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'ERROR': logging.ERROR,
                       'CRITICAL': logging.CRITICAL}
        if len(sys.argv) > 1:
            argv_string = str.upper(sys.argv[1])
            self.info(f"{emoji.INFO} selected log level: {argv_string} ")
            print(f"{emoji.INFO} selected log level: {argv_string} ")
        else:
            argv_string = str.upper(default_log_level.DEFAULT)
            self.info(f"{emoji.INFO} selected default log level: {argv_string} ")
            print(f"{emoji.INFO} selected default log level: {argv_string} ")
        try:
            return debug_level[argv_string]
        except Exception as e:
            self.critical(f"failed to set logging level to "
                          f"{sys.argv[1]} due to {e} {emoji.TASK_FAILED}, "
                          f"instead set to default: {argv_string}")
            print(f"failed to set logging level to "
                  f"{sys.argv[1]} due to {e} {emoji.TASK_FAILED}, "
                  f"instead set to "
                  f"default: {argv_string}")
            return debug_level[str.upper(default_log_level.DEFAULT)]

    def close(self):
        handlers = self.logger.handlers[:]
        try:
            for handler in handlers:
                self.logger.removeHandler(handler)
                handler.close()
        except Exception as e:
            self.error(f"failed to close log_file : "
                       f"{e} {emoji.TASK_FAILED}")
