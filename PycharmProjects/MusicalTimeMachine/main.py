from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

CLIENT_ID = "ab7e67157f9d497fb3ce2642fd69f760"
CLIENT_SECRET = "535d9b68facc4d70ba03600823b604b3"
SONG_LIST_URL = "https://www.billboard.com/charts/hot-100/1980-08-01"
DISPLAY_NAME = "Yoga with Amit and Shivangi"
# import lxml
# choice = input("Where would you like to travel to? Type the date in the format YYYY-MM-DD:")
#

# auth_manager = SpotifyClientCredentials(client_secret=CLIENT_SECRET,client_id=CLIENT_ID)
# sp = spotipy.Spotify(auth_manager=auth_manager)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SONG_LIST_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=DISPLAY_NAME,
    )
)
# Get user ID
user_id = sp.current_user()["id"]


# print(user_id)
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# song_names = ["The list of song", "titles from your", "web scrape"]
response = requests.get(SONG_LIST_URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# # print(soup.prettify())
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# playlists = sp.user_playlists('spotify')

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
