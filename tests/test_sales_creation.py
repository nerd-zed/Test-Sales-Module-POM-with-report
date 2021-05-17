import time

import pytest
from pageObjects.LoginPage import LoginPage
from testData.TestData import TestData
from utilities import ExcelUtil, PropertyFile, ScreenShot
from utilities.BaseClass import BaseClass


class TestSalesModule(BaseClass):

    @pytest.mark.order(1)
    def test_sales_module(self, getData):
        driver = self.driver
        logger = self.getLogger()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_valid_login(TestData.USERNAME, TestData.PASSWORD)
        logger.info('Logged In Successfully')

        homepage.click_allapps()
        salesmodulepage = homepage.select_sales()
        salesorderpage = salesmodulepage.navigate_to_sales_order()

        salesorderpage.click_create_btn()
        salesorderpage.select_customer(getData['customername'])
        salesorderpage.select_validity(getData['validity'])
        salesorderpage.add_product(getData['product1'])
        salesorderpage.add_product(getData['product2'])
        salesorderpage.add_product(getData['product3'])
        # salesorderpage.select_quotation(getData['quotation'])
        salesorderpage.select_payment_terms(getData['paymentterms'])
        salesorderpage.click_confirm()
        salesorderpage.click_create_invoice()
        salesorderpage.select_down_payment(getData['downpayment'])
        salesorderpage.click_create_nd_view()
        salesorderpage.click_validate()
        salesorderpage.click_register()
        salesorderpage.click_validate_register()
        # salesorderpage.click_send_print()
        # salesorderpage.click_email_checkbox()
        # salesorderpage.click_print()
        # salesorderpage.click_ok_btn()
        time.sleep(5)
        logger.info('Record Created Successfully')

        salesorderpage.open_sales_list()
        salesorderpage.click_on_created_order()
        salesorderpage.click_cancel()
        salesorderpage.click_actions_and_delete()
        logger.info('Record Deleted Successfully')

        TestData.write_valid_result()
        homepage.do_logout()
        logger.info('Logged Out Successfully')



    @pytest.fixture(params=TestData.getSalesTestData())
    def getData(self, request):
        return request.param
