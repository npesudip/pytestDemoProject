from selenium.webdriver.common.by import By
import time


class TheTwoMerchants:
    # Merchant Wealth
    merchant1_xp_l1 = "(//b[normalize-space()='Jessica'])[1]"
    merchant1_wealth_xp_l2 = "(//p[normalize-space()='3000'])[1]"
    merchant2_xp_l3 = "(//b[normalize-space()='Bernard'])[1]"
    merchant2_wealth_xp_l4 = "(//p[normalize-space()='2000'])[1]"
    richest_input_box_id_l5 = "r3Input"
    button_for_richest_id_l6 = "r3Butn"

    second_success_message_css_l7 = "div[id='successBanner2'] h4"

    def __init__(self, driver):
        self.driver = driver

    def copy_merchant_1(self):
        merchant1 = self.driver.find_element(By.XPATH, self.merchant1_xp_l1).text
        # merchant1 = self.driver.find_element(By.XPATH, self.merchant1_xp_l1).get_attribute('innerHTML')
        return merchant1

    def copy_mer1_wealth(self):
        m1_wealth = self.driver.find_element(By.XPATH, self.merchant1_wealth_xp_l2).text
        # m1_wealth = self.driver.find_element(By.XPATH, self.merchant1_wealth_xp_l2).get_attribute('innerHTML')
        return m1_wealth

    def copy_merchant_2(self):
        merchant2 = self.driver.find_element(By.XPATH, self.merchant2_xp_l3).text
        # merchant2 = self.driver.find_element(By.XPATH, self.merchant2_xp_l3).get_attribute('innerHTML')
        return merchant2

    def copy_mer2_wealth(self):
        m2_wealth = self.driver.find_element(By.XPATH, self.merchant2_wealth_xp_l4).text
        # m2_wealth = self.driver.find_element(By.XPATH, self.merchant2_wealth_xp_l4).get_attribute('innerHTML')
        return m2_wealth

    def submit_richest_name(self, rich_name):
        self.driver.find_element(By.ID, self.richest_input_box_id_l5).click()
        self.driver.find_element(By.ID, self.richest_input_box_id_l5).send_keys(rich_name)

    def click_answer_button_2(self):
        self.driver.find_element(By.ID, self.button_for_richest_id_l6).click()

    def assert_two_merchant(self):
        assert_message_2 = self.driver.find_element(By.CSS_SELECTOR, self.second_success_message_css_l7).text
        return assert_message_2


