from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from page.product_page import ProductPage


class CategoryPage:
    """
    Amazon selects products from the category page

    """
    PAGE_CONTROL = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    GO_TO_TWO_PAGE = (By.CLASS_NAME, "a-normal")
    THIRD_PRODUCT = (By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".s-main-slot.s-result-list.s-search-results")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.PRODUCT_LIST), 'No "Products" on the page!')
        (self.methods.wait_element_visible(self.GO_TO_TWO_PAGE), 'No "Next" on the page!')

    def select_product(self, search):
        """"
        The second page goes through and selects the third product
        """
        self.methods.wait_element_clickable(self.GO_TO_TWO_PAGE).click()
        page_control = self.methods.wait_element_visible(CategoryPage.PAGE_CONTROL).text
        assert (page_control == search)
        self.methods.wait_all_element(self.THIRD_PRODUCT)[2].click()
        return ProductPage(self.driver)