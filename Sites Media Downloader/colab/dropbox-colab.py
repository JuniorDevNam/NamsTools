import sys
#from urllib.parse import urlparse as urlp

link = sys.argv[1]
name = sys.argv[2]
vi_tri_luu = sys.argv[3]

if name == "":
    print("ERROR - You haven't specified file name")
    sys.exit(0)

def dropdown(link, name, vi_tri_luu):
    if vi_tri_luu == "Google Drive":
      !wget -O "$name" -P /content/drive/MyDrive $link
    else:
      !wget -O "$name"  $link

link = link.replace("dl=0", "dl=1")
#path = urlp(link).path.split('/')
#name = path[len(path)-1]
#name = name.replace("%20","_")
#name = name.replace("%28","(")
#name = name.replace("%29",")")
dropdown(link, name, vi_tri_luu)