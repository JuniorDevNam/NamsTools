from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

# Khởi tạo trình duyệt
driver = webdriver.Firefox()

# Mở trang web
driver.get('your_website_url')

# Cuộn trang từ đầu đến cuối
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

# Tìm tất cả các phần tử hình ảnh
images = driver.find_elements_by_tag_name('img')

# Tạo thư mục để lưu hình ảnh
if not os.path.exists('images'):
    os.makedirs('images')

# Tải và lưu hình ảnh
for i, img in enumerate(images):
    src = img.get_attribute('src')
    if src is not None:
        response = requests.get(src)
        with open(f'images/{str(i).zfill(4)}.jpg', 'wb') as f:
            f.write(response.content)

# Đóng trình duyệt
driver.close()