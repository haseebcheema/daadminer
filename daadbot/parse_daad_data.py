from selenium.webdriver.common.by import By


class DaadData:

    def __init__(self, uni_section_element):
        self.uni_section_element = uni_section_element
        self.uni_cards = self.pull_uni_cards()

    def pull_uni_cards(self):
        return self.uni_section_element.find_elements(By.CLASS_NAME, 'c-ad-carousel')

    def get_data(self):
        scraped_data = []

        for single_uni_card in self.uni_cards:
            card_data = {}

            # course title
            course_title = single_uni_card.find_element(By.CLASS_NAME, 'js-course-title').text
            card_data['Course Title'] = course_title

            # course type
            course_type = single_uni_card.find_element(By.CLASS_NAME, 'c-ad-carousel__course-type').text
            course_type = course_type.strip('•').strip()
            card_data['Course Type'] = course_type

            # university name
            university = single_uni_card.find_element(By.CLASS_NAME, 'js-course-academy').text
            university = university.strip('•').strip()
            card_data['University'] = university

            # location
            location = single_uni_card.find_element(By.CLASS_NAME, 'c-ad-carousel__subtitle--location').text
            card_data['Location'] = location

            # subject, semester start, tuition fee
            ul_list = single_uni_card.find_elements(By.CLASS_NAME, 'c-ad-carousel__data-list')
            subject = ul_list[0].find_element(By.CLASS_NAME, 'c-ad-carousel__data-item').text
            card_data['Subject'] = subject

            semester_start = ul_list[0].find_elements(By.CLASS_NAME, 'c-ad-carousel__data-item')[1].text
            card_data['Beginning'] = semester_start

            tuition_fee = ul_list[0].find_elements(By.CLASS_NAME, 'c-ad-carousel__data-item')[2].text
            card_data['Tuition Fee'] = tuition_fee

            # language and duration
            language = ul_list[1].find_element(By.CLASS_NAME, 'c-ad-carousel__data-item').text
            card_data['Language'] = language

            duration = ul_list[1].find_elements(By.CLASS_NAME, 'c-ad-carousel__data-item')[1].text
            card_data['Duration'] = duration

            # links
            link = single_uni_card.find_element(By.CLASS_NAME, 'js-course-detail-link').get_attribute('href')
            card_data['Link'] = link

            scraped_data.append(card_data)

        return scraped_data
