#Made by Nam (GitHub @IAmNamNguyen)
#Được tạo bởi Nam

#*******************************************************

#Mục đích / Purpose:
'''
Nhập các đường liên kết trực tiếp của những bức ảnh ở file input, công cụ
sẽ chuyển đổi những đường liên kết ảnh đó sang dạng những thẻ <img> trong mã HTML
ở file output, phục vụ cho việc tạo trang web thư viện ảnh hoặc truyện tranh đơn giản.

Import direct links of images in input files, tools
will convert those image links to <img> tags in HTML
in the output file, serving to create a simple photo gallery or comic website.
'''
#********************************************************
import sys
from os.path import join
input_file = join(sys.path[0], "input.txt")
output_file = join(sys.path[0], "output.txt")
with open(input_file,'r',encoding="utf-8") as i:
    images = i.readlines()
print(" ")  
print("Hãy đảm bảo rằng đã đưa dữ liệu đầu vào ở file input.txt")
print(" ")
print("********************")
print(" ")

params = str(input("Các cú pháp phụ cho thẻ img (title, alt, style)? - Yes/No: "))
if params == "Y" or "y" or "yes" or "Yes":
    print(f"Nếu không muốn cú pháp đó, hãy gõ \"N/A\"")
    title = str(input("title?: "))
    alt = str(input("alt?: "))
    style = str(input("style?: "))
else:
    for t in range(len(images)):
        html = f'<img src={images[t]} id="{t}"/>\n'
        with open(output_file,'a',encoding="utf-8") as o:
            o.write(str(html))
    sys.exit()


for t in range(len(images)):
    html = [f"<img src=\"{images[t]}\"",f"title=\"{title}\"",f"alt=\"{alt}\"",f"style=\"{style}\"",f"id=\"{t}\"","/>"]

    if title == "N/A":
        del html[1]
    if alt == "N/A":
        if title == "N/A":
            del html[1]
        else:
            del html[2]
    if style == "N/A":
        if title == "N/A" and alt == "N/A":
            del html[1]
        elif title == "N/A" and alt != "N/A":
            del html [2]
        elif alt == "N/A" and title != "N/A":
            del html[2]
        else:
            del html[3]
    
    merged_html = ''.join(html) + '\n'
    with open(output_file,'a',encoding="utf-8") as o:
        o.write(str(merged_html))