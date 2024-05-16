import requests
web = "https://nettruyencc.com/truyen-tranh/blue-archive-global/chapter-1/1"
print(web.split("/"))
reffer_list=[
   'https://nettruyenco.vn/',
   'https://nettruyencc.com/'
]
print(f'https://{web.split("/")[2]}')
print(reffer_list[1])
print(reffer_list[1]==f'https://{web.split("/")[2]}')