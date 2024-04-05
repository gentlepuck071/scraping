# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from common.categoies_list import web3_categories_list
from common.start_webdriver_2 import start_driver_2
from common.utils import check_keywords_in_title
import time

def get_event_list(href, type):
    url = href
    driver = start_driver_2()
    driver.get(url)
    delay = 3
    time.sleep(delay)
    print("Page Loaded Completely")

    data_list = []
    try:
        if type == "topic":
            topic = driver.find_element(By.CSS_SELECTOR, 'div.jsx-212035885.flex-column.header h1')
            print(topic.text)
            print(web3_categories_list)
            is_topic = check_keywords_in_title(topic, web3_categories_list)
            if is_topic:
                is_web3 = True
            else:
                is_web3 = False

        else:
            is_web3 = False
        card_wrappers = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card-wrapper')))
        for card_wrapper in card_wrappers:
            unit_data = {}

            try:
                a_tag = card_wrapper.find_element(By.CSS_SELECTOR, 'a.event-link')
                unit_data['href'] = a_tag.get_attribute('href')

                h3_tag = card_wrapper.find_element(By.CLASS_NAME, 'jsx-3851280986')
                unit_data['title'] = h3_tag.text
                
                # summarytag = card_wrapper.find_element(By.CLASS_NAME, 'jsx-1290421626 text-ellipses')
                # unit_data['summary'] = summarytag.text

                # descriptiontag = card_wrapper.find_element(By.CLASS_NAME, 'mirror-content')
                # unit_data['description'] = descriptiontag.text

                organizertag = card_wrapper.find_elements(By.CLASS_NAME, 'jsx-3575689807.text-ellipses')
                unit_data['organizer'] = organizertag[0].text

                locationtag = card_wrapper.find_elements(By.CLASS_NAME, 'jsx-3575689807.text-ellipses')
                unit_data['location'] = locationtag[1].text
                

                imgurltag = card_wrapper.find_element(By.CSS_SELECTOR, 'img.jsx-4068354093')
                unit_data['imgurl'] = imgurltag.get_attribute('src')
                
                pill_labels = card_wrapper.find_elements(By.CLASS_NAME, 'jsx-146954525.pill-label')
                pill_label_texts = [label.text for label in pill_labels]
                unit_data['tags'] = pill_label_texts

                if is_web3:
                    data_list.append(unit_data)
                else:
                    # print("======================================================================================")
                    print(unit_data)
                    # print(web3_categories_list)
                    isInclude = check_keywords_in_title(unit_data['title'], web3_categories_list)
                    if(isInclude):
                        data_list.append(unit_data)

            except NoSuchElementException:
                print("Unable to locate elements in card-wrapper")

    except TimeoutException:
        print("Timed out waiting for time line to load")
    except Exception as e:
        print(f'error: {e}')

    return data_list