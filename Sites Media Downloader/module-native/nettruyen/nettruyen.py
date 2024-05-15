import requests
import urllib
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def onechapter(web):
    # Khởi tạo trình duyệt
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # Thêm 1 số option cho chrome như kích thước windows, chế độ ẩn danh, ...
    #options.add_argument('--disable-gpu')
    #options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("--incognito")
    #options.add_argument("--window-size=1920x1080")
    service = Service(executable_path=r'C:\Users\Dell 7390\Documents\NamsTools\Sites Media Downloader\module-native\nettruyen\chromedriver.exe')
    driver = webdriver.Chrome(service=service,options=options)
    # Mở trang web
    driver.get(web)

    SCROLL_PAUSE_TIME = 0.5
    i = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        i += 1
        if i == 5:  # Optional: Stop after a certain number of iterations
            break

    # Allow time for any remaining images to load
    driver.implicitly_wait(10)
    # Find all lazy-loaded images (adjust the selector as needed)
    shoe_images = driver.find_elements(By.CSS_SELECTOR, 'div.page-chapter img')
    print(shoe_images)
    # Download each image
    for index, img in enumerate(shoe_images):
        src = img.get_attribute("src")
        urllib.request.urlretrieve(src, f"image_{index}.png")

onechapter("https://nettruyencc.com/truyen-tranh/blue-archive-global/chapter-1/1")