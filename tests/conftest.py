import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from testData.TestData import TestData
from utilities import PropertyFile
from utilities.BrowserInitialization import BrowserInitialization


@pytest.fixture()
def setup(request, browser):
    global driver
    driver = BrowserInitialization.generateDriver(browser, TestData.BASE_URL)
    request.cls.driver = driver
    yield
    # # Do teardown (this code will be executed after each test):

    # Close browser window:
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # print('*****', outcome, '*****')
    # print('*****', rep.nodeid, '*****')
    # print('*****', rep.location, '*****')
    # print('*****', item, '*****')
    # print('*****', call, '*****')

    # if rep.outcome == 'failed':
    #     allure.attach(driver.get_screenshot_as_png(), name=rep.nodeid, attachment_type=AttachmentType.PNG)
    # setattr(item, "rep_" + rep.when, rep)
    # return rep
