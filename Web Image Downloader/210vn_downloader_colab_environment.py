from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
from urllib.parse import urlparse, urlunparse
import time

# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path=r'/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service,options=options)

# Truy cập trang web
url = input("Nhập URL của trang web: ")
driver.get(url)

# Cuộn trang từ đầu đến cuối
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(7)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

# Tìm tất cả thẻ <img> trong thẻ <div id=image>
images = driver.find_elements_by_tag_name('img')

# Tạo thư mục để lưu hình ảnh nếu nó chưa tồn tại
if not os.path.exists('images'):
    os.makedirs('images')

# Duyệt qua từng hình ảnh và tải về
for i, img in enumerate(images, start=1):
    # Lấy URL của hình ảnh
    src = img.get_attribute('data-src')
    parsed_url = urlparse(src)

    # Trích xuất tên file từ phần đường dẫn của URL
    image_name = os.path.basename(parsed_url.path)

    # Tạo URL mới với cấu trúc đã chỉ định
    new_url = urlunparse(('https', 'i3.hhentai.net', '/images/2023/09v2/01/' + image_name + '?imgmax=1200', '', '', ''))

    # Tạo tên file theo số thứ tự từ 0001 đến 9999
    file_name = os.path.join('images', f'{i:04}.jpg')

    # Tải hình ảnh về
    urllib.request.urlretrieve(new_url, file_name)

# Đóng trình duyệt
driver.quit()
