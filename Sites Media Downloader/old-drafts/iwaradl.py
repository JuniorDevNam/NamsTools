import requests, os, sys
import json
import urllib
from urllib.parse import urlparse
import http.client


#USERNAME = sys.argv[1]
#PASSWORD = sys.argv[2]
PATH = sys.argv[2]
id = sys.argv[1]
Proxy = sys.argv[3]
Token = ""
Authorization = ""
#Get the video info json from the API server
def GetVidInfo(id):
    u = f"https://api.iwara.tv/video/{id}"
    print("Requesting for JSON...")
    try:
        datajs = requests.get('https://example.com')
        datajs.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
        sys.exit(0)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        sys.exit(0)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        sys.exit(0)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong", err)
        sys.exit(0)
    try:
        datapy = json.loads(datajs)
    except json.JSONDecodeError as jserr:
        print("JSON Not Valid", jserr)
    
    print("Requesting for JSON... Done.")
    return datapy

def GetRequest(u, ver, Proxy):
    print("Checking and Setting up Proxy...")
    try:
        url = urlparse(Proxy)
        if url.scheme in ['http', 'https']:
            proxy_handler = urllib.request.ProxyHandler({url.scheme: Proxy})
            #opener = urllib.request.build_opener(proxy_handler)
            #urllib.request.install_opener(opener)
        else:
            raise ValueError("proxy URL scheme error")
    except Exception as e:
        print("Error setting up proxy:", e)

    # Tạo một session mới
    s = requests.Session()

    # Thiết lập thời gian chờ tối đa là 6 giây
    s.timeout = 6

    # Thiết lập proxy cho session (nếu có)
    s.proxies = proxy_handler
    
    #Tạo 1 yêu cầu HTTP GET mới tới u
    try:
        req = requests.get(u)
    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return None

    #Check Token và Authorization:
    if Authorization != "" and Token == "":
        Token = 

