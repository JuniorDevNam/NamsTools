import sys
import os
import requests
from bs4 import BeautifulSoup

def download_images(url, save_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, img in enumerate(img_tags, start=1):
        img_url = img.get('src')
        if img_url is not None:
            if 'http' not in img_url:
                # sometimes an image source can be relative 
                # if it is provide the base url which also happens 
                # to be the site variable atm. 
                img_url = '{}{}'.format(url, img_url)
            response = requests.get(img_url)
            with open(os.path.join(save_dir, '{:04d}.jpg'.format(i)), 'wb') as f:
                f.write(response.content)

# Sử dụng chương trình
url = input("Nhập URL của trang web: ")
save_dir = f"{os.path.join(sys.path[0])}/Downloaded Images/"
download_images(url, save_dir)