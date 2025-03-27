import tkinter as tk
from tkinter import filedialog
import libtorrent as lt
import time

def get_peers(torrent_path): 
    session = lt.session()
    info = lt.torrent_info(torrent_path) 
    handle = session.add_torrent({'ti': info, 'save_path': '.'})

    print("Haetaan ip osoitteita...\n") 
    time.sleep(5) # Allow time for peer discovery

    peers = handle.get_peer_info() 
    for peer in peers: 
        print(f"IP: {peer.ip}")

    session.remove_torrent(handle)

def on_button_click():
    torrent_file = filedialog.askopenfilename(filetypes=[("Torrent files", "*.torrent")])
    if torrent_file:
        get_peers(torrent_file)

# Create the main window
root = tk.Tk()
root.title("IP Imuttaja v.1.0")

# Create and place the button
button = tk.Button(root, text="Valitse torrent tiedosto ja imuta", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()