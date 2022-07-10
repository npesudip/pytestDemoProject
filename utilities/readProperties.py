import configparser

config = configparser.RawConfigParser()
config.read(r"..\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        # url = config.get('common info', 'baseURL')
        test_url = "https://techstepacademy.com/trial-of-the-stones"
        return test_url


config_obj = ReadConfig
url = config_obj.getApplicationURL()
print(url)
