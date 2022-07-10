from pageObjects.RiddleOfStone import RiddleOfStoneSection
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_RiddleOfStone:
    baseURL = "https://techstepacademy.com/trial-of-the-stones"
    # logger = LogGen.loggen()  # Logger

    def test_riddleOfStone(self, setup):
        # self.logger.info("************* Test_001_RiddleOfStone **********")
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
            assert True
        else:
            assert False
