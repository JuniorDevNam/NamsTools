import requests
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import sys
import time
import random

#https://stackoverflow.com/questions/14587728/what-does-this-error-in-beautiful-soup-means
user_agent_list = [
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
   "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1",
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3",
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0"
]


def onechapter(web):
    output_dir = join(sys.path[0],"downloads")
    res = requests.get(web,verify=False)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.findAll('img',{"data-src":True})
    image_links = [img['data-src'] for img in img_tags]
    #['https:', '', 'evvdsfgefdszihfdx.hentaivn.lat', 'HGHrrFSDweqZSfd', 'lgbdfexijzbxsdrl', '2024', '01', '12', '1705045067-0.png?imgmax=1200']
    #https://i3.hhentai.net/images/5/6/7/8
    parts = web.split("/")
    print(parts[2],parts[3])
    #folder = f'{output_dir}\{parts[2]}\{parts[3]}'
    #makedirs(folder, exist_ok=True)
    for x in image_links:
        l = x.split("/")
        name = l[8].replace("?imgmax=1200","")
        #link = f'https://i3.hhentai.net/images/{l[5]}/{l[6]}/{l[7]}/{l[8]}'
        image_save_path = join(output_dir, name)
        print(x)
        print(image_save_path)
        res = requests.get(x,verify=False)
        with open(image_save_path, 'wb') as f:
            f.write(res.content)
 

def allchapters(web, headers):
    res = requests.get(web,headers=headers)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    #debug
    #with open(debug_html, 'w') as f:
    #    f.write(soup)
    # Find all <a> tags within the specified <div>
    links = []
    for item in soup.find_all("div", class_="page-info"):
        for link in item.find_all("a"):
            links.append(link.get("href"))
    print(links)


web = str(input("Nhập đường link của truyện: "))
print("**!** Tool còn nhiều hạn chế, và mình sẽ luôn cố gắng cập nhật để bắt kịp với trang web.")
time.sleep(5)
print("Running...")
referer = f'https://{web.split("/")[2]}/'
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
allchapters(web, headers)