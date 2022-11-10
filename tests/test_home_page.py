from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest as pytest


class TestHomePage(BaseClass):

    def test_home_page(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.enterName().send_keys(getData["firstname"])
        log.info("First Name is: "+getData["firstname"])
        home_page.enterEmail().send_keys(getData["email"])
        home_page.clickChkBox().click()
        self.selectByVisibleText(home_page.select_Gender(), getData["gender"])
        home_page.btn_Submit().click()
        msg_sucess = home_page.msg_Success().text
        assert "Success!423423" in msg_sucess
        self.driver.refresh()

    # @pytest.fixture(params=[("Test User1", "test.user1@gmail.com", "Male"), ("Test User2", "test.user2@gmail.com", "Female")])
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param
