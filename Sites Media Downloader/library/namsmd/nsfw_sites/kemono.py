import requests
from bs4 import BeautifulSoup
from os.path import join
#, exists
from pathlib import Path
#from os import makedirs
import sys
#import urllib
#https://stackoverflow.com/questions/14587728/what-does-this-error-in-beautiful-soup-means


def down(url):

    # Gửi yêu cầu HTTP đến trang web
    response = requests.get(url)
    fol = url.split("/")
    # Phân tích cú pháp HTML từ trang web
    soup = BeautifulSoup(response.text, 'html.parser')
    # Tìm tất cả các thẻ <a> trong HTML, lấy thuộc tính href (URL của liên kết)
    links = [a['href'] for a in soup.find_all('a',class_='post__attachment-link')]
    print(links)

    # Tải và lưu tất cả các liên kết
    for link in links:
        # Kiểm tra xem liên kết có phải là một tệp tin không
        if '.' in link:
            # Tải tệp tin
            response = requests.get(link, stream=True)
            # Lưu tệp tin
            l = link.split('/')
            print(l)
            file = l[-1].split('?f=')[-1]
            print(file)
            #down_dir = join(sys.path[0],"downloads")
            down_dir = Path(sys.path[0]) / "downloads"
            #if not exists(down_dir):
                #makedirs(down_dir)
            output_dir = join(down_dir,file)
            with open(output_dir, 'wb') as out_file:
                out_file.write(response.content)
            print(f"Đã tải {link}")
