import requests
from bs4 import BeautifulSoup

def save_html_element(url, element_id, file_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find(id=element_id)

    if element is not None:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(element))
    else:
        print(f"Không tìm thấy thành phần có id '{element_id}' trên trang web.")

# Sử dụng chương trình
url = input("Nhập URL của trang web: ")
element_id = input("Nhập ID của thành phần bạn muốn sao chép: ")
file_path = input("Nhập đường dẫn tệp để lưu mã HTML: ")
save_html_element(url, element_id, file_path)

#------------------------------------------------------------------

def save_html_elements(url, tag_name, file_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(tag_name)

    if elements:
        with open(file_path, 'w', encoding='utf-8') as f:
            for element in elements:
                f.write(str(element))
                f.write('\n\n')
    else:
        print(f"Không tìm thấy thẻ '{tag_name}' trên trang web.")

# Sử dụng chương trình
url = input("Nhập URL của trang web: ")
tag_name = input("Nhập tên thẻ bạn muốn sao chép: ")
file_path = input("Nhập đường dẫn tệp để lưu mã HTML: ")
save_html_elements(url, tag_name, file_path)

