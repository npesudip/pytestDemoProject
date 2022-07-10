from selenium.webdriver.common.by import By


class RiddleOfStoneSection:
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
