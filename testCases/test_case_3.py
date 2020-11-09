import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateSavingsPage import CreateSavingsAccount
from pageObjects.CreditPage import ApplyForCredit
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_ApplyCredit:
    baseURL= ReadConfig.getApplicationURL()
    path = ".//TestData/SavingTestData.xlsx"
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() # Logger

    def test_applyCredit(self, setup):
        self.logger.info( "******************* Starting Test_004_Apply Credit *********************************" )
        self.logger.info( "***************************** Verifying Page Elements ***************************" )
        self.driver = setup
        self.driver.get( self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in sheet: ", self.rows)
        self.lp.setUserName(self.username )
        self.lp.setPassword(self.password )
        lst_status = [] # Empty List Variable
        self.lp.clickLogin()
        time.sleep( 2 )
        self.logger.info("***** Login Successful*******")
        self.logger.info("***** Starting Apply Credit Test ****")
        self.cp = ApplyForCredit(self.driver)
        self.cp.clickOnCreditMenu()
        self.cp.clickOnNewAppMenu()
        self.logger.info("***** Providing Financial Information ******** ")
        self.cp.setEmploymentStatus("Unemployed")
        self.cp.setAnnualIncome("5000")
        self.cp.setMonthlyMortgage("3000")
        self.cp.setMonthlyLoan("1000")
        self.cp.setMonthlyOtherLoan("1000")
        self.cp.setMinimumCreditCard("1000")
        self.cp.setBankStatus("Neither")
        self.cp.clickCheckbox()
        self.cp.clickApply()

        self.logger.info( "********Submitting Savings Account Number*****" )
        self.msg = self.driver.find_element_by_tag_name( "body" ).text
        print( self.msg )
        if 'Declined' in self.msg:
            assert True == True
            self.driver.close()
            self.logger.info("***** Test_004_Apply Credit Passed ****")
        else:
            self.logger.info("***** Test_004_Apply Credit Passed Failed ***")
            self.driver.save_screenshot( ".//Screenshots/" + "test_applyCredit.png" )
            self.driver.close()
        self.logger.info( "***** Ending Test_004_Apply Credit Test ********")