from selenium import webdriver
import time
import openpyxl
from MakeMyTripProject.Locators.HotelsLocators import HotelsLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class HotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.Hotel_text_xpath = HotelsLocators.Hotel_text_xpath
        self.city_id = HotelsLocators.city_id
        self.enter_city_text_box_xpath = HotelsLocators.enter_city_text_box_xpath
        self.selected_city_xpath = HotelsLocators.selected_city_xpath
        self.checkin_id = HotelsLocators.checkin_id
        self.checkin_date_xpath = HotelsLocators.checkin_date_xpath
        self.checkout_date_xpath = HotelsLocators.checkout_date_xpath
        self.rooms_guest_id = HotelsLocators.rooms_guest_id
        self.no_of_rooms_xpath = HotelsLocators.no_of_rooms_xpath
        self.no_of_childrens_xpath = HotelsLocators.no_of_childrens_xpath
        self.age_of_child_xpath = HotelsLocators.age_of_child_xpath
        self.apply_button_xpath = HotelsLocators.apply_button_xpath
        self.search_button_id = HotelsLocators.search_button_id
        self.page_title_xpath = HotelsLocators.page_title_xpath

    def click_on_hotels(self):
        self.driver.find_element_by_xpath(self.Hotel_text_xpath).click()

    def click_on_city_box(self):
        self.driver.find_element_by_id(self.city_id).click()

    def click_on_enter_city_text_box(self,cityname):
        self.driver.find_element_by_xpath(self.enter_city_text_box_xpath).click()
        self.driver.find_element_by_xpath(self.enter_city_text_box_xpath).send_keys(cityname)
        self.driver.find_element_by_xpath(self.selected_city_xpath).click()

    def click_on_checkin_date(self):
        self.driver.find_element_by_id(self.checkin_id).click()
        self.driver.find_element_by_xpath(self.checkin_date_xpath).click()

    def click_on_checkout_date(self):
        self.driver.find_element_by_xpath(self.checkout_date_xpath).click()

    def fill_room_guest_details(self):
        self.driver.find_element_by_id(self.rooms_guest_id).click()
        self.driver.find_element_by_xpath(self.no_of_rooms_xpath).click()
        self.driver.find_element_by_xpath(self.no_of_childrens_xpath).click()
        self.driver.find_element_by_xpath(self.age_of_child_xpath).click()
        self.driver.find_element_by_xpath(self.apply_button_xpath).click()

    def click_on_search_button(self):
        self.driver.find_element_by_id(self.search_button_id).click()
        self.driver.find_element_by_xpath(self.page_title_xpath).is_displayed()



