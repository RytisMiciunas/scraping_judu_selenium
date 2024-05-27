from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constans import emoji
from utilities.log_class import LogClass


class Functionality:
    driver: WebDriver
    wait: WebDriverWait
    log: LogClass

    def __init__(self, driver, wait, log):
        self.driver = driver
        self.wait = wait
        self.log = log

    def find_element(self, element):
        return self.driver.find_element(*element)

    def find_and_click_on_element(self, element):
        try:
            found_element = self.find_element(element)
            found_element.click()
        except Exception as e:
            self.log.error(f"Faild to find element, "
                           f"trying to scroll to it and try again {emoji.TASK_FAILED}"
                           f"error: {e}")
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", found_element)
                found_element.click()
            except Exception as e:
                self.log.critical(f"failed to click on element {emoji.TASK_FAILED}. Error: {e}")

    def wait_for_element_clickable(self, element):
        self.wait.until(EC.element_to_be_clickable(element))

    def wait_for_frame_and_switch(self, element):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(element))

    def wait_for_element_visible(self, element):
        self.wait.until(EC.visibility_of_element_located(element))

    def wait_for_element_to_be_located(self, element):
        self.wait.until(EC.presence_of_all_elements_located(element))
