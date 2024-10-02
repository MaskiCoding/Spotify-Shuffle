from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def shuffle_playlist(playlist_id, playlist_name):
    playlist = sp.playlist(playlist_id)

    # Fetch the tracks from the playlist
    tracks = playlist['tracks']['items']

    # Extract track URIs
    track_uris = [track['track']['uri'] for track in tracks]

    # Shuffle the tracks
    random.shuffle(track_uris)

    # Replace the playlist items with the shuffled tracks
    sp.playlist_replace_items(playlist_id, track_uris)

    # Show confirmation
    messagebox.showinfo("Success", f"{playlist_name} has been shuffled.")

def on_playlist_button_click(playlist_id, playlist_name):
    shuffle_playlist(playlist_id, playlist_name)

# Load environment variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

scope = "playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Fetch user's playlists
playlists = sp.current_user_playlists()
playlist_dict = {playlist['name']: playlist['id'] for playlist in playlists['items']}
playlist_images = {playlist['id']: playlist['images'][0]['url'] for playlist in playlists['items'] if playlist['images']}

# Create the main window
root = tk.Tk()
root.title("Spotify Playlist Shuffler")

# Set dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
button_bg_color = "#3e3e3e"
button_fg_color = "#ffffff"

root.configure(bg=bg_color)

# Create buttons with album covers in a 3x3 grid
row = 0
col = 0
for playlist_name, playlist_id in playlist_dict.items():
    if playlist_id in playlist_images:
        response = requests.get(playlist_images[playlist_id])
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        button = tk.Button(root, image=img, command=lambda pid=playlist_id, pname=playlist_name: on_playlist_button_click(pid, pname), bg=button_bg_color, fg=button_fg_color)
        button.image = img  # Keep a reference to avoid garbage collection
        button.grid(row=row, column=col, padx=10, pady=10)

        col += 1
        if col == 3:
            col = 0
            row += 1

# Run the Tkinter event loop
root.mainloop()
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def shuffle_playlist(playlist_id, playlist_name):
    playlist = sp.playlist(playlist_id)

    # Fetch the tracks from the playlist
    tracks = playlist['tracks']['items']

    # Extract track URIs
    track_uris = [track['track']['uri'] for track in tracks]

    # Shuffle the tracks
    random.shuffle(track_uris)

    # Replace the playlist items with the shuffled tracks
    sp.playlist_replace_items(playlist_id, track_uris)

    # Show confirmation
    messagebox.showinfo("Success", f"{playlist_name} has been shuffled.")

def on_playlist_button_click(playlist_id, playlist_name):
    shuffle_playlist(playlist_id, playlist_name)

# Load environment variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

scope = "playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Fetch user's playlists
playlists = sp.current_user_playlists()
playlist_dict = {playlist['name']: playlist['id'] for playlist in playlists['items']}
playlist_images = {playlist['id']: playlist['images'][0]['url'] for playlist in playlists['items'] if playlist['images']}

# Create the main window
root = tk.Tk()
root.title("Spotify Playlist Shuffler")

# Set dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
button_bg_color = "#3e3e3e"
button_fg_color = "#ffffff"

root.configure(bg=bg_color)

# Create buttons with album covers in a 3x3 grid
row = 0
col = 0
for playlist_name, playlist_id in playlist_dict.items():
    if playlist_id in playlist_images:
        response = requests.get(playlist_images[playlist_id])
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        button = tk.Button(root, image=img, command=lambda pid=playlist_id, pname=playlist_name: on_playlist_button_click(pid, pname), bg=button_bg_color, fg=button_fg_color)
        button.image = img  # Keep a reference to avoid garbage collection
        button.grid(row=row, column=col, padx=10, pady=10)

        col += 1
        if col == 3:
            col = 0
            row += 1

# Run the Tkinter event loop
root.mainloop()