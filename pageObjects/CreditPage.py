import time

class ApplyForCredit:
    link_DigitalCreditMenu_xpath = "/html/body/aside/nav/div[2]/ul/li[5]/a"
    link_NewAppMenuItem_xpath = "/html/body/aside/nav/div[2]/ul/li[5]/ul/li/a"
    lstitem_EmploymentSts_id = "employmentStatus"
    lstitem_UnEmploymentSts_xpath ="/html/body/div[1]/div[2]/div/form/div[4]/div/div/div[2]/div[1]/div/select/option[6]"
    textbox_TotalAnnualIncome_id = "annualIncome"
    textbox_MonthlyMortgage_id = "monthlyMortgage"
    textbox_MonthlyLoan_id = "monthlyAutoLoan"
    textbox_MonthlyOtherLoan_id = "monthlyOtherLoan"
    textbox_MinimumCreditCard_id = "minimumCreditCard"
    lstitem_BankStatus_id = "bankStatus"
    lstitem_NeitherSts_xpath = "/html/body/div[1]/div[2]/div/form/div[4]/div/div/div[2]/div[5]/div/select/option[5]"
    checkbox_AgreeTerms_id = "agreeTerms"
    button_Apply_xpath = "/html/body/div[1]/div[2]/div/form/div[5]/div/div/div[2]/button"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCreditMenu(self):
        self.driver.find_element_by_xpath(self.link_DigitalCreditMenu_xpath).click()

    def clickOnNewAppMenu(self):
        self.driver.find_element_by_xpath(self.link_NewAppMenuItem_xpath).click()

    def setEmploymentStatus(self, status):
        self.driver.find_element_by_id(self.lstitem_EmploymentSts_id).click()
        time.sleep(2)
        if status == 'Unemployed':
            self.listitem = self.driver.find_element_by_id(self.lstitem_UnEmploymentSts_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setAnnualIncome(self, income):
        self.driver.find_element_by_id(self.textbox_TotalAnnualIncome_id).send_keys(income)

    def setMonthlyMortgage(self, mortgage):
        self.driver.find_element_by_id(self.textbox_MonthlyMortgage_id).send_keys(mortgage)

    def setMonthlyLoan(self, loan):
        self.driver.find_element_by_id(self.textbox_MonthlyLoan_id).send_keys(loan)

    def setMonthlyOtherLoan(self, otherloan):
        self.driver.find_element_by_id(self.textbox_MonthlyOtherLoan_id).send_keys(otherloan)

    def setMinimumCreditCard(self, creditcard):
        self.driver.find_element_by_id(self.textbox_MinimumCreditCard_id).send_keys(creditcard)

    def setBankStatus(self, bankstatus):
        self.driver.find_element_by_id(self.lstitem_BankStatus_id).click()
        time.sleep(2)
        if bankstatus == 'Neither':
            self.driver.find_element_by_xpath(self.lstitem_NeitherSts_xpath).click()

    def clickCheckbox(self):
        self.driver.find_element_by_id(self.checkbox_AgreeTerms_id).click()

    def clickApply(self):
        self.driver.find_element_by_xpath(self.button_Apply_xpath).click()