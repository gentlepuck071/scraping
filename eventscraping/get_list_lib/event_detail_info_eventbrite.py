from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from common.start_webdriver_2 import start_driver_2
from common.utils import extract_numbers_with_regex
import time


def get_detail_info_eventbrite (event):
    url = event.get("href")
    driver = start_driver_2()
    driver.get(url)
    delay = 3
    time.sleep(delay)
    dom = bs(driver.page_source, "html.parser")
    event_detail_info ={}

    try:
        hero_element = driver.find_element(By.CSS_SELECTOR, "div.event-hero-wrapper")
        event_img = hero_element.find_element(By.TAG_NAME, "img")
        img_src = event_img.get_attribute("src")
        event_detail_info["image"] = img_src
        main_element = driver.find_element(By.CLASS_NAME, "div[data-testid = 'mainContent']")
        title_element = main_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'title']")
        event_title = title_element.text
        event_detail_info["title"] = event_title
        summary_element = main_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'summary']")
        event_summary = summary_element.text
        event_detail_info["summary"] = event_summary
        organizers = []
        organizer_element = main_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'organizerBrief']")
        event_organizer = organizer_element.find_element(By.CSS_SELECTOR, "strong.organizer-listing-info-variant-b__name-link").text
        organizers.append(event_organizer)
        event_detail_info["organizers"] = organizers
        time_element = main_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'dateAndTime']")
        event_time = time_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'display-date-container']").text
        event_detail_info["time"] = event_time
        addr_element = main_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'location']")
        addr_div = addr_element.find_element(By.CLASS_NAME, "location-info__address")
        addr = {}
        street_addr = addr_div.find_element(By.TAG_NAME, "p").text
        local_addr = dom.find('div', attrs={'class': 'location-info__address'}).contents[1]
        addr["street_addr"] = street_addr
        addr["local_addr"] = local_addr
        event_detail_info["addr"] = addr
        description_element = main_element.find_element(By.CSS_SELECTOR, "div[data-testid = 'aboutThisEvent']")
        description_detail = description_element.find_element(By.CSS_SELECTOR, "#event-description")
        event_description = description_detail.get_attribute("innerHTML")
        event_detail_info["description"] = event_description

        price_element = dom.find('div', attrs={'class': "conversion-bar__body"})
        if price_element:
            price = price_element.text
            if price == "Sold Out":
                ticket = "sold out"
                isFree = False
            elif price == "Donation":
                ticket = "donation"
                isFree = True
            else:
                ticket = ""
                if price == "Free":
                    isFree = True
                else:
                    isFree = False
        else:
            price_element = driver.find_element(By.CSS_SELECTOR, "div.ticket-card-compact-size__price>span")
            if price_element:
                price = price_element.text
                if price == "Sold Out":
                    ticket = "sold out"
                    isFree = False
                elif price == "Donation":
                    ticket = "donation"
                    isFree = True
                else:
                    ticket = ""
                    if price == "Free":
                        isFree = True
                    else:
                        isFree = False
            else:
                ticket = ""
                isFree = False
        event_detail_info["ticket"] = ticket
        event_detail_info["isFree"] = isFree
        

    except Exception as e:
        print(f'error: {e}')

    finally:
        driver.quit()

    return event_detail_info
