import requests

def connect():
    r=requests.get('https://www.google.com.tw/')
    if(r.status_code!=200):
        return False
    else: 
        return True