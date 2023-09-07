from selenium import webdriver
import daadbot.constants as const
import os


class Daad(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Daad, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

