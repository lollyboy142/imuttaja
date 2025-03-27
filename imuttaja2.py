import requests
import bencodepy
import tkinter as tk
from tkinter import filedialog
import hashlib
import urllib.parse

def get_peers(torrent_path):
    try:
        # Parse the .torrent file
        with open(torrent_path, "rb") as f:
            torrent = bencodepy.decode(f.read())

        # Extract tracker URL and info hash
        tracker_url = torrent[b'announce'].decode()
        info_hash = hashlib.sha1(bencodepy.encode(torrent[b'info'])).digest()

        # Build the tracker request URL
        params = {
            "info_hash": info_hash,
            "peer_id": "-PC0001-123456789012",
            "port": 6881,
            "uploaded": 0,
            "downloaded": 0,
            "left": 0,
            "compact": 1,
        }
        url = f"{tracker_url}?{urllib.parse.urlencode(params)}"

        # Send the request to the tracker
        response = requests.get(url)
        if response.status_code == 200:
            print("Tracker response:", response.content)
        else:
            print(f"Tracker request failed with status code {response.status_code}")
    except Exception as e:
        print(f"Error fetching peers: {e}")

def on_button_click():
    torrent_file = filedialog.askopenfilename(filetypes=[("Torrent files", "*.torrent")])
    if torrent_file:
        get_peers(torrent_file)

# Create the main window
root = tk.Tk()
root.title("IP Imuttaja v.1.1")

# Create and place the button
button = tk.Button(root, text="Valitse torrent tiedosto ja imuta", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()