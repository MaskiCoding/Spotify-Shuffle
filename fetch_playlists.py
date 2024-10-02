import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

def fetch_playlists():
    # Yoink user credentials from the .env file
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")

    scope = "playlist-modify-public playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

    # Used to fetch user playlist
    playlists = sp.current_user_playlists()
    playlist_dict = {playlist['name']: playlist['id'] for playlist in playlists['items']}
    playlist_images = {playlist['id']: playlist['images'][0]['url'] for playlist in playlists['items'] if playlist['images']}

    return playlist_dict, playlist_images