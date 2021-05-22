from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from page.login_page import LoginPage
from page.category_page import CategoryPage


class HomePage:
    LOGIN_ICON = (By.ID, "nav-link-accountList")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    search_icon = (By.CLASS_NAME, "nav-search-submit")
    HOME_LOGO = (By.ID, "nav-logo-sprites")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.driver.get('https://www.amazon.com')
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.HOME_LOGO), 'No "Navigate Logo" button on the page!')
        (self.methods.wait_element_visible(self.SEARCH_BAR), 'No "Search bar"  on the page!')

    def sign_in_button_click(self):
        """
        Navigates to the loginpage
        """
        self.methods.wait_element_clickable(self.LOGIN_ICON).click()
        return LoginPage(self.driver)

    def search_query(self, search):
        """
        Navigates to the category search

        """
        self.methods.wait_element_clickable(self.SEARCH_BAR).send_keys(search)
        self.methods.wait_element_clickable(self.search_icon).click()
        return CategoryPage(self.driver)
