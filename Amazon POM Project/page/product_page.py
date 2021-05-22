from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from page.wishlist_page import WishlistPage


class ProductPage:
    """Product page to add list"""

    ADD_TO_LIST = (By.ID, "add-to-wishlist-button-group")
    VIEW_YOUR_LIST = (By.ID, "WLHUC_viewlist")
    TITLE = (By.ID, "titleSection")
    PRODUCT_CONTROL = (By.XPATH, "//h3[@class='a-size-base']")
    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.ADD_TO_LIST), 'No "Add to list" button on the page!')
        (self.methods.wait_element_visible(self.ADD_TO_CART), 'No "Add to cart" button on the page!')

    def product_addlist(self):
        """
        Adds product to the add list
        """
        title = self.methods.wait_element_clickable(self.TITLE).text
        self.methods.wait_element_clickable(ProductPage.ADD_TO_LIST).click()
        self.methods.wait_element_clickable(ProductPage.VIEW_YOUR_LIST).click()
        name = self.methods.wait_all_element(self.PRODUCT_CONTROL)[0].text
        assert title == name
        return WishlistPage(self.driver)