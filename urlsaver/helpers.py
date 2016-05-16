import requests
from bs4 import BeautifulSoup

from urllib.parse import urlparse

# Googlebot user-agent string
user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

def add_scheme(url):
    if urlparse(url).scheme:
        return url
    return "http://" + url

def url_exists(url):
    try:
        r = requests.head(add_scheme(url),
                          headers={'user-agent': user_agent}, verify=False)
        return r.status_code # requests.codes.ok == 200
    except:
        return False

def get_title(url):
    r = requests.get(add_scheme(url),
                     headers={'user-agent': user_agent}, verify=False)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.title.text
