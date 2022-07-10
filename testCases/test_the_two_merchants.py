import time

from pageObjects.TheTwoMerchants import TheTwoMerchants


class Test_002_RiddleOfStone:
    baseURL = "https://techstepacademy.com/trial-of-the-stones"

    def test_002_merchant_wealth(self, setup):
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
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "Two Merchants.png")
            self.driver.close()
            assert False
