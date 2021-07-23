class loginLocators():
    Login_via_email_label_xpath = "//label[text()='Login with Phone/Email']"
    Login_xpath = "//p[contains(text(),'Login or Create Account')]"
    username_id = "username"
    continue_button_xpath = "//button[@data-cy='continueBtn']"
    password_id = "password"
    login_button_xpath = "//span[contains(text(),'Login')]"
    loggedInUser_xpath = "//p[@data-cy='loggedInUser']"
    My_Profile_xpath = "//p[text()='My Profile']"
    logout_xpath = "//li[text()='Logout']"

    login_or_create_login_xpath = "//p[text()='Login or Create Account']"
    invalid_credential_login_message_xpath = "//span[text()='Either Username or Password is incorrect.']"