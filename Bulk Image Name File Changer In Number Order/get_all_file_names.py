#@title Công cụ duyệt tên file và ghi tên file ra 1 file xuất dữ liệu
import os
import sys
#directory = str(input("Nhập đường dẫn thư mục cần duyệt: "))
imagespath = os.path.join(sys.path[0],"Images")
output_file = os.path.join(sys.path[0],"output_file_names.txt")
def write_file_names_to_txt(directory, output_file):
    with open(output_file, 'w') as f:
        for filename in os.listdir(directory):
            f.write(filename + '\n')


write_file_names_to_txt(imagespath, output_file)
