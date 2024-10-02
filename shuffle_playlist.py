import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def shuffle_playlist(playlist_id):
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")

    if not client_id or not client_secret or not redirect_uri:
        raise ValueError("Missing Spotify API credentials")

    scope = "playlist-modify-public playlist-modify-private"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

    # Get the tracks in the playlist
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    # Extract track URIs
    track_uris = [track['track']['uri'] for track in tracks]

    # Shuffle the track URIs
    random.shuffle(track_uris)

    # Clear the playlist
    sp.playlist_replace_items(playlist_id, [])

    # Add the shuffled tracks back to the playlist
    sp.playlist_add_items(playlist_id, track_uris)

    print(f"Playlist {playlist_id} shuffled")