import os
from datetime import datetime

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    current_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    if browser_name == 'chrome':
        service_obj = Service(parent_dir + "//drivers//chromedriver");
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == 'firefox':
        service_obj = Service(parent_dir + "//drivers//geckodriver");
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == 'edge':
        service_obj = Service(parent_dir + "//drivers//msedgedriver");
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    current_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    config.option.htmlpath = (
            parent_dir + "/reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # # current directory
    # current_dir = os.getcwd()
    # print("Present Directory", current_dir)
    # # parent directory
    # print(os.path.abspath(os.path.join(current_dir, os.pardir)))

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        current_dir = os.getcwd()
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = parent_dir + "/reports/" + report.nodeid.replace("::", "_")  + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
