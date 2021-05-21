import time

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SalesModulePage import SalesModulePage
from testData.TestData import TestData
from utilities import ExcelUtil, ScreenShot
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen


class TestSalesModule(BaseClass):
    logger = LogGen.logGen()
    testStatus = []

    @pytest.mark.order(1)
    def test_sales_module(self, getData):
        driver = self.driver
        driver.get(TestData.BASE_URL)
        driver.maximize_window()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_valid_login(TestData.USERNAME, TestData.PASSWORD)
        self.logger.info('Logged In Successfully')

        homepage.click_allapps()
        salesmodulepage = homepage.select_module()
        # homepage.select_module()
        salesorderpage = salesmodulepage.navigate_to_sales_order()

        salesorderpage.click_create_btn()
        statusList = salesorderpage.select_customer(getData['customername'])
        if statusList[0] is not True & statusList[1] is not False:
            self.logger.info('Customer Not found')
        else:
            salesorderpage.select_validity(getData['validity'])
            salesorderpage.add_product(getData['product1'])

            salesorderpage.select_payment_terms(getData['paymentterms'])
            salesorderpage.click_confirm()
            # time.sleep(10)

        if salesorderpage.isTitleNew() is False:
            if getData['expected'] == 'Pass':
                self.logger.info('Record Created Successfully')
                salesorderpage.open_sales_list()
                salesorderpage.click_on_created_order()
                salesorderpage.click_cancel()
                salesorderpage.click_actions_and_delete()
                self.logger.info('Record Deleted Successfully')
                TestData.write_result('Pass', 'Pass')
                self.testStatus.append('True')
            elif getData['expected'] == 'Fail':
                # This condition executes at application error
                self.logger.info('Application error')
                TestData.write_result('Pass', 'Fail')
                self.testStatus.append('False')
        elif salesorderpage.isTitleNew() is True:
            if getData['expected'] == 'Pass':
                # This condition executes at application error
                self.logger.info('Application error')
                TestData.write_result('Fail', 'Fail')
                self.testStatus.append('False')
            elif getData['expected'] == 'Fail':
                self.logger.info('Record creation failed successfully')
                TestData.write_result('Fail', 'Pass')
                self.testStatus.append('True')

        assert 'True' == self.testStatus[-1]
        self.logger.info('Test Run successfully')

        homepage.do_logout()
        self.logger.info('Logged Out Successfully')

    @pytest.fixture(params=TestData.getSalesTestData())
    def getData(self, request):
        return request.param
