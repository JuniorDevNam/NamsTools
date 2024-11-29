import sys
from os.path import join
result = join(sys.path[0], 'output.txt')
numimg = int(input("Số ảnh lần lượt: "))
pictureformat = str(input("Định dạng của tất cả ảnh sẽ dùng (Cần phải giống nhau): "))
#steps = 1
prelink = input("Nhập tiền tố đường dẫn nếu có: ")
with open(result, 'w') as file:
    pass
for x in range(numimg+1):
    img = f'<img src="{prelink}image_{x}.{pictureformat}">\n'
    with open(result, 'a') as i:
        i.write(str(img))
    #steps += 1