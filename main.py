from requests import get
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
response = get(url=URL, headers=headers)
response.raise_for_status()
html_page = response.text
