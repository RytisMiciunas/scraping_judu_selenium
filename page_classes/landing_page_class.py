from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from constans import element_tuple
from utilities.functionality_class import Functionality
from utilities.log_class import LogClass


class LandingPage(Functionality):
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

    def go_to_vvt_schedule(self):
        self.driver.maximize_window()
        self.find_and_click_on_element(element_tuple.DECLINE_COOCKIES)
        dropbox = self.find_element(element_tuple.PUBLIC_TRANSPORT_FOR_TRAVELERS_DROPBOX)
        selecting = self.find_element(element_tuple.BUS_SCHEDULE_OPTION)
        self.action.move_to_element(dropbox).move_to_element(selecting).click().perform()
