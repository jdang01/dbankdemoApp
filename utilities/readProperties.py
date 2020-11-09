import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url= config.get('environment variables', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username= config.get('environment variables', 'username')
        return username

    @staticmethod
    def getPassword():
        validpass= config.get('environment variables', 'password')
        return validpass
