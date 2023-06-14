from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser............")
    return driver


################ PyTest HTML Reports ##############
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerece'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Thrinath_k'
#
#
# # It is hook for delete/modify/ Environment info to HTML Report....
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
