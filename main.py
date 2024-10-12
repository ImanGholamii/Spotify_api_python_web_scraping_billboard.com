from datetime import datetime

from bs4 import BeautifulSoup
from decouple import config
from requests import get
from spotipy import client
from spotipy.oauth2 import SpotifyOAuth

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
songs_title = [title.strip() for title in titles]

songs_title = songs_title[::2]


# ------------------------------ spotify ------------------------------
# ---------- CREATE PLAY LIST
def set_scope(scope: str):
    return scope


# ---------- CREATE PLAY LIST
# scope = 'playlist-modify-private'  # STEP 1 to make a private playlist
# scope = 'playlist-read-private'  # STEP 2 to read the private playlists

def spotify(scope: str):
    return client.Spotify(
        requests_timeout=20,
        retries=2,
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri='https://example.com',
        ),
    )


# --------- GET USER INFO
user_info = spotify(scope='playlist-modify-private').current_user()
username = user_info['display_name']
user_id = user_info['id']


# ---------- CREATE NEW PRIVATE PLAYLIST
def create_playlist():
    spotify(scope='playlist-modify-private').user_playlist_create(
        user=user_id,
        name='PyPlaylist',
        public=False,
        collaborative=False,
        description='First Private playlist made by webapi'
    )


create_playlist()  # STEP 1 to make a private playlist
# ---------- GET CURRENT USER'S PLAYLISTS
playlists = spotify(scope='playlist-read-private').current_user_playlists()
playlists_id = [(item['name'], item['id']) for item in playlists['items']]
private_playlist_id = playlists_id[0][1]


# ---------- SEARCH USER'S SONGS TITLES
def get_uris(sound_tracks):
    uris = []
    for track in sound_tracks:
        sound_track_data = spotify(scope='playlist-modify-private').search(q=f'track:{track}', type='track', limit=1)
        items = sound_track_data['tracks']['items']
        if items:
            uri = items[0]['uri']
            uris.append(uri)
        else:
            print(f"No results found for track: {track}")
    return uris


uris_list = get_uris(sound_tracks=songs_title)

# ---------- ADD USER'S SONGS TO PLAYLIST

spotify(scope='playlist-modify-private').playlist_add_items(playlist_id=private_playlist_id, items=uris_list,
                                                            position=0)
