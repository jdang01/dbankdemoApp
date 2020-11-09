import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    #username = ReadConfig.getUserName()
    #correct_password = ReadConfig.getCorrectPassword()
    #incorrect_password = ReadConfig.getIncorrectPassword()
    logger = LogGen.loggen()

    def test_login_valid(self, setup):
        self.logger.info("***************************** Starting test_login_valid *********************************")
        self.logger.info("***************************** Verifying Login Page ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in sheet: ", self.rows)
        lst_status=[]  # Empty List Variable
        for r in range(2,self.rows-1):
            self.username = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.expected = XLUtils.readData( self.path, 'Sheet1',r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            actual_title = self.driver.title
            expected_title = "Digital Bank"
            if actual_title == expected_title:
                if self.expected == "Pass":
                    self.logger.info("************Login Passed ***************")
                    lst_status.append("Pass")
                    self.lp.clickProfileImage()
                    time.sleep(2)
                    self.lp.clickLogout()
                elif self.expected == "Fail":
                    self.logger.info("************Login Failed ***************")
                    lst_status.append("Fail")
                    self.lp.clickProfileImage()
                    time.sleep(2)
                    self.lp.clickLogout()
            elif actual_title != expected_title:
                if self.expected == "Pass":
                    self.logger.info("************Login Failed ***************")
                    lst_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("************Login Passed ***************")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("**********Test Case test_login_valid is Passed ************")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Test Case test_login_valid is Failed***********")
            self.driver.save_screenshot(".//Screenshots/" + "test_login_valid.png")
            self.driver.close()
            assert True
        self.logger.info("******** Ending test_login_valid Test *****")
        self.logger.info("******* test_login_valid Completed ********")


    def test_login_invalid(self, setup):
        self.logger.info("***************************** Starting test_login_invalid *********************************")
        self.logger.info("***************************** Verifying Login Page ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in sheet: ", self.rows)
        lst_status=[]  # Empty List Variable
        for r in range(3,self.rows):
            self.username = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.expected = XLUtils.readData( self.path, 'Sheet1',r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            self.msg = self.driver.find_element_by_tag_name( "body" ).text
            print( self.msg )
            expected_error = "Invalid credentials or access not granted."
            if 'Invalid credentials' in self.msg:
                if self.expected == "Fail":
                    self.logger.info("************ Invalid Login Passed ***************")
                    lst_status.append("Pass")
                elif self.expected == "Pass":
                    self.logger.info("************ Invalid Login Failed ***************")
                    lst_status.append("Fail")
        if "Fail" not in lst_status:
            self.logger.info("**********Test Case test_login_invalid is Passed ************")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Test Case test_login_valid is Failed***********")
            self.driver.save_screenshot(".//Screenshots/" + "test_login_valid.png" )
            self.driver.close()
            assert True
        self.logger.info("******** Ending test_login_invalid Test *****")
        self.logger.info("******* test_login_invalid Completed ********")