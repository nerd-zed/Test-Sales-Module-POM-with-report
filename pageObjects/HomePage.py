from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.SalesModulePage import SalesModulePage
from utilities import ScreenShot


class HomePage(BasePage):
    USERMENU = (By.XPATH, "(//li[@class='o_user_menu']//a)[1]")
    LOGOUTBTN = (By.XPATH, "//a[@data-menu='logout']")
    ALLAPPS = (By.XPATH, "(//a[@data-toggle='dropdown'])[1]")
    HEADING = (By.XPATH, "(//a[@role='button'])[1]")
    SELECT_SALES = (By.XPATH, "//a[text()[normalize-space()='Sales']]")

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.click(self.USERMENU)
        self.click(self.LOGOUTBTN)

    def click_allapps(self):
        self.click(self.ALLAPPS)

    def select_sales(self):
        self.click(self.SELECT_SALES)

        assert True == self.check_text_presence(self.HEADING, 'Sales')
        ScreenShot.takeScreenshot(self.driver, 'opened_sales_app')
        return SalesModulePage(self.driver)
