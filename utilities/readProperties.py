import configparser

config = configparser.RawConfigParser()

config.read(".\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getExcelFileName():
        fileName = config.get('common info', 'excelFilePath')
        return fileName

    @staticmethod
    def getExcelSheet():
        sheetName = config.get('common info', 'salestd')
        return sheetName

    @staticmethod
    def getModuleName():
        moduleName = config.get('common info', 'moduleName')
        return moduleName
