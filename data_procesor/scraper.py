import sqlite3

from bs4 import BeautifulSoup
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.functionality_class import Functionality
from utilities.log_class import LogClass
from constans import emoji


class Scraper(Functionality):
    driver: WebDriver
    wait: WebDriverWait
    log: LogClass
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, driver, wait, log):
        self.driver = driver
        self.wait = wait
        self.log = log
        super().__init__(driver, wait, log)

    def scraping_data(self):
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        scraped_data = ((soup.find('div', class_='timetable-container'))
                        .find('table', class_='table-bordered').find_all('tr'))
        data = []
        try:
            for row in scraped_data[1:]:
                hour_cell = row.find('th')
                hour = hour_cell.text
                minute = row.find('td')
                minute_array = []
                for all_minutes in minute:
                    if all_minutes.text != '':
                        minute_array.append(all_minutes.text)
                data.append((hour, minute_array))
            self.log.info(f"{emoji.INFO}Successfully scraped data from web ")
        except Exception as e:
            self.log.error(f"Failed to scrap data from web {emoji.TASK_FAILED}. Error:{e}")
        return data
