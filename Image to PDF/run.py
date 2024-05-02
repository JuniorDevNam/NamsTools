#https://datatofish.com/images-to-pdf-python/

from PIL import Image
import sys
from os.path import join
n = int(input("Number of Image(s): "))
i = str(input("Folder Contains Images: "))
name = str(input("Name of the PDF file (contains .pdf): "))
out = join(sys.path[0],"output",name)
image_list = []
dest = f'{i}001'
image_1 = Image.open(dest)
im_1 = image_1.convert('RGB')
for x in range(2,n+1):
    if x < 10:
        dest = f'{i}00{x}'
        image = Image.open(dest)
        img = image.convert('RGB')
        image_list.append(img)
    elif x >= 10 and x < 100:
        dest = f'{i}0{x}'
        image = Image.open(dest)
        img = image.convert('RGB')
        image_list.append(img)
im_1.save(out, save_all=True, append_images=image_list)