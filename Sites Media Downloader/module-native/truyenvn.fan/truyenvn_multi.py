import requests
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import sys

'''
web = sys.argv[1]
place = sys.argv[2]
from_chapter = sys.argv[3]
from_chapter = int(from_chapter)
to_chapter = sys.argv[4]
to_chapter = int(to_chapter)
special_chapter_suffixes = sys.argv[5]
special_chapter_suffixes = special_chapter_suffixes.split()
'''

#Update 15/5/24 để phù hợp với đổi mới của mã nguồn trang web

def onechapter(web, output_dir):
    res = requests.get(web)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    c = 0
    img_urls = []
    while True:
        specific_id = f'image-{c}'
        img_tag = soup.find('img', id=specific_id)
        if img_tag:
            img_url = img_tag['data-src']
            print(img_url)
            img_urls.append(img_url)
            c += 1
        else:
            print("Not Found Image URL with image ID",specific_id)
            break
    if img_urls == []:
        return "Link Not Available"
    parts = web.split("/")
    print(parts[4],parts[5])
    folder = f'{output_dir}\{parts[4]}\{parts[5]}'
    makedirs(folder, exist_ok=True)
    for x in img_urls:
        n = x.split("/")[-1]
        image_save_path = join(folder, n)
        print(image_save_path)
        res = requests.get(x)
        with open(image_save_path, 'wb') as f:
            f.write(res.content)


def multichapters(link, dir, from_chapter, latest_chapter, *special_chapters):
    a = []
    chapsuffix = link.split("/")[-2]
    print(chapsuffix)
    for c in range(from_chapter,latest_chapter+1):
        chapterlink = f'{link}{chapsuffix}-chapter-{c}'
        print(chapterlink)
        onechapter(chapterlink,dir)
        if special_chapters != a:
            for x in special_chapters:
                specialchapterlink = f'{link}{chapsuffix}-chapter-{c}-{x}'
                print(specialchapterlink)
                onechapter(specialchapterlink,dir)
        

#multichapters(web,place,from_chapter,to_chapter,special_chapter_suffixes)

multichapters("https://truyenvn.lol/truyen-tranh/dong-ho-ngung-dong-thoi-gian/","\downloads",26,46,0)

#multichapters("https://truyenvn.lol/truyen-tranh/phan-boi-loai-nguoi-de-chich-gai/","\downloads",1,42)
