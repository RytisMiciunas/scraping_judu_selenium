from selenium.webdriver.common.by import By

DECLINE_COOCKIES = (By.XPATH, "/html/body/div[3]/div[2]/button[2]")
PUBLIC_TRANSPORT_FOR_TRAVELERS_DROPBOX = \
    (By.XPATH, "(//a[contains(@class,'nav-link w-sub')])[1]")
BUS_SCHEDULE_OPTION = \
    (By.XPATH, "//a[contains(text(),'Maršrutų tvarkaraščiai')]")
SCHEDULE_IFRAME = (By.XPATH, "//iframe[@title='Schedules']")
EXPRESS_BUS_OPTION = (By.XPATH, "//span[@class='transport-toggle toggle-expressbus']")
FOUR_G_BUS_BUTTON = (By.XPATH, "//a[@href='#expressbus/4g/a-b/map']")
EUROPE_SQUARE_STOP = (By.XPATH, "//a[@data-index='11']")
BICYCLE_CHECKBOX = (By.XPATH, "(//div[@class='bicycle-container'])[2]")
CHOOSE_SUNDAY_CHECKBOX = (By.XPATH, "//input[@data-workdays='7']")
CHOOSE_SATURDAY_CHECKBOX = (By.XPATH, "//input[@data-workdays='6']")
CHOOSE_WORKDAY_CHECKBOX = (By.XPATH, "//input[@data-workdays='12345']")
TIME_TABLE = (By.XPATH, "//div[@id='schedule-new']")
