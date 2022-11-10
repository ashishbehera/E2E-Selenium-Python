from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self,  driver):
        self.driver = driver

    selectCountry = (By.ID, "country")
    linkTextCountry = (By.LINK_TEXT, "India")
    btnPurchase = (By.CSS_SELECTOR, ".btn-success")
    msgSuccess = (By.CSS_SELECTOR, ".alert-success")

    def getSelectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getLinkTextCountry(self):
        return self.driver.find_element(*ConfirmPage.linkTextCountry)

    def getBtnPurchase(self):
        return self.driver.find_element(*ConfirmPage.btnPurchase)

    def getMsgSuccess(self):
        return self.driver.find_element(*ConfirmPage.msgSuccess)

