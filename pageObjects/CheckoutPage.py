from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productList = (By.XPATH, "//div[@class='card h-100']")
    btnAddToCheckout = (By.CSS_SELECTOR, ".btn-primary")
    btnCheckout = (By.CSS_SELECTOR, ".btn-success")
    cardTitle = (By.CLASS_NAME, "card-title")
    btnInfo = (By.CSS_SELECTOR, ".btn-info")

    def getProductList(self):
        return self.driver.find_elements(*CheckoutPage.productList)

    def getBtnAddToCheckout(self):
        return self.driver.find_element(*CheckoutPage.btnAddToCheckout)

    def getBtnCheckout(self):
          self.driver.find_element(*CheckoutPage.btnCheckout).click()
          confirm_page = ConfirmPage(self.driver)
          return confirm_page

    def addProducts(self, productName):
        for product in self.getProductList():
            if product.find_element(*CheckoutPage.cardTitle).text == productName:
                product.find_element(*CheckoutPage.btnInfo).click()
                break