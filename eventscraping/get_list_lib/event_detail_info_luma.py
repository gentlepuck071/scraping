from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from common.start_webdriver_2 import start_driver_2
from common.utils import extract_numbers_with_regex
import time

def get_detail_info_luma (event):
    url = event.get("href")
    driver = start_driver_2()
    driver.get(url)
    delay = 3
    time.sleep(delay)
    dom = bs(driver.page_source, "html.parser")
    event_detail_info = {}

    try:
        try:
            is_left_right = driver.find_element(By.CLASS_NAME, 'event-page-right').is_displayed()
         
            left_element = driver.find_element(By.CLASS_NAME, 'event-page-left')
            right_element = driver.find_element(By.CLASS_NAME, 'event-page-right')
            image_element = left_element.find_element(By.CLASS_NAME, "cover-image.rounded")
            img = image_element.find_element(By.TAG_NAME, "img")
            img_src = img.get_attribute("src")
            event_detail_info['image'] = img_src
            content_cards = left_element.find_elements(By.CSS_SELECTOR, "div.event-page-desktop-only > div.content-card")

            for content_card in content_cards:

                if 'Presented by' in content_card.text:
                    presenters = []
                    presenters_elements = content_card.find_elements(By.CSS_SELECTOR, "div > div > div.jsx-1380439751.felx-center.gap-2")

                    for element in presenters_elements:
                        presenter = {}
                        presenter_img = element.find_element(By.TAG_NAME, "img")
                        presenter_img_src = presenter_img.get_attribute("src")
                        presenter['avatar'] = presenter_img_src
                        presenter_div = element.find_element(By.CSS_SELECTOR, "div > a > div > div")
                        presenter['name'] = presenter_div.text
                        presenters.append(presenter)

                    event_detail_info['presenter'] = presenters
                    continue
                if 'Hosted By' in content_card.text:
                    organizers = []
                    organizer_element = content_card.find_element(By.CSS_SELECTOR, "div.jsx-4155675949.content > div.jsx-591752197.flex-column.hosts")
                    organizers_elements = organizer_element.find_elements(By.CLASS_NAME, 'jsx-591752197.flex-center.gap-2')

                    for element in organizers_elements:
                        organizer = {}
                        organizer_avatar = element.find_element(By.CSS_SELECTOR, "div.avatar")
                        organizer_img = organizer_avatar.value_of_css_property('background-image')
                        organizer["avatar"] = organizer_img.lstrip('url("').rstrip('")')
                        organizer_name = element.find_element(By.CSS_SELECTOR, "div.jsx-591752197.fw-medium.text-ellipses")
                        organizer["name"] = organizer_name.text
                        organizers.append(organizer)

                    event_detail_info['organizers'] = organizers
                    continue
                if 'Going' in content_card.text:
                    participants = 0
                    participants_element = content_card.find_element(By.CLASS_NAME, "jsx-4155675949.title-label.text-tinted.fs-sm")
                    participants_str = participants_element.text
                    participants_array = extract_numbers_with_regex(participants_str)
                    participants = participants_array[0]
                    event_detail_info['participants'] = participants

            top_element = right_element.find_element(By.CSS_SELECTOR, 'div.top-card-content')
            title_element = top_element.find_element(By.CSS_SELECTOR, 'h1.title')
            title = title_element.text
            event_detail_info["title"] = title
            row_elements = top_element.find_elements(By.CLASS_NAME, 'row-container')
            event_date = row_elements[0].find_element(By.CLASS_NAME, 'jsx-2370077516.title.text-ellipses').text
            event_time = row_elements[0].find_element(By.CLASS_NAME, 'jsx-2370077516.desc.text-ellipses').text
            event_detail_info["time"] = event_date + event_time
            event_street_addr = row_elements[1].find_element(By.CLASS_NAME, 'jsx-3850535622.text-ellipses')
            event_local_addr = row_elements[1].find_element(By.CLASS_NAME, 'jsx-2370077516.desc.text-ellipses')
            event_addr = {}
            event_addr["streetAddr"] = event_street_addr.text
            event_addr["localAddr"] = event_local_addr.text
            event_detail_info["addr"] = event_addr

            tags = []
            base_card = right_element.find_element(By.CLASS_NAME, 'base-11-card')
            if base_card:
                tag = base_card.find_element(By.CLASS_NAME, 'jsx-3783920370.title.fw-medium').text
                tags.append(tag)

            event_detail_info["tags"] = tags

            right_cards = driver.find_elements(By.CLASS_NAME, 'event-page-right > div.content-card')

            for element in right_cards:

                if 'About Event' in element.text:
                    description_element = element.find_element(By.CSS_SELECTOR, 'div.mirror-content')
                    event_description = description_element.get_attribute('innerHTML')
                    event_detail_info["description"] = event_description
                    continue

                if 'Location' in element.find_element(By.CSS_SELECTOR, 'div.card-title').text:
                    event_street_addr = element.find_element(By.CLASS_NAME, 'jsx-2999812480.fw-medium')
                    event_local_addr = element.find_element(By.CLASS_NAME, 'jsx-2999812480.text-tinted.fs-sm.mt-1')
                    event_addr = {}
                    event_addr["streetAddr"] = event_street_addr.text
                    event_addr["localAddr"] = event_local_addr.text
                    if "addr" not in event_detail_info or event_detail_info["addr"] is None:
                        event_detail_info["addr"] = event_addr
                    continue
        except NoSuchElementException:
            is_left_right = False

            try:
                is_top_bottom = driver.find_element(By.CLASS_NAME, "top-card").is_displayed()

                top_element = driver.find_element(By.CLASS_NAME, "top-card")
                image_element = top_element.find_element(By.CLASS_NAME, "img-aspect-ratio.cover-image")
                img = image_element.find_element(By.TAG_NAME, "img")
                img_src = img.get_attribute("src")
                event_detail_info["image"] = img_src

                top_card = top_element.find_element(By.CLASS_NAME, "top-card-cocntent")
                title_element = top_card.find_element(By.TAG_NAME, "h1")
                title = title_element.text
                event_detail_info["title"] = title

                organizers = []
                organizer = {}
                organizer_element = top_card.find_element(By.CLASS_NAME, "hosts")
                organizer_avatar = organizer_element.find_element(By.CLASS_NAME, "jsx-4070717398.avatar")
                organizer_img = organizer_avatar.value_of_css_property('background-image')
                organizer["avatar"] = organizer_img.lstrip('url("').rstrip('")')
                organizer_name = organizer_element.find_element(By.CLASS_NAME, "jsx-1290421626.text-ellipses").text
                organizer["name"] = organizer_name.replace('Hosted by ', '')
                organizers.append(organizer)
                event_detail_info["organizers"] = organizers

                row_elements = top_card.find_elements(By.CLASS_NAME, "row-container")
                event_date = row_elements[0].find_element(By.CLASS_NAME, "jsx-2370077516.title.text-ellipses").text
                event_time = row_elements[0].find_element(By.CLASS_NAME, "jsx-2370077516.desc.text-ellipses").text
                event_detail_info["addr"] = event_addr

                bottom_element = driver.find_element(By.CLASS_NAME, 'bottom-section')
                content_card = bottom_element.find_elements(By.CLASS_NAME, "content-card")
                for content_card in content_cards:
                    tags = []
                    card_title = content_card.find_element(By.CLASS_NAME, "card-title").text
                    if card_title == "Registration":
                        if "Approval Required" in content_card.text:
                            tags.append("Approval Required")
                            event_detail_info["tags"] = tags
                        continue
                    if card_title == "About Event":
                        description_element = content_card.find_element(By.CSS_SELECTOR, 'div.mirror-content')
                        event_description = description_element.get_attribute('innerHTML')
                        event_detail_info["description"] = event_description
                        continue

                    if card_title == "Location":
                        event_street_addr = content_card.find_element(By.CLASS_NAME, 'jsx-116709410.fw-medium')
                        event_local_addr = content_card.find_element(By.CLASS_NAME, 'jsx-116709410.text-tinted.fs-sm.mt-1')
                        event_addr = {}
                        event_addr["streetAddr"] = event_street_addr.text
                        event_addr["localAddr"] = event_local_addr.text
                        if "addr" not in event_detail_info or event_detail_info["addr"] is None:
                            event_detail_info["addr"] = event_addr
                        continue

                    if card_title == "People":
                        content_element = content_card.find_element(By.CLASS_NAME, "content")
                        title = content_element.find_element(By.CLASS_NAME, "title").text
                        if title == "Hosts":
                            if "organizers" not in event_detail_info or event_detail_info["organizers"] is None:
                                organizers = []
                                organizer_element = content_element.find_element(By.CSS_SELECTOR, "div.jsx-956617335.flex-column.hosts")
                                organizers_elements = organizer_element.find_elements(By.CLASS_NAME, 'jsx-956617335.flex-center.gap-2')

                                for element in organizers_elements:
                                    organizer = {}
                                    organizer_avatar = element.find_element(By.CSS_SELECTOR, "div.avatar")
                                    organizer_img = organizer_avatar.value_of_css_property('background-image')
                                    organizer["avatar"] = organizer_img.lstrip('url("').rstrip('")')
                                    organizer_name = element.find_element(By.CSS_SELECTOR, "div.jsx-956617335.fw-medium.text-ellipses")
                                    organizer["name"] = organizer_name.text
                                    organizers.append(organizer)
                                
                                event_detail_info['organizers'] = organizers

                        participants = 0
                        participants_element = content_element.find_element(By.CSS_SELECTOR, "div.jsx-956617335 > div.jsx-956617335.flex-baseline.spread.title-row")
                        participants_str = participants_element.text
                        participants_array = extract_numbers_with_regex(participants_str)
                        participants = participants_array[0]
                        event_detail_info['participants'] = participants

                        continue

            except NoSuchElementException:
                is_top_bottom = False


    except TimeoutException:
        print("Timed out waiting for time line to load")

    except Exception as e:
        print(f'error: {e}')

    return event_detail_info