from selenium import webdriver
from selenium.webdriver.common.by import By
import daadbot.constants as const
import os
from  daadbot.parse_daad_data import DaadData


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
        # self.get(const.BASE_URL)
        self.get("https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=Computer%20Science&degree%5B%5D=2&lang%5B%5D=2&fos=6&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&langDeAvailable=&langEnAvailable=&lvlEn%5B%5D=&modStd%5B%5D=&cit%5B%5D=&tyi%5B%5D=&ins%5B%5D=&fee=1&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&dur=&subjects%5B%5D=49&limit=10&offset=&display=list")

    def accept_cookies(self):
        cookies_btn = self.find_element(By.CLASS_NAME, 'snoop-button')
        cookies_btn.click()

    # def change_language(self):
    #     eng_language = self.find_element(By.CLASS_NAME, 'qa-language-item')
    #     eng_language.click()
    #
    # def go_to_international_programs(self):
    #     ul_list = self.find_element(By.CSS_SELECTOR, 'ul[aria-live="polite"]')
    #     link_to_programs = ul_list.find_elements(By.TAG_NAME, 'li')
    #     link_to_programs[2].click()
    #
    # def choose_programme(self, programme):
    #
    #     # enter programme in the input box
    #     input_field = self.find_element(By.CSS_SELECTOR, 'input[name="q"]')
    #     input_field.clear()
    #     input_field.send_keys(programme)
    #
    #     # select course
    #     course_type = self.find_element(By.CSS_SELECTOR, 'button[title="Please select"]')
    #     course_type.click()
    #     select_course = self.find_element(By.CLASS_NAME, 'multiselect-container')
    #     masters_course = select_course.find_elements(By.CSS_SELECTOR, 'li input')
    #     masters_course[1].click()
    #
    #     # select language
    #     course_language = self.find_elements(By.CSS_SELECTOR, 'button[title="Please select"]')
    #     course_language[1].click()
    #     select_language = self.find_elements(By.CLASS_NAME, 'multiselect-container')
    #     eng_language = select_language[1].find_elements(By.CSS_SELECTOR, 'li input')
    #     eng_language[1].click()
    #
    #     # select course field
    #     course_field = self.find_element(By.CSS_SELECTOR, 'select[name="fos"]')
    #     course_field.click()
    #     select_field = course_field.find_element(By.CSS_SELECTOR, 'option[value="6"]')
    #     select_field.click()
    #
    #     # submit the form
    #     submit = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    #     submit.click()
    #
    # def apply_filters(self):
    #
    #     # select subject
    #     select_subject = self.find_elements(By.CLASS_NAME, 'c-multiselect')
    #     select_subject[1].click()
    #     select_cs = select_subject[1].find_element(By.CSS_SELECTOR, 'input[value="49"]')
    #     select_cs.click()
    #
    #     # select no fees
    #     select_fees = self.find_element(By.ID, 'filterFee')
    #     select_fees.click()
    #     no_fee_option = select_fees.find_element(By.CSS_SELECTOR, 'option[value="1"]')
    #     no_fee_option.click()
    #
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
        daad_section.get_data()