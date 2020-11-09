class LoginPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_signin_id = "submit"
    image_profile_xpath = "/html/body/div[1]/header/div/div[2]/div[1]/a/img"
    link_logout_linktext = "Logout"
    error_login_xpath = "/html/body/div[1]/div/div/div[2]/div/text()"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_signin_id).click()

    def clickProfileImage(self):
        self.driver.find_element_by_xpath(self.image_profile_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

    def getErrorMsg(self):
        error_text = self.driver.find_element_by_xpath(self.error_login_xpath).text
        return error_text
