from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    chkBox = (By.ID, "exampleCheck1")
    selectGender = (By.ID, "exampleFormControlSelect1")
    btnSubmit = (By.XPATH, "//input[@value='Submit']")
    msgSucess = (By.CSS_SELECTOR, ".alert-success")


    def shopItems(self):
         self.driver.find_element(*HomePage.shop).click()
         checkout_page = CheckoutPage(self.driver)
         return checkout_page

    def enterName(self):
        return self.driver.find_element(*HomePage.name)

    def enterEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickChkBox(self):
        return self.driver.find_element(*HomePage.chkBox)

    def select_Gender(self):
        return self.driver.find_element(*HomePage.selectGender)

    def btn_Submit(self):
        return self.driver.find_element(*HomePage.btnSubmit)

    def msg_Success(self):
        return self.driver.find_element(*HomePage.msgSucess)
