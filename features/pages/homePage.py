from selenium.webdriver.common.by import By

from features.pages.login import Login


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    product_name_search_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    valid_product_xpath = "//a[normalize-space()='HP LP3065']"
    error_msg_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"
    my_account_xpath = "//span[normalize-space()='My Account']"
    login_xpath = "//a[normalize-space()='Login']"

    def search_product_by_name(self, product):
        self.driver.find_element(By.XPATH, self.product_name_search_xpath).send_keys(product)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def valid_product_displayed(self):
        assert self.driver.find_element(By.XPATH, self.valid_product_xpath).is_displayed()

    def proper_error_msg_displayed(self):
        msg = self.driver.find_element(By.XPATH, self.error_msg_xpath).text
        assert msg == "There is no product that matches the search criteria."

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()
        return Login(self.driver)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()
        return Login(self.driver)


