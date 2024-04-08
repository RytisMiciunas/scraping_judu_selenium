import time
import datetime
import psutil
import holidays.countries

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from constans import element_tuple, emoji
from utilities.functionality_class import Functionality
from utilities.log_class import LogClass


class SchedulePage(Functionality):
    driver: WebDriver
    wait: WebDriverWait
    action: ActionChains
    log: LogClass

    def __init__(self, driver, wait, log, action):
        self.driver = driver
        self.wait = wait
        self.log = log
        self.action = action
        super().__init__(driver, wait, log)

    def select_4g(self):
        for proc in psutil.process_iter():
            if "firefox" in proc.name():
                time.sleep(5)       # ask for PowerPoint presentation if questions appear why sleep
                break

        self.wait_for_frame_and_switch(element_tuple.SCHEDULE_IFRAME)
        self.wait_for_element_clickable(element_tuple.EXPRESS_BUS_OPTION)
        self.click_on_element(element_tuple.EXPRESS_BUS_OPTION)

        self.wait_for_element_clickable(element_tuple.FOUR_G_BUS_BUTTON)
        self.click_on_element(element_tuple.FOUR_G_BUS_BUTTON)

    # this function checks is it just a regular day, saturday or sunday/holiday
    def check_what_day(self):
        lt_holidays = holidays.country_holidays('LT')
        today = datetime.datetime.now().date()
        self.log.debug(f"checking what day is today {emoji.INFO}")
        if today.strftime("%Y-%m-%d") in lt_holidays or today.strftime("%a") == "Sun":
            return element_tuple.CHOOSE_SUNDAY_CHECKBOX
        if today.strftime("%a") == "Sat":       # was elif and else but pylint didn't like that
            return element_tuple.CHOOSE_SATURDAY_CHECKBOX
        return element_tuple.CHOOSE_WORKDAY_CHECKBOX

    def select_europe_square_stop(self):
        try:
            self.click_on_element(element_tuple.EUROPE_SQUARE_STOP)
        except Exception as e:
            self.log.error(f"failed to select Europe square bus stop"
                           f" {emoji.TASK_FAILED}. Error:{e}")

    def select_todays_schedule(self):
        self.find_element(element_tuple.CHOOSE_WORKDAY_CHECKBOX).is_displayed()
        self.wait_for_element_clickable(element_tuple.BICYCLE_CHECKBOX)
        self.click_on_element(self.check_what_day())
