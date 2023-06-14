from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    path = ReadConfig.getScreenshotPath()

    logger = LogGen.loggen()

    def test_homepage_title(self, setup):
        self.logger.info("************************* Test_001_Login *************************")
        self.logger.info("************************* Verifying Home Page Title *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************************* Home page title test is passed *************************")
        else:
            self.driver.save_screenshot(self.path + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************************* Home page title test is failed *************************")
            assert False

    def test_login(self, setup):
        self.logger.info("************************* Verifying Login Test *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clic_login()
        act_title = self.driver.title
        # self.lp.click_logout()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************************* Login test is passed *************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.path + "test_login.png")
            self.driver.save_screenshot()
            self.logger.info("************************* Login test is failed *************************")
            self.driver.close()
            assert False
