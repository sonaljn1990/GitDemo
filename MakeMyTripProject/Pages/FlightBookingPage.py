from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from MakeMyTripProject.Locators.FlightLocators import flightLocators

class FlightBooking():
    def __init__(self, driver):
        self.driver = driver
        self.flight_option_xpath = flightLocators.flight_option_xpath
        self.round_trip_radio_button_select = flightLocators.round_trip_radio_button_select
        self.from_City_id = flightLocators.from_City_id
        self.from_text_box_xpath = flightLocators.from_text_box_xpath
        self.selection_in_from_field_xpath = flightLocators.selection_in_from_field_xpath
        self.to_city_xpath = flightLocators.to_city_xpath
        self.select_to_city_from_list_xpath = flightLocators.select_to_city_from_list_xpath
        self.Departure_xpath = flightLocators.Departure_xpath
        #self.from_month_xpath = flightLocators.from_month_xpath
        #self.from_date_xpath = flightLocators.from_date_xpath
        #self.expected_fr_date = flightLocators.expected_fr_date
        self.Departure_date_xpath = flightLocators.Departure_date_xpath
        #self.expected_to_date = '12'
        #self.departure_date_xpath = flightLocators.departure_date_xpath
        #self.select_departure_date_xpath = flightLocators.select_departure_date_xpath
        self.Return_xpath = flightLocators.Return_xpath
        self.return_date_xpath = flightLocators.return_date_xpath
        #self.select_return_date_xpath = flightLocators.select_return_date_xpath
        self.travellers_xpath = flightLocators.travellers_xpath
        self.no_of_adults_xpath = flightLocators.no_of_adults_xpath
        self.no_of_children_xpath = flightLocators.no_of_children_xpath
        self.no_of_infants_xpath = flightLocators.no_of_infants_xpath
        self.travel_class_xpath = flightLocators.travel_class_xpath
        self.apply_button_xpath = flightLocators.apply_button_xpath
        self.search_button_xpath = flightLocators.search_button_xpath
        self.search_not_found_xpath = flightLocators.search_not_found_xpath
        self.go_back_button_xpath = flightLocators.go_back_button_xpath

    def select_round_trip_option(self):
        self.driver.find_element_by_xpath(self.flight_option_xpath).click()
        self.driver.find_element_by_xpath(self.round_trip_radio_button_select).click()

    def select_from_city(self, from_city):
        self.driver.find_element_by_id(self.from_City_id).click()
        self.driver.find_element_by_xpath(self.from_text_box_xpath).click()
        self.driver.find_element_by_xpath(self.from_text_box_xpath).clear()
        self.driver.find_element_by_xpath(self.from_text_box_xpath).send_keys(from_city)
        self.driver.find_element_by_xpath(self.selection_in_from_field_xpath).click()

    def select_to_city(self, to_city):
        self.driver.find_element_by_xpath(self.to_city_xpath).click()
        self.driver.find_element_by_xpath(self.to_city_xpath).send_keys(to_city)
        self.driver.find_element_by_xpath(self.select_to_city_from_list_xpath).click()

    def select_departure_date(self):
        self.driver.find_element_by_xpath(self.Departure_xpath).click()
        self.driver.find_element_by_xpath(self.Departure_date_xpath).click()
        #Select(self.driver.find_element_by_xpath(self.from_month_xpath)).select_by_visible_text("July")
        #Select(self.driver.find_element_by_xpath(self.from_date_xpath)).select_by_visible_text("10")
        #self.driver.find_element_by_xpath(self.select_departure_date_xpath).click()

    def select_return_date(self):
        self.driver.find_element_by_xpath(self.Return_xpath).click()
        self.driver.find_element_by_xpath(self.return_date_xpath).click()
        #self.driver.find_element_by_xpath(self.select_return_date_xpath).click()

    def select_travellers_information(self):
        self.driver.find_element_by_xpath(self.travellers_xpath).click()
        self.driver.find_element_by_xpath(self.no_of_adults_xpath).click()
        self.driver.find_element_by_xpath(self.no_of_children_xpath).click()
        self.driver.find_element_by_xpath(self.no_of_infants_xpath).click()
        self.driver.find_element_by_xpath(self.apply_button_xpath).click()

    def perform_search_for_flights(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
        assert self.driver.find_element_by_xpath(self.search_not_found_xpath).is_displayed(),"Flights are available,please select"
        print("Please perform Refresh search")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.go_back_button_xpath).click()


