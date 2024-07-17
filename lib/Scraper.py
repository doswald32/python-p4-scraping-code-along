from bs4 import BeautifulSoup 
import requests
import ipdb
import Course
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ipdb

# class Scraper:
    
#     def __init__(self):
#         self.courses = []
    
#     def get_page():
#         url = "https://app.membersports.com/tee-times/3697/4758/0/3/false"
#         doc =  BeautifulSoup(requests.get(f'{url}').text, 'html.parser')
#         ipdb.set_trace()

# class Scraper:
    
#     def __init__(self):
#         self.courses = []
    
#     def get_page(self):
#         url = "https://app.membersports.com/tee-times/3697/4758/0/3/false"
#         response = requests.get(url)
#         if response.status_code == 200:
#             doc = BeautifulSoup(response.text, 'html.parser')
#             ipdb.set_trace()
#             times = doc.find_all('div', class_='timeCol')
#             return times
#         else:
#             print("Failed to retrieve the page.")
#             return None

# scraper = Scraper()
# times = scraper.get_page()
# print(times)

class Scraper:
    
    def __init__(self):
        self.courses = []
    
    def get_page(self):

        courses = {
            "Foothills Par 3": 0,
            "Foothills Executive 9": 0,
            "Foothills 18": 0,
            "Foothills": 0,
            "Meadows": 0,
            "Meadows Back Nine": 0
        }

        url = "https://app.membersports.com/tee-times/3697/4758/0/3/false"
        
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode

        # Path to your ChromeDriver
        driver_path = '/usr/bin/chromedriver'
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)

        # Wait for the element with the class name 'timeCol' to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'timeCol'))
        )
        
        # Get the page source and parse it with BeautifulSoup
        page_source = driver.page_source
        doc = BeautifulSoup(page_source, 'html.parser')

        date_raw = doc.select('.dateFormat')
        full_date = date_raw[0].text.replace(u'\xa0', u' ')

        availability = {full_date:
                            {'06:00 AM':
                                {
                                    "Foothills Par 3": 0,
                                    "Foothills Executive 9": 0,
                                    "Foothills 18": 0,
                                    "Foothills": 0,
                                    "Meadows": 0,
                                    "Meadows Back Nine": 0
                                }
                             }

                        }

        ipdb.set_trace()
        
        # Find the elements with the class 'timeCol'
        times = doc.find_all('div', class_='timeCol')
        
        driver.quit()
        
        return times

scraper = Scraper()
times = scraper.get_page()
print(times)
