from selenium import webdriver
import time
import openpyxl
import unittest

workbook = openpyxl.load_workbook("D:/Python practice files/MMT.xlsx")
sheet = workbook.active
import MakeMyTripProject.Pages.HotelsPage

class test_HotelBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_hotel_search(self):
        driver = self.driver
        driver.get("https://makemytrip.com/")
        driver.implicitly_wait(10)
        hotelsearch = MakeMyTripProject.Pages.HotelsPage.HotelPage(driver)
        hotelsearch.city = sheet.cell(row=7, column=2).value
        hotelsearch.click_on_hotels()
        hotelsearch.click_on_city_box()
        hotelsearch.click_on_enter_city_text_box(hotelsearch.city)
        hotelsearch.click_on_checkin_date()
        hotelsearch.click_on_checkout_date()
        hotelsearch.fill_room_guest_details()
        hotelsearch.click_on_search_button()
        print("GitHub command to check")
        print("GitHub command to check")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


workbook.save("D:/Python practice files/MMT.xlsx")

if __name__ == "__main__":
    unittest.main()
