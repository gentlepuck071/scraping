from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from common.start_webdriver_2 import start_driver_2
from common.utils import check_keywords_in_title
from common.categoies_list import web3_categories_list

def get_event_list(url):
    url = url + "/?oage="
    driver = start_driver_2()
    try:
        event_list = []
        is_end = False
        page = 1
        while not is_end:
            page_url = url +str (page)
            driver.get(page_url)
            delay = 10
            time.sleep(delay)
            dom = bs(driver.page_source, "html.parser")
            try:
                search_result_element = driver.find_element(By.CSS_SELECTOR, "ul.SearchResultPanelContentEventCardList-module__eventList___1YEh_")
                is_search_result = search_result_element.is_displayed()
                page += 1
                event_elements = search_result_element.find_elements(By.TAG_NAME, "li")
                for element in event_elements:
                    event = {}
                    event_card = element.find_element(By.CSS_SELECTOR, "div.discover-search-desktop-card")
                    event_detail = event_card.find_element(By.CSS_SELECTOR, "section.event-card-details")
                    title_element = event_detail.find_element(By.CSS_SELECTOR, "div.Stack_root__1ksk7>a")
                    event_url = title_element.get_attribute("href")
                    event_title = title_element.text
                    event["href"] = event_url
                    event["title"] = event_title
                    event_list.append(event)
            except NoSuchElementException:
                is_search_result = False
                is_end = True

    finally:
        driver.quit()


    return event_list            