from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Spx:
    CATEGORY_PAGE = (By.CLASS_NAME, "navigation__desktop-item")
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card")
    PRODUCT_SIZE = (By.CLASS_NAME, "mb-3.js-variant")
    ADD_TO_CART = (By.CLASS_NAME, "js-add-to-cart")
    GO_TO_CART = (By.CLASS_NAME, "js-go-basket")
    MAIN_PAGE = (By.CLASS_NAME, "header__icon")
    WEBSITE = "https://www.spx.com.tr/"
    SEPETEKLE = (By.CLASS_NAME, "basket-wrapper__title")
    SIZE = (By.CSS_SELECTOR, "a[data-selected='True']")
    driver_path = " "

    def __init__(self):
        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.maximize_window()
        self.browser.get(self.WEBSITE)
        self.wait = WebDriverWait(self.browser, 15)

    def test_navigate(self):
        assert "SPX - Sport Point Extreme" in self.browser.title
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].click()
        assert "https://www.spx.com.tr/erkek/" in self.browser.current_url, True
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[4].click()
        assert "Rossıgnol Stade Erkek Kayak Montu - Kayak Montu" in self.browser.title, True
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_SIZE))[3].click()

        assert self.wait.until(ec.element_to_be_clickable(self.SIZE))

        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()

        assert self.wait.until(ec.element_to_be_clickable(self.SEPETEKLE)).text == "Ürün Sepete Eklendi"

        self.wait.until(ec.element_to_be_clickable(self.GO_TO_CART)).click()
        assert "https://www.spx.com.tr/baskets/basket/" in self.browser.current_url, True
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        assert "SPX - Sport Point Extreme" in self.browser.title


Spx().test_navigate()

from selenium import webdriver
import requests

driver = webdriver.Chrome("chromedriver.exe yolu")

driver.get("resim(ler)in olduğu web adresi")

resimler = driver.find_elements_by_xpath("imgler için yazıdğınız xpath")

for i in resimler:
    url = i.get_attribute("src")
    imgdata = requests.get(url)

    with open("kaydedilecek resim yolu", "wb") as img:
        img.write(imgdata.raw)  # imgdata.raw yada imgdata.content olacaktı bu ikisinden biri

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_fullpage_screenshot(self):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("yoururlxxx")
    time.sleep(2)

    #the element with longest height on page
    ele=driver.find_element("xpath", '//div[@class="react-grid-layout layout"]')
    total_height = ele.size["height"]+1000

    driver.set_window_size(1920, total_height)      #the trick
    time.sleep(2)
    driver.save_screenshot("screenshot1.png")
    driver.quit()

if __name__ == "__main__":
    test_fullpage_screenshot()