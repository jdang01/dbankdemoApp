class CreateSavingsAccount:
    link_SavingsMenu_id = "savings-menu"
    link_SavingsMenuItem_id = "new-savings-menu-option"
    rd_SavingsType_id = "Savings"
    rd_MoneyType_id = "Money Market"
    rd_IndOwnership_id = "Individual"
    rd_JointOwnership_id = "Joint"
    textbox_AccountName_xpath = "/html/body/div[1]/div[2]/div/div/div/div/form/div[1]/div[4]/div/input"
    textbox_InitialDeposit_xpath = "/html/body/div[1]/div[2]/div/div/div/div/form/div[1]/div[5]/div/input"
    button_Submit_id = "newSavingsSubmit"

    def __init__(self,driver):
        self.driver=driver

    def clickOnSavingsMenu(self):
        self.driver.find_element_by_id(self.link_SavingsMenu_id).click()

    def clickOnSavingsMenuItem(self):
        self.driver.find_element_by_id(self.link_SavingsMenuItem_id).click()

    def selectAccountType(self, account):
        if account == 'Savings':
            self.driver.find_element_by_id(self.rd_SavingsType_id).click()
        elif account == 'Money Market':
            self.driver.find_element_by_id(self.rd_MoneyType_id).click()
        else:
            self.driver.find_element_by_id( self.rd_SavingsType_id).click()

    def selectOwnershipId(self, owner):
        if owner == 'Individual':
            self.driver.find_element_by_id(self.rd_IndOwnership_id).click()
        elif owner == 'Joint':
            self.driver.find_element_by_id(self.rd_JointOwnership_id).click()
        else:
            self.driver.find_element_by_id(self.rd_IndOwnership_id).click()

    def setAccountName(self, accountname):
        self.driver.find_element_by_xpath(self.textbox_AccountName_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_AccountName_xpath).send_keys(accountname)

    def setDepositAmt(self, deposit):
        self.driver.find_element_by_xpath(self.textbox_InitialDeposit_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_InitialDeposit_xpath).send_keys(deposit)

    def clickSubmit(self):
        self.driver.find_element_by_id(self.button_Submit_id).click()
