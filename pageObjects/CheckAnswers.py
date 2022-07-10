from selenium.webdriver.common.by import By


class CheckAnswers:
    riddle_stone_id_l1 = "r1Input"
    riddle_answer_btn_id_l2 = "r1Btn"
    secret_key_css_l3 = "div[id='passwordBanner'] h4"
    enter_secret_key_id_l4 = "r2Input"
    button_for_secret_key_l5 = "r2Butn"
    first_success_message_css_l6 = "div[id='successBanner1'] h4"

    def __init__(self, driver):
        self.driver = driver

    def setRiddleOfStone(self):
        self.driver.find_element(By.ID, self.riddle_stone_id_l1).click()
        self.driver.find_element(By.ID, self.riddle_stone_id_l1).send_keys("rock")

    def click_riddleOfStone(self):
        self.driver.find_element(By.ID, self.riddle_answer_btn_id_l2).click()

    def copySecretKey(self):
        secret_key = self.driver.find_element(By.CSS_SELECTOR, self.secret_key_css_l3).text
        return secret_key

    def click_secretkey_input_box(self):
        self.driver.find_element(By.ID, self.enter_secret_key_id_l4).click()

    def set_secret_key(self, password):
        self.driver.find_element(By.ID, self.enter_secret_key_id_l4).send_keys(password)

    def click_secretKey_button(self):
        self.driver.find_element(By.ID, self.button_for_secret_key_l5).click()

    def read_success_message(self):
        first_success_message = self.driver.find_element(By.CSS_SELECTOR, self.first_success_message_css_l6).text
        return first_success_message

    # Merchant Wealth
    merchant1_xp_l1 = "(//b[normalize-space()='Jessica'])[1]"
    merchant1_wealth_xp_l2 = "(//p[normalize-space()='3000'])[1]"
    merchant2_xp_l3 = "(//b[normalize-space()='Bernard'])[1]"
    merchant2_wealth_xp_l4 = "(//p[normalize-space()='2000'])[1]"
    richest_input_box_id_l5 = "r3Input"
    button_for_richest_id_l6 = "r3Butn"

    second_success_message_css_l7 = "div[id='successBanner2'] h4"

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

    check_answers_btn_id = "checkButn"
    assert_Trail_complete_xp = "(//h4[normalize-space()='Trial Complete'])[1]"

    def click_check_answers(self):
        self.driver.find_element(By.ID, self.check_answers_btn_id).click()

    def trail_complete_message(self):
        assert_message_3 = self.driver.find_element(By.XPATH, self.assert_Trail_complete_xp).text
        return assert_message_3
