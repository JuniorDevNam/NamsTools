import requests
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import sys
import time
import random

debug_html = join(sys.path[0],"debug.html")
debug_html_ch = join(sys.path[0],"debug_ch.html")

#https://stackoverflow.com/questions/14587728/what-does-this-error-in-beautiful-soup-means
user_agent_list = [
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
   "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1",
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3",
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0"
]


def onechapter(web, headers, output_dir):
    res = requests.get(web,headers=headers)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    #debug
    #with open(debug_html_ch, 'w', encoding='utf8') as f:
    #    f.write(str(soup))
    # Tìm thẻ h1 có class
    h1_tag = soup.find("h1", class_="name font-15x mb-3 pt-3 text-center")

    # Trích xuất văn bản từ thẻ h1
    if h1_tag:
        h1_text = h1_tag.text.strip()
        print(h1_text)
    img_links = []
    for x in soup.find_all("div", class_="content-text"):#, id="image"):
        for y in x.find_all("img"):
            img_links.append(y.get("src"))
    #debug
    print(img_links)
    #parts = web.split("/")
    #title_tag = soup.find('title')
    #title = title_tag.string.replace(":"," -")
    #title = web.split("/")[-1]
    if output_dir == '':
        folder = join(sys.path[0],"downloads",h1_text)
    else:
        folder = join(output_dir,h1_text)
    makedirs(folder, exist_ok=True)
    for index, link in enumerate(img_links):
        print(link)
        file = join(folder,f"image_{index}.jpg")
        response = requests.get(link, headers=headers)
        with open(file, "wb") as f:
            f.write(response.content)
    time.sleep(1)
    print("Xong.")

 

def allchapters(web, headers, domain):
    while True:
        try:
            requests.get(web,headers=headers)
            break
        except requests.exceptions.SSLError:
            try:
                requests.get(f'https://webcache.googleusercontent.com/search?q=cache:{web}',headers=headers)
            except requests.exceptions.SSLError:
                print("Giải mã trang web bị lỗi. Đang cố gắng thử lại...")
    #html_content = res.text
    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import time

    # Khởi tạo trình duyệt
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    # Thêm 1 số option cho chrome như kích thước windows, chế độ ẩn danh, ...
    #options.add_argument('--disable-gpu')
    #options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--incognito")
    #options.add_argument("--window-size=1920x1080")
    chromedrv = join(sys.path[0], "chromedriver.exe")
    service = Service(executable_path=chromedrv)
    driver = webdriver.Chrome(service=service,options=options)
    # Mở trang web
    driver.get(web)
    time.sleep(10)
    # Scroll down to the bottom of the page
    while True:
        # Scroll down using the END key
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Add a delay to allow content to load (adjust as needed)
    # Check if we've reached the bottom of the page
        if driver.execute_script("return window.scrollY + window.innerHeight >= document.body.scrollHeight"):
            break

    # Get the HTML source of the entire page
    html_source = driver.page_source

    # Close the browser
    driver.quit()
    soup = BeautifulSoup(html_source, 'html.parser')

    #debug
    #with open(debug_html, 'w', encoding='utf8') as f:
    #    f.write(str(soup))
    # Find all <a> tags within the specified <div>
    links = []
    #for item in soup.find_all("div", class_="page-info"):
    #for item in soup.find_all("div", class_=lambda x: x and 'watch-online' in x):
    for item in soup.find_all("p", id="inner-listshowchapter"):
        for link in item.find_all("a"):
            links.append(link.get("href"))
    print(links)
    links.pop(1)
    #print(links)
    #title_tag = soup.find("title")
    #title = title_tag.string
    title = web.split("/")[-1]
    print(title)
    output_dir = join(sys.path[0],"downloads",title)
    for link in links:
        chap = f'{domain}{link}'
        print(chap)
        onechapter(chap, headers, output_dir)


web = str(input("Nhập đường link của truyện: "))
print("**!** Tool còn nhiều hạn chế, và mình sẽ luôn cố gắng cập nhật để bắt kịp với trang web.")
time.sleep(5)
print("Running...")
referer = f'https://{web.split("/")[2]}/'
domain = f'https://{web.split("/")[2]}'
print("Server:",referer)
headers = {
   'Connection': 'keep-alive',
   'Cache-Control': 'max-age=0',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': random.choice(user_agent_list),
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
   #'referer': random.choice(reffer_list)
   'referer': referer
    }
if "xem-truyen" in web:
    print("Có vẻ đây là link của 1 chap đơn. Tiến hành tải...")
    output_dir = ''
    onechapter(web, headers, output_dir)
else:
    print("Có vẻ như đây là đường link của cả một truyện. Tiến hành tải tất cả chương mà truyện hiện có...")
    allchapters(web, headers, domain)