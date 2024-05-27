from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from data_procesor.database_manipulating_class import DatabaseManipulating
from data_procesor.output_class import Output
from data_procesor.scraper import Scraper
from page_classes.landing_page_class import LandingPage
from page_classes.schedule_page_class import SchedulePage
from utilities.log_class import LogClass
from utilities.setup_class import Setup
from constans import url, element_tuple


class Base(Setup):  # pylint: disable=too-few-public-methods
    driver: WebDriver
    wait: WebDriverWait
    log: LogClass
    action: ActionChains

    landing_page: LandingPage
    schedule_page: SchedulePage
    scraper: Scraper
    database_manipulating: DatabaseManipulating
    output: Output

    def __init__(self, which_driver):
        super().__init__(which_driver)
        self.driver.get(url.JUDU_URL)
        self.driver.maximize_window()
        self.driver.find_element(*element_tuple.DECLINE_COOCKIES).click()

        self.landing_page = LandingPage(self.driver, self.wait, self.log, self.action)
        self.schedule_page = SchedulePage(self.driver, self.wait, self.log, self.action)
        self.scraper = Scraper(self.driver, self.wait, self.log)
        self.database_manipulating = DatabaseManipulating(self.log)
        self.output = Output(self.log)

    def close(self):
        self.log.close()
        self.driver.quit()
