import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ReadConfig.getScreenshotPath()
    file = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("************************* Test_002_DDT_Login *************************")
        self.logger.info("************************* Verifying Login DDT Test *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.row = XLUtils.getRowCount(self.file, "Sheet1")
        lst_status = []
        for r in range(2, self.row + 1):
            self.username = XLUtils.readData(self.file, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.file, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.file, "Sheet1", r, 3)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            time.sleep(3)
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("Login DDT Test Passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login DDT Test Failed")
                self.driver.close()
                assert False
        self.logger.info("****** End of Login DDT Test ***********")
        self.logger.info("******** completed TC_LoginDDT_002")
