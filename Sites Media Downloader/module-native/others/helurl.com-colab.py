import sys
import json
import requests
from urllib.parse import urlparse as urlp

link = sys.argv[1]
name = sys.argv[2]
custom_name = sys.agrv[3]
vi_tri_luu = sys.agrv[4]

def helurldown(link, name, vi_tri_luu):
    if vi_tri_luu == "Google Drive":
        !wget -O "$name" -P /content/drive/MyDrive $link
    else:
        !wget -O "$name" $link

if (link.find("api") < 0):
    x = link.split("/")
    h = x[len(x)-1]
    url = 'https://helurl.com/api/v1/shareable-links/'+ h + '?withEntries=true&page=1&order=updated_at:desc'
    x = requests.get(url)
    data = x.json()
    id = data['link']['id']
    hash = data['link']['entry']['hash']
    link = 'https://helurl.com/api/v1/file-entries/download/'+ hash +'?shareable_link=' + str(id) + '&password=null'#;
    print("Direct link: ",link)#;
elif name == "":
    print("The link you entered is Direct Link, requires preset name file")
    print("ERROR - You haven't specified file name")
    sys.exit(0)

if custom_name:
    helurldown(link, name, vi_tri_luu)
else:
    name = data['link']['entry']['name']
    helurldown(link, name, vi_tri_luu)

'''
    
else:
    if custom_name:
        helurldown(link, name, custom_name, vi_tri_luu)
    else:
        name = input('Link bạn nhập là link trực tiếp từ helurl, nhập tên file bạn muốn lưu: ')
        helurldown(link, name, custom_name, vi_tri_luu)
        '''