import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.start_webdriver_2 import start_driver_2
from get_list_lib.city_event_list import get_event_list
from common.utils import remove_repeated_events
from get_list_lib.event_detail_info_luma import get_detail_info_luma
import requests

def get_list_luma():
    driver = start_driver_2()
    luma_url = 'https://lu.ma'
    driver.get(luma_url+'/explore')
    WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "div.can-divide")) )
    list_luma = []
    event_sections = driver.find_elements(By.CSS_SELECTOR, 'div.can-divide')
    city_event_elements = event_sections[0].find_elements(By.TAG_NAME, 'a')
    calender_event_elements = event_sections[1].find_elements(By.TAG_NAME, 'a')

    city_event_href_values = [element.get_attribute('href') for element in city_event_elements]
    for city_href in city_event_href_values:
        x = requests.post("http://127.0.0.1:8000/api/v1/web3events/new/", {"title": city_href, "summary": city_href})
        print(x)
        list_luma.extend(get_event_list(city_href, 'city'))

    calender_event_href_values = [element.get_attribute('href') for element in calender_event_elements]
    for calender_href in calender_event_href_values:
        x = requests.post("http://127.0.0.1:8000/api/v1/web3events/new/", {"title": calender_href, "summary": calender_href})
        print(x)
        list_luma.extend(get_event_list(calender_href, 'topic'))


    # filtered_event_list = remove_repeated_events(list_luma, "href")
    # print("count:", len(filtered_event_list))

get_list_luma()
    # event_detail_list = [get_detail_info_luma(filtered_event_list[0])]
    # return event_detail_list


    