#import requests
#from bs4 import BeautifulSoup
#from lxml import html
#from os.path import join
from os import system as run
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#https://toilanam.wordpress.com/2024/02/15/thiet-lap-chrome-webdriver-tren-google-colab/

def getvideo_selenium_colab(web):
    # Khởi tạo trình duyệt
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #Thêm 1 số option cho chrome như kích thước windows, chế độ ẩn danh, ...
    #options.add_argument("--incognito")
    options.add_argument("--window-size=1920x1080")
    service = Service(executable_path=r'/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service,options=options)
    # Mở trang web
    driver.get(web)
    time.sleep(5)
    link = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div[4]/div[3]/div/a[1]")
    run(f'wget {link}')
def getvideo_selenium(web, driver_path):
    # Khởi tạo trình duyệt
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #Thêm 1 số option cho chrome như kích thước windows, chế độ ẩn danh, ...
    #options.add_argument("--incognito")
    options.add_argument("--window-size=1920x1080")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service,options=options)
    # Mở trang web
    driver.get(web)
    time.sleep(5)
    links = driver.find_elements(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div[4]/div[3]/div/a[1]")
    print(links)

getvideo_selenium("https://rule34video.com/video/3295189/legend-clover-mansa-musa-2/",)