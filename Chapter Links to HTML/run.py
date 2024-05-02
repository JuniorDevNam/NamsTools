import sys
from os.path import join
input_file_1 = join(sys.join[0],"chapter_titles.txt")
input_file_2 = join(sys.join[0],"chapter_links.txt")
with open(input_file_1, 'r', encoding = "utf-8") as i1:
  chapter_titles = i1.readlines()
with open(input_file_2, 'r', encoding = "utf-8") as i2:
  chapter_links = i2.readlines()
print("    ")
print("Đảm bảo đã nhập các dữ liệu cần thiết vào các file input / Make sure to import all necessary datas to the input files.")
print("    ")
