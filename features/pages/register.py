from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    register_option_css = "a[href='https://tutorialsninja.com/demo/index.php?route=account/register']"
    input_first_name_css_selector = "#input-firstname"
    input_last_name_css_selector = "#input-lastname"
    input_telephone = "#input-telephone"
    input_confirm_password = "#input-confirm"
    check_box_css_selector = "input[value='1'][name='agree']"
    continue_button_css_selector = "input[value='Continue']"
    account_create_msg = "div[id='content'] h1"
    warning_msg_css_selector = ".fa.fa-exclamation-circle"

    def click_on_register_option(self):
        self.driver.find_element(By.CSS_SELECTOR, self.register_option_css).click()

    def enter_first_name(self, firstname):
        self.driver.find_element(By.CSS_SELECTOR, self.input_first_name_css_selector).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.CSS_SELECTOR, self.input_last_name_css_selector).send_keys(lastname)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.CSS_SELECTOR, self.input_telephone).send_keys(telephone)

    def enter_confirm_password(self, confirmpassword):
        self.driver.find_element(By.CSS_SELECTOR, self.input_confirm_password).send_keys(confirmpassword)

    def click_on_check_box(self):
        self.driver.find_element(By.CSS_SELECTOR, self.check_box_css_selector).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_button_css_selector).click()

    def account_created_successfully_msg(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.account_create_msg).text
        print(msg)

    def warning_msg(self):
        warnMsg = self.driver.find_element(By.CSS_SELECTOR, self.warning_msg_css_selector).text
        print(warnMsg)
