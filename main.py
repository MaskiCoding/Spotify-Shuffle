import tkinter as tk
from gui import create_gui
from fetch_playlists import fetch_playlists

# Fetch playlists
playlist_dict, playlist_images = fetch_playlists()

def on_playlist_button_click(playlist_id, playlist_name):
    print(f"Playlist {playlist_name} with ID {playlist_id} clicked")

# Create the GUI
create_gui(playlist_dict, playlist_images, on_playlist_button_click)