import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def create_gui(playlist_dict, playlist_images, on_playlist_button_click):
    # Main window
    root = tk.Tk()
    root.title("Spotify Playlist Shuffler")

    # Selection of colors
    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    button_bg_color = "#3e3e3e"
    button_fg_color = "#ffffff"

    root.configure(bg=bg_color)

    # Create buttons with album covers in a grid
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
            button.image = img  # Keep a reference to avoid dogshit collection
            button.grid(row=row, column=col, padx=10, pady=10)

            col += 1
            if col == 3:
                col = 0
                row += 1

    # Run the Tkinter loop
    root.mainloop()