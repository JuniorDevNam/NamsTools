import sys, os, random, requests, re
from bs4 import BeautifulSoup
user_agent_list = [
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
   "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1",
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3",
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0"
]
referer = 'https://https://vatlyhadong.vn/'
headers = {
   'Connection': 'keep-alive',
   'Cache-Control': 'max-age=0',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': random.choice(user_agent_list),
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
   'referer': referer
    }

def run(web):
    protected_url = web
    response = session.get(protected_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('div', class_='plyr__video-wrapper plyr__video-embed').text
    video_id = re.search(r"embed/([a-zA-Z0-9_-]+)", data).group(1)
    link = f'https://youtube.com/watch?={video_id}'
    return link
def scraping(web):
    session = requests.Session()
    login_url = 'https://vatlyhadong.vn/dang-nhap'
    login_data = {
        'username': 'your_username',
        'password': 'your_password'
    }
    session.post(login_url, data=login_data)
web = str(input('link: '))