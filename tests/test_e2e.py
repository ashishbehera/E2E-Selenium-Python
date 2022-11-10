from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        # driver.find_element(By.LINK_TEXT,  "Shop").click()
        # driver.find_element(By.XPATH,  "//a[contains(@href,'shop')]").click()

        checkout_page = home_page.shopItems()
        log.info("Getting all the card titles")
        checkout_page.addProducts("iphone X")
        checkout_page.getBtnAddToCheckout().click()
        confirm_page = checkout_page.getBtnCheckout()
        log.info("Entering Country Name")
        confirm_page.getSelectCountry().send_keys("ind")
        self.verifyLinkPresent("India")
        confirm_page.getLinkTextCountry().click()
        # driver.find_element(By.LINK_TEXT, "term & Conditions").click()
        # driver.find_element(By.CSS_SELECTOR, ".nsm-dialog-btn-close").click()
        # driver.find_element(By.ID, "checkbox2").click()
        confirm_page.getBtnPurchase().click()
        # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        msgSucess = confirm_page.getMsgSuccess().text.strip()
        log.info("Text messagw from application: "+msgSucess)
        assert "Success! Thank you!" in msgSucess


