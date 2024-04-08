import os

from selenium.common import WebDriverException
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from constans import emoji
from utilities.log_class import LogClass


class Setup:    # pylint: disable=too-few-public-methods
    driver: WebDriver
    wait: WebDriverWait
    log: LogClass
    path: str
    action: ActionChains

    def __init__(self, which_driver):
        self.log = LogClass()
        self.path = os.getcwd()
        self.driver = self.__get_driver(which_driver)
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.action = ActionChains(self.driver)

    def __get_driver(self, which_driver):
        match which_driver:
            case 0:
                try:
                    driver = webdriver.Chrome()
                    self.log.info(f"connected to chrome successfully {emoji.TASK_SUCCSEEDED}")
                    return driver
                except FileNotFoundError:
                    self.log.info(f"Chrome driver not found at: {self.path}. "
                                  f"Trying to connect to other drivers{emoji.TASK_FAILED}")
                except WebDriverException as e:
                    self.log.critical(f"Error initializing Chrome driver{emoji.TASK_FAILED}."
                                      f" Error: {e}")
                except Exception as e:
                    self.log.critical(f"An unexpected error occurred with chrome: "
                                      f"{e} {emoji.TASK_FAILED}")

            case 1:
                try:
                    driver = webdriver.Firefox()
                    self.log.info(f"connected to Firefox successfully {emoji.TASK_SUCCSEEDED}")
                    return driver
                except FileNotFoundError:
                    self.log.info(f"Mozilla driver not found at: {self.path}. "
                                  f"Trying to connect to other driver {emoji.TASK_FAILED}")
                except WebDriverException as e:
                    self.log.critical(f"Error initializing Mozilla driver {emoji.TASK_FAILED}."
                                      f" Error: {e} ")
                except Exception as e:
                    self.log.critical(f"An unexpected error occurred with Mozilla: "
                                      f"{e} {emoji.TASK_FAILED}")

            case 2:
                try:
                    driver = webdriver.Edge()
                    self.log.info(f"connected to Edge successfully {emoji.TASK_SUCCSEEDED}")
                    return driver
                except FileNotFoundError as e:
                    self.log.critical(
                        f"Couldn't connect to any driver. Edge driver not found at: "
                        f"{self.path}. Error: {e} {emoji.TASK_FAILED}")
                except WebDriverException as e:
                    self.log.critical(f"Error initializing Edge driver {emoji.TASK_FAILED}. "
                                      f"Error: {e}")
                except Exception as e:
                    self.log.critical(f"An unexpected error occurred with Edge: "
                                      f"{e} {emoji.TASK_FAILED}")
            case _:
                self.log.critical(f"Didn't select proper driver {emoji.TASK_FAILED}")
                return None
