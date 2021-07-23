class HotelsLocators:

    Hotel_text_xpath = "//span[text()='Hotels']"
    city_id = "city"
    enter_city_text_box_xpath = "//input[contains(@placeholder,'Enter city/ Hotel/ Area/ Building')]"
    selected_city_xpath = "//p[contains(text(),'Leh, Ladakh, India')]"
    checkin_id = "checkin"
    checkin_date_xpath = "//div[@aria-label='Sat Jul 10 2021']"
    #select_checkout_date_xpath = "//span[text()='Select Checkout Date']"
    checkout_date_xpath = "//div[@aria-label='Tue Jul 13 2021']"
    rooms_guest_id = "guest"
    no_of_rooms_xpath = "//li[@data-cy='adults-2']/../li[1]"
    no_of_childrens_xpath = "//li[@data-cy='children-1']"
    age_of_child_xpath = "//option[@data-cy='childAgeValue-3']"
    apply_button_xpath = "//button[text()='APPLY']"
    search_button_id = "hsw_search_button"
    page_title_xpath = "//p[text()='Hotels, Villas, Apartments and more in Leh']"
    Free_Cancellation_checkbox_xpath = "//p[text()='Free Cancellation']"
    guest_house_xpath = "//span[text()='Deskit Villa Guest House']"    #perform scrolling to find out it
    #switch to next tab
    book_this_now_id = "detpg_headerright_book_now"
    guest_details_xpath = "//span[text()='GUEST DETAILS']"   #perform scrolling to find out it
    i_am_booking_for_myself_xpath = "//label[text()='Myself']"
    title_xpath = "//select[@id='title']"
    Mrs_xpath = "//option[@value='Mrs']"
    #scrooling till Pay now button
    Pay_now_button_xpath = "//a[text()='Pay Now']"
