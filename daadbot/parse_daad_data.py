from selenium.webdriver.common.by import By


class DaadData:

    def __init__(self, uni_section_element):
        self.uni_section_element = uni_section_element
        self.uni_cards = self.pull_uni_cards()

    def pull_uni_cards(self):
        return self.uni_section_element.find_elements(By.CLASS_NAME, 'c-ad-carousel')

    def get_data(self):
        for single_uni_card in self.uni_cards:

            # course title
            course_title = single_uni_card.find_element(By.CLASS_NAME, 'js-course-title').text
            print(course_title)

            # course type
            course_type = single_uni_card.find_element(By.CLASS_NAME, 'c-ad-carousel__course-type').text
            course_type = course_type.strip('•').strip()
            print(course_type)

            # university name
            university = single_uni_card.find_element(By.CLASS_NAME, 'js-course-academy').text
            university = university.strip('•').strip()
            print(university)

            # location
            location = single_uni_card.find_element(By.CLASS_NAME, 'c-ad-carousel__subtitle--location').text
            print(location)

            # subject, semester start, tuition fee
            ul_list = single_uni_card.find_elements(By.CLASS_NAME, 'c-ad-carousel__data-list')
            subject = ul_list[0].find_element(By.CLASS_NAME, 'c-ad-carousel__data-item').text
            print(subject)

            semester_start = ul_list[0].find_elements(By.CLASS_NAME, 'c-ad-carousel__data-item')[1].text
            print(semester_start)

            tuition_fee = ul_list[0].find_elements(By.CLASS_NAME, 'c-ad-carousel__data-item')[2].text
            print(tuition_fee)

            # language and duration
            language = ul_list[1].find_element(By.CLASS_NAME, 'c-ad-carousel__data-item').text
            print(language)

            duration = ul_list[1].find_elements(By.CLASS_NAME, 'c-ad-carousel__data-item')[1].text
            print(duration)

            # links
            link = single_uni_card.find_element(By.CLASS_NAME, 'js-course-detail-link').get_attribute('href')
            print(link)
