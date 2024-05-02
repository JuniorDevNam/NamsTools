import sys
from os import system as system
from urllib.parse import urlparse as urlp

link = sys.argv[1]
name = sys.argv[2]
custom_name = sys.argv[3]
no_check_certificate = sys.argv[4]

def directdown(link, name, no_check_certificate):
    if no_check_certificate:
      system(f'wget -O {name} {link} --no-check-certificate')
    else:
      system(f'wget -O {name} {link}')

if custom_name:
    directdown(link, name, no_check_certificate)
else:
    path = urlp(link).path.split('/')
    name = path[len(path)-1]
    name = name.replace("%20","_")
    name = name.replace("%28","(")
    name = name.replace("%29",")")
    directdown(link, name, no_check_certificate)