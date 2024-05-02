#import requests
#from bs4 import BeautifulSoup
#from lxml import html
from os import system as run
from os.path import join
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#https://toilanam.wordpress.com/2024/02/15/thiet-lap-chrome-webdriver-tren-google-colab/
chromedrv = join(sys.path[0], "chromedriver.exe")
dir_path = join(sys.path[0], "downloads")
prefs = {"download.default_directory" : dir_path}
#example: prefs = {"download.default_directory" : "C:\Tutorial\down"}
# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#Thêm 1 số option cho chrome như kích thước windows, chế độ ẩn danh, ...
options.add_argument("--incognito")
#options.add_argument("--window-size=300x400")
options.add_experimental_option("prefs",prefs)
service = Service(executable_path=chromedrv)
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, 20)
    
def waitUntilDownloadCompleted(maxTime=600):
    driver.execute_script("window.open()")
    # switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    # navigate to chrome downloads
    driver.get('chrome://downloads')
    # define the endTime
    endTime = time.time() + maxTime
    while True:
        try:
            # get the download percentage
            downloadPercentage = driver.execute_script(
                "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
            # check if downloadPercentage is 100 (otherwise the script will keep waiting)
            if downloadPercentage == 100:
                # exit the method once it's completed
                return downloadPercentage
        except:
            pass
        # wait for 1 second before checking the percentage next time
        time.sleep(1)
        # exit method if the download not completed with in MaxTime.
        if time.time() > endTime:
            break

def getvideo_selenium(web):
    width = 500
    height = 400
    driver.set_window_size(width, height)
    # Mở trang web
    driver.get(web)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/input[1]'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div[4]/div[3]/div/a[1]'))).click()
    #link = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div[4]/div[3]/div/a[1]")
    waitUntilDownloadCompleted(120)

getvideo_selenium("https://rule34video.com/video/3350934/privaty-consomekitchen/")