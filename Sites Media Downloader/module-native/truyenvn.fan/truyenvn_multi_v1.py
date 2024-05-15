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

#If this not work, consider using v2

def onechapter(web, output_dir):
    res = requests.get(web)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    #print(img_tags)
    parts = web.split("/")
    print(parts[4],parts[5])
    folder = f'{output_dir}\{parts[4]}\{parts[5]}'
    makedirs(folder, exist_ok=True)
    for x in range(1,len(img_tags)+1):
        if 1 <= x <= 9:
            downlink = f'https://img.imgxyzz.xyz/{parts[4]}/{parts[5]}/00{x}.jpg'
        elif x > 9:
            downlink = f'https://img.imgxyzz.xyz/{parts[4]}/{parts[5]}/0{x}.jpg'
        print(downlink)
        image_save_path = join(folder, f'0{x}.jpg')
        res = requests.get(downlink)
        with open(image_save_path, 'wb') as f:
            f.write(res.content)
    '''
    res = requests.get(web)
    html_content = res.text
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_links = [img['data-src'] for img in img_tags]
    for i, link in enumerate(image_links):
        image_save_path = join(output_dir, f'image_{i}.jpg')
        res = requests.get(link)
        with open(image_save_path, 'wb') as f:
            f.write(res.content)
    '''

def multichapters(link, dir, from_chapter, latest_chapter, *special_chapters):
    print("Generating Chapters List Links...")
    listchaps = []
    for c in range(from_chapter,latest_chapter+1):
        chapterlink = f'{link}chapter-{c}'
        lnktest = f'{chapterlink}/001.jpg'
        print(f"Testing: {lnktest}")
        chlnktest = requests.get(lnktest)
        #if chlnktest.status_code != 404:
        if chlnktest.ok:
            print("OK!")
            listchaps.append(chapterlink)
        else:
            print("Not Available.")
        a = []
        if special_chapters != a:
            for x in special_chapters:
                #c = c + x
                specialchapterlink = f'{link}chapter-{c}-{x}'
                test = f'{specialchapterlink}/001.jpg'
                print(f"Testing: {test}")
                resp = requests.get(test)
                #if resp.status_code != 404:
                if resp.ok:
                    print("OK!")
                #c = c - x
                    listchaps.append(specialchapterlink)
                else:
                    print("Not Available.")
    for x in listchaps:
        onechapter(x, dir)

#multichapters(web,place,from_chapter,to_chapter,special_chapter_suffixes)

multichapters("https://truyenvn.lol/truyen-tranh/dong-ho-ngung-dong-thoi-gian/","\downloads",26,90,0)