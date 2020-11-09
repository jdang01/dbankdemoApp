import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateSavingsPage import CreateSavingsAccount
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_CreateSavings:
    baseURL= ReadConfig.getApplicationURL()
    path = ".//TestData/SavingTestData.xlsx"
    #username = ReadConfig.getUserName()
    #correct_password = ReadConfig.getCorrectPassword()
    logger = LogGen.loggen() # Logger

    def test_createSavingsAcct(self, setup):
        self.logger.info("******************* Starting Test_003_Create Savings *********************************")
        self.logger.info("***************************** Verifying Page Elements ***************************" )
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage( self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in sheet: ", self.rows)
        #self.lp.setUserName(self.username )
        #self.lp.setPassword(self.password )
        lst_status = [] # Empty List Variable
        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.account = XLUtils.readData(self.path,'Sheet1',r,3)
            self.owner = XLUtils.readData(self.path, 'Sheet1', r,4)
            self.accountname = XLUtils.readData( self.path,'Sheet1',r,5)
            self.deposit = XLUtils.readData(self.path,'Sheet1',r,6)
            self.expected = XLUtils.readData(self.path,'Sheet1',r,7)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            self.logger.info("***** Login Successful*******")
            self.logger.info("***** Starting Create Savings Account Test ******** ")
            self.sp = CreateSavingsAccount(self.driver)
            self.sp.clickOnSavingsMenu()
            self.sp.clickOnSavingsMenuItem()
            self.logger.info("***** Providing Account Details ******** " )
            self.sp.selectAccountType(self.account)
            self.sp.selectOwnershipId(self.owner)
            #self.name = self.random_generator() + "test"
            self.sp.setAccountName(self.accountname)
            self.sp.setDepositAmt(self.deposit)
            self.sp.clickSubmit()

            self.logger.info("********Submitting Savings Account Number*****")
            self.msg = self.driver.find_element_by_tag_name("body").text
            print(self.msg)
            if 'Account: Savings' in self.msg:
                assert True == True
                lst_status.append("Pass")
                self.logger.info("***** Test Passed ****")
            else:
                self.logger.info( "********** Test Failed ***********" )
                assert True == False
                lst_status.append("Fail")
        if "Fail" not in lst_status:
            self.logger.info( "**********Test createSavingsAcct Passed  ************" )
            self.driver.close()
            assert True
        else:
            self.logger.info( "********** Test createSavingsAcct Passed  ***********" )
            self.driver.save_screenshot( ".//Screenshots/" + "test_createSavingsAcct.png" )
            self.driver.close()
            assert True
            self.driver.close
            self.logger.info("***** Ending Test_003_Create Savings Test ******** ")

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))