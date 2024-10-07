from datetime import datetime

from bs4 import BeautifulSoup
from requests import get


def validate_date_format(date_string, format):
    try:
        date_parts = date_string.split('-')
        year, month, day = date_parts[0], date_parts[1], date_parts[2]
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            datetime.strptime(date_string, format)
            return True
    except ValueError:
        return False


needs_to_try = True
while needs_to_try:
    date_string = input("Which date do you want to travel? type date in YYYY-MM-DD format:")
    if validate_date_format(date_string, "%Y-%m-%d"):
        needs_to_try = False
    else:
        needs_to_try = True

URL = "https://www.billboard.com/charts/hot-100/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
}
response = get(url=URL, headers=headers)
response.raise_for_status()
html_page = response.text

soup = BeautifulSoup(markup=html_page, features='html.parser')
all_titles = soup.find_all(name='h3', class_='c-title')
titles = [title.getText().replace('Producer(s):', '') for title in all_titles[7:404:2]]
song_titles = [title.strip() for title in titles]

song_titles = song_titles[::2]
