import sys
from os.path import join
result = join(sys.path[0], 'output.txt')
numimg = int(input("Số ảnh lần lượt: "))
pictureformat = str(input("Định dạng của tất cả ảnh sẽ dùng (Cần phải giống nhau): "))
steps = 1
for x in range(numimg):
    img = f'<img src="{steps}.{pictureformat}">\n'
    with open(result, 'a') as i:
        i.write(str(img))
    steps += 1