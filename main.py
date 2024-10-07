from bs4 import BeautifulSoup
from requests import get

URL = "https://www.billboard.com/charts/hot-100/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
response = get(url=URL, headers=headers)
response.raise_for_status()
html_page = response.text

soup = BeautifulSoup(markup=html_page, features='html.parser')
all_titles = soup.find_all(name='h3', class_='c-title')
song_titles = []
for title in all_titles[7:404:2]:
    title = title.get_text().replace('Producer(s):', '')
    song_titles.append(title.strip())
song_titles = song_titles[::2]
