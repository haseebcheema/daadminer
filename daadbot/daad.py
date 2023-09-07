from selenium import webdriver
from selenium.webdriver.common.by import By
import daadbot.constants as const
import os


class Daad(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDriver", teardown=True):
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

    def accept_cookies(self):
        cookies_btn = self.find_element(By.CLASS_NAME, 'snoop-button')
        cookies_btn.click()

