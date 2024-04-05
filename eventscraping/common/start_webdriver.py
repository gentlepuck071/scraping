from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import urllib

def start_driver():

        options = webdriver.ChromeOptions()
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--disable-extensions')  
        options.add_argument('--start-maximized')   
        options.add_argument('--no-sandbox')  
        options.add_argument('--disable-dev-shm-usage') 
        options.add_argument("headless")

        chrome_prefs = {
            "profile.default_content_setting_values": {
                "images": 2,
                "javascript": 2,
            }
        }
        options.experimental_options["prefs"] = chrome_prefs

        try:
            driver = webdriver.Chrome(options=options)
        except ValueError :
        #     driver_path = ChromeDriverManager().install()
        #     service = Service(executable_path=driver_path)
        #     driver = webdriver.Chrome(service=service, options=options, )
        # finally:
            latest_chromedriver_version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
            latest_chromedriver_version = urllib.request.urlopen(latest_chromedriver_version_url).read().decode('utf-8')
            service = Service(ChromeDriverManager(driver_version=latest_chromedriver_version).install())

            print(service, options)

            driver = webdriver.Chrome(service=service, options=options)
       
        return driver