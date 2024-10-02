import tkinter as tk
from gui import create_gui
from fetch_playlists import fetch_playlists
from shuffle_playlist import shuffle_playlist
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch playlists
playlist_dict, playlist_images = fetch_playlists()

def on_playlist_button_click(playlist_id, playlist_name):
    print(f"Playlist {playlist_name} with ID {playlist_id} clicked")
    shuffle_playlist(playlist_id)

# Create the GUI
create_gui(playlist_dict, playlist_images, on_playlist_button_click)