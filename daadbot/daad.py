import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import daadbot.constants as const
import os
from daadbot.parse_daad_data import DaadData
import pandas as pd


class Daad(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDriver", teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Daad, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()
        self.scraped_data = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def accept_cookies(self):
        cookies_btn = self.find_element(By.CLASS_NAME, 'snoop-button')
        cookies_btn.click()

    def change_language(self):
        eng_language = self.find_element(By.CLASS_NAME, 'qa-language-item')
        eng_language.click()

    def go_to_international_programs(self):
        ul_list = self.find_element(By.CSS_SELECTOR, 'ul[aria-live="polite"]')
        link_to_programs = ul_list.find_elements(By.TAG_NAME, 'li')
        link_to_programs[2].click()

    def choose_programme(self, programme):

        # enter programme in the input box
        input_field = self.find_element(By.CSS_SELECTOR, 'input[name="q"]')
        input_field.clear()
        input_field.send_keys(programme)

        # select course
        course_type = self.find_element(By.CSS_SELECTOR, 'button[title="Please select"]')
        course_type.click()
        select_course = self.find_element(By.CLASS_NAME, 'multiselect-container')
        masters_course = select_course.find_elements(By.CSS_SELECTOR, 'li input')
        masters_course[1].click()

        # select language
        course_language = self.find_elements(By.CSS_SELECTOR, 'button[title="Please select"]')
        course_language[1].click()
        select_language = self.find_elements(By.CLASS_NAME, 'multiselect-container')
        time.sleep(5)
        eng_language = select_language[1].find_elements(By.CSS_SELECTOR, 'li input')
        eng_language[1].click()

        # select course field
        course_field = self.find_element(By.CSS_SELECTOR, 'select[name="fos"]')
        course_field.click()
        select_field = course_field.find_element(By.CSS_SELECTOR, 'option[value="6"]')
        select_field.click()

        # submit the form
        submit = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit.click()

    def apply_filters(self):

        # select subject
        select_subject = self.find_elements(By.CLASS_NAME, 'c-multiselect')
        select_subject[1].click()
        select_cs = select_subject[1].find_element(By.CSS_SELECTOR, 'input[value="49"]')
        select_cs.click()

        # select no fees
        select_fees = self.find_element(By.ID, 'filterFee')
        select_fees.click()
        no_fee_option = select_fees.find_element(By.CSS_SELECTOR, 'option[value="1"]')
        no_fee_option.click()

    def filter_amount_on_page(self):
        num_filter = self.find_element(By.ID, 'filterAmountOnPage')
        num_filter.click()
        num_of_items = num_filter.find_element(By.CSS_SELECTOR, 'option[value = "100"]')
        num_of_items.click()

    def total_pages(self):
        num_pages = self.find_element(By.CLASS_NAME, 'js-result-pagination-last').text
        return int(num_pages)

    def go_to_next_page(self):
        next_page = self.find_element(By.CLASS_NAME, 'c-result-pagination__link.c-result-pagination__link--next.ml-1.js-result-pagination-next')
        next_page.click()

    def get_daad_results(self):
        uni_section_element = self.find_element(By.CLASS_NAME, 'js-result-list-content')
        daad_section = DaadData(uni_section_element)

        # getting all the data
        scraped_data = daad_section.get_data()
        self.scraped_data.extend(scraped_data)

    def convert_into_csv(self):
        df = pd.DataFrame(self.scraped_data)
        df.to_csv('daad_data.csv', index=False)

    def convert_into_excel(self):
        df = pd.DataFrame(self.scraped_data)
        df.to_excel('daaddata.xlsx', index=False)