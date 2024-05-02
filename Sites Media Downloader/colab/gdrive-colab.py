import sys
from os import system as system
link = sys.argv[1]
name = sys.argv[2]
#vi_tri_luu = sys.argv[3]

if name == "":
    print("ERROR - You haven't specified file name")
    sys.exit(0)

FILEID = f'https://docs.google.com/uc?export=download&id={link}'
FILENAME = name

a = ' --load-cookies /tmp/cookies.txt'
b = f' \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate {FILEID}'
c = f' -O- | sed -rn \'s/.*confirm=([0-9A-Za-z_]+).*/\1\n/p\')&id={link}\"'
d = f' -O {FILENAME} && rm -rf /tmp/cookies.txt'
e = ' -P /content/drive/MyDrive'
system(f'wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate {FILEID} -O- | sed -rn \'s/.*confirm=([0-9A-Za-z_]+).*/\1\n/p\')&id={link}" -O {FILENAME} && rm -rf /tmp/cookies.txt')

#if vi_tri_luu == "Google Drive":
    #!wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "$FILEID" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$link" -O "$FILENAME" && rm -rf /tmp/cookies.txt -P /content/drive/MyDrive
#else:
    #!wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=FILEID" -O FILENAME && rm -rf /tmp/cookies.txt
    #!wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "$FILEID" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$link" -O "$FILENAME" && rm -rf /tmp/cookies.txt