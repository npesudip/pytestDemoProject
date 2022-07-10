import sys
import os

from pageObjects.CheckAnswers import CheckAnswers
from pageObjects.RiddleOfStone import RiddleOfStoneSection
from pageObjects.TheTwoMerchants import TheTwoMerchants
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

os.chdir(os.path.dirname(sys.argv[0]))


class Test_NinjaTrails:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    def test_001_riddleOfStone(self, setup):
        self.logger.info("************* Test_001_RiddleOfStone **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.ros = RiddleOfStoneSection(self.driver)
        self.ros.setRiddleOfStone()
        self.ros.click_riddleOfStone()
        secret_key = self.ros.copySecretKey()
        self.ros.click_secretkey_input_box()
        self.ros.set_secret_key(password=secret_key)
        self.ros.click_secretKey_button()
        success_message = self.ros.read_success_message()

        if success_message == "Success!":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "Two Merchants.png")
            self.driver.close()
            assert False

    def test_002_merchant_wealth(self, setup):
        self.logger.info("************* test_002_merchant_wealth **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.mw = TheTwoMerchants(self.driver)
        m1 = self.mw.copy_merchant_1()
        m1_wealth = self.mw.copy_mer1_wealth()
        m2 = self.mw.copy_merchant_2()
        m2_wealth = self.mw.copy_mer2_wealth()

        if m1_wealth > m2_wealth:
            self.mw.submit_richest_name(rich_name=m1)
        else:
            self.mw.submit_richest_name(rich_name=m2)
        self.mw.click_answer_button_2()

        success_message2 = self.mw.assert_two_merchant()

        if success_message2 == "Success!":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "Two Merchants.png")
            self.driver.close()
            assert False

    def test_003_check_answers(self, setup):
        self.logger.info("************* test_003_check_answers **********")
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
            self.driver.save_screenshot("..\\Screenshots\\" + "Two Merchants.png")
            self.driver.close()
            assert False
