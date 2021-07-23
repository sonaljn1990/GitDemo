from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
from MakeMyTripProject.Locators.loginLocators import loginLocators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        # self.driver.get("https://www.makemytrip.com/")
        self.Login_via_email_label_xpath = loginLocators.Login_via_email_label_xpath
        self.username_id = loginLocators.username_id
        self.continue_button_xpath = loginLocators.continue_button_xpath
        self.password_id = loginLocators.password_id
        self.login_button_xpath = loginLocators.login_button_xpath
        self.loggedInUser_xpath = loginLocators.loggedInUser_xpath
        self.My_Profile_xpath = loginLocators.My_Profile_xpath
        self.logout_xpath = loginLocators.logout_xpath
        self.login_or_create_login_xpath = loginLocators.login_or_create_login_xpath
        self.invalid_credential_login_message_xpath = loginLocators.invalid_credential_login_message_xpath


    def click_to_login_via_email(self):
        self.driver.find_element_by_xpath(self.Login_via_email_label_xpath).click()

    def enter_username(self, email):
        self.driver.find_element_by_id(self.username_id).send_keys(email)

    def click_on_continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def check_user_loggedIn(self):
        if self.driver.find_element_by_xpath(self.loggedInUser_xpath).is_displayed():
            return True
        else:
            return False
    def click_logged_in_user(self):
        self.driver.find_element_by_xpath(self.loggedInUser_xpath).click()

    def click_on_my_profile(self):
        self.driver.find_element_by_xpath(self.My_Profile_xpath).click()

    def click_on_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()

    def click_on_Login_or_create_account(self):
        self.driver.find_element_by_xpath(self.login_or_create_login_xpath).click()

    def check_invalid_credential_login_msg(self):
        self.driver.find_element_by_xpath(self.invalid_credential_login_message_xpath).is_displayed()
        return True