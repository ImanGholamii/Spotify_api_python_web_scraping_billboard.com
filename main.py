from datetime import datetime

from bs4 import BeautifulSoup
from decouple import config
from requests import get

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')


def validate_date_format(date_string, format_):
    try:
        date_parts = date_string.split('-')
        year, month, day = date_parts[0], date_parts[1], date_parts[2]
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            datetime.strptime(date_string, format_)
            return True
    except ValueError:
        return False


needs_to_try = True
while needs_to_try:
    date = input("Which date do you want to travel? type date in YYYY-MM-DD format:")
    if validate_date_format(date_string=date, format_="%Y-%m-%d"):
        needs_to_try = False
    else:
        needs_to_try = True
# ------------------------------ billboard ------------------------------
URL = "https://www.billboard.com/charts/hot-100/" + date
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

response = get(url=URL, headers=headers)
response.raise_for_status()
html_page = response.text

soup = BeautifulSoup(markup=html_page, features='html.parser')
all_titles = soup.find_all(name='h3', class_='c-title')
titles = [title.getText().replace('Producer(s):', '') for title in all_titles[7:404:2]]
song_titles = [title.strip() for title in titles]

song_titles = song_titles[::2]
# print(song_titles)
# ------------------------------ spotify ------------------------------
# ---------- CREATE PLAY LIST
endpoint = "https://api.spotify.com/v1/users/{user_id}/playlists"

