import time

from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    input_email_Css_Selector = "#input-email"
    input_password_Css_Selector = "#input-password"
    login_button_css_selector = "input[value='Login']"
    msg_css_selector = "body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)"
    warning_msg_css_selector = ".alert.alert-danger.alert-dismissible"

    def enter_email(self, validemail):
        self.driver.find_element(By.CSS_SELECTOR, self.input_email_Css_Selector).send_keys(validemail)

    def enter_password(self, validpassword):
        self.driver.find_element(By.CSS_SELECTOR, self.input_password_Css_Selector).send_keys(validpassword)

    def click_on_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()
        time.sleep(2)

    def login_msg(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.msg_css_selector).text
        print(msg)

    def warning_msg(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.warning_msg_css_selector).text
        print(msg)
