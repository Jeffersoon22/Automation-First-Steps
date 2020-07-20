import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StepsForTest():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def go_to_google(self):
        self.driver.get('https://www.google.com')

    def search_In_GoogLe(self, text):
        element = self.driver.find_element_by_xpath("//input[@name='q']")
        element.send_keys(text)
        element.send_keys(Keys.RETURN)
        time.sleep(0.5)

    def check_title_contains(self):
        result = EC.title_contains('სამი გოჭი')
        return result

    def check_clear_button(self):
        button = self.driver.find_element_by_xpath("//div[@role='button'][@aria-label='გასუფთავება']")
        return button

    def count_results(self):
        search_result = len(self.driver.find_elements_by_xpath("//div[@class='g']"))
        return search_result

    def check_all_title_contain(self):
        time.sleep(0.5)
        heads = len(self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md']"))
        heads_which_contains = len(
            self.driver.find_elements_by_xpath("//h3[@class='LC20lb DKV0Md'][contains(text(), 'სამი გოჭი')]"))
        if heads == heads_which_contains:
            return True
        else:
            return False

    def go_to_Photos_page(self):
        element = self.driver.find_element_by_xpath("//a[text()='სურათები']")
        element.click()

    def check_Search_By_Photo_button_exist(self):
        button = self.driver.find_element_by_xpath("//span[@aria-label='Search by image']")
        return button

    def open_picture_from_youtube(self):
        photos_from_youtube = self.driver.find_elements_by_xpath("//div[@class='fxgdke'][text()='youtube.com']")
        random_element = photos_from_youtube[0].find_element_by_xpath('./../../..')
        random_element.click()
        time.sleep(0.7)

    # check photo attributes
    def check_photo_close_button(self):
        closeButton = self.driver.find_element_by_xpath("//a[@aria-label='Close'][@role='button']")
        return closeButton

    def check_image_exist(self):
        image = self.driver.find_element_by_xpath("//img[@class='n3VNCb']")
        return image

    def check_youtube_button_exits(self):
        youTubeButton = self.driver.find_element_by_xpath("//a[@aria-label='Visit YouTube'][@role='button']")
        youtubeSpan = youTubeButton.find_element_by_xpath("//span[text()='YouTube']")
        if youtubeSpan and youTubeButton:
            return youTubeButton

    def check_share_button_exist(self):
        shareButton = self.driver.find_element_by_xpath("//a[@role='button'][@aria-label='Share']")
        return shareButton

    def check_more_options_button(self):
        button = self.driver.find_element_by_xpath("//a[@role='button'][@aria-label='More Options']")
        return button

    def check_get_help_button(self):
        getHelpButton = self.driver.find_element_by_xpath("//div[@class='L43GYb']").find_element_by_xpath(
            "//span[text()='Get help']")
        return getHelpButton

    def check_feedback_button(self):
        feedbackButton = self.driver.find_element_by_xpath("//div[@class='L43GYb']").find_element_by_xpath(
            "//span[text()='Send feedback']")
        return feedbackButton

    def title_of_photo(self):
        title_of_Photo = self.driver.find_element_by_xpath("//a[@class='Beeb4e']")
        if title_of_Photo:
            return True

    def youtube_watch_button_exist(self):
        buttonForWatch = self.driver.find_element_by_xpath("//div[@class='yscHWb mkSNZe']")
        return buttonForWatch

    def youtube_watch_time(self):
        watchAndTime = self.driver.find_element_by_xpath(".//span[@class='UiOOze']")
        return watchAndTime.text

    def check_author(self):
        author = self.driver.find_element_by_xpath(".//span[@class='Nngn4d mkSNZe cNGt9e']")
        return author.text

    def views_and_likes(self):
        viewsAndLikesOfVideo = self.driver.find_element_by_xpath(".//div[@class='gvZQHb UDylye']")
        return viewsAndLikesOfVideo.text

    def related_images(self):
        relatedImagesTitle = self.driver.find_element_by_xpath("//div[@class='dPO1Qe gadasb']")
        relatedImagesDiv = self.driver.find_element_by_xpath("//div[@class='EVPn8e'][@role='list']")
        if relatedImagesDiv and relatedImagesTitle:
            return True
        else:
            return False

    def clear_input(self):
        element = self.driver.find_element_by_xpath("//input[@name='q']")
        element.clear()

    def input_search(self, text):
        element = self.driver.find_element_by_xpath("//input[@name='q']")
        element.send_keys(text)
        return element.get_attribute('value')

    def count_photos(self):
        photos = self.driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
        return len(photos)

    def count_contain_title(self):
        titles_contain = self.driver.find_elements_by_xpath("//*[contains(text(), 'სამი გოჭი')]")
        return len(titles_contain)

    def driver_close(self):
        time.sleep(3)
        self.driver.quit()
