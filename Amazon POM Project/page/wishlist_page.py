from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class WishlistPage:

    DELETE_ITEM = (By.NAME, "submit.deleteItem")
    DELETED = (By.XPATH, ".//*[contains(text(),'Deleted')]")
    MOVE = (By.ID, "move-to-list-button-I350Z21ZJX30G0")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.DELETE_ITEM), 'No "Delete" button on the page!')
        (self.methods.wait_element_visible(self.MOVE), 'No "Your list"  on the page!')

    def delete_product(self):
        """
        Delete product to the wish list
        """
        self.methods.wait_element_clickable(WishlistPage.DELETE_ITEM).click()
        assert self.methods.selector_exists(WishlistPage.DELETED)