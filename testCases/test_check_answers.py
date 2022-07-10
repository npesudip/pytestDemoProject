from pageObjects.CheckAnswers import CheckAnswers
from pageObjects.RiddleOfStone import RiddleOfStoneSection
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_RiddleOfStone:
    baseURL = "https://techstepacademy.com/trial-of-the-stones"

    # logger = LogGen.loggen()  # Logger

    def test_check_answers(self, setup):
        # self.logger.info("************* Test_001_RiddleOfStone **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.CheckAnswer = CheckAnswers(self.driver)

        self.CheckAnswer.setRiddleOfStone()
        self.CheckAnswer.click_riddleOfStone()
        secret_key = self.CheckAnswer.copySecretKey()
        self.CheckAnswer.click_secretkey_input_box()
        self.CheckAnswer.set_secret_key(password=secret_key)
        self.CheckAnswer.click_secretKey_button()
        success_message = self.CheckAnswer.read_success_message()

        m1 = self.CheckAnswer.copy_merchant_1()
        m1_wealth = self.CheckAnswer.copy_mer1_wealth()
        m2 = self.CheckAnswer.copy_merchant_2()
        m2_wealth = self.CheckAnswer.copy_mer2_wealth()

        if m1_wealth > m2_wealth:
            self.CheckAnswer.submit_richest_name(rich_name=m1)
        else:
            self.CheckAnswer.submit_richest_name(rich_name=m2)
        self.CheckAnswer.click_answer_button_2()
        success_message2 = self.CheckAnswer.assert_two_merchant()

        self.CheckAnswer.click_check_answers()
        success_message = self.CheckAnswer.trail_complete_message()

        if success_message == "Trial Complete":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
