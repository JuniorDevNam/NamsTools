import sys
from os.path import join
input_file = join(sys.path[0], "input.txt")
output_file = join(sys.path[0], "output.txt")
with open(input_file,'r',encoding="utf-8") as i:
    paras = i.readlines()
print(" ")  
print("Hãy đảm bảo rằng đã đưa dữ liệu đầu vào ở file input.txt")
print(" ")
print("********************")
print(" ")
checknote = str(input("Có note không? (yes/no): "))
if checknote == "yes" or checknote == "y" or checknote == "ýe":
    notes = str(input("Liệt kê các dòng cần note (ngăn cách bởi dấu phẩy, viết liền): "))
    listnote = list(map(int, notes.split(",")))
l = 1
for t in range(len(paras)):
    if l in listnote:
        print(f'Đã đến dòng chứa note (dòng {l}).')
        notenum = int(input("Ghi tên note: "))
        notetext = str(input("Nội dung note: "))
        html = f'<p id="{t}">{paras[t]}<span id="anchor-note{notenum}" class="tooltip note1"><img src="https://lh3.googleusercontent.com/drive-viewer/AITFw-xyuuPf49I2OFom2c6CIbz141FBPVeMYdXXuHBxXSbMG1QimWwH6hRod5vafbrjzRALb8rIhpUrVmEK6j5XbdYhszKLKA=s1600" title="note{notenum}"><a href="#note{notenum}" title="Xuống dưới">.</a><span class="toolttext">{notetext}</span></span></p>\n'
        with open(output_file,'a',encoding="utf-8") as o:
            o.write(str(html))
    else:
        html = f'<p id="{t}">{paras[t]}</p>\n'
        with open(output_file,'a',encoding="utf-8") as o:
            o.write(str(html))
    l = l + 1

    
