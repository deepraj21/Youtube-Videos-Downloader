from tkinter import *
from pytube import YouTube


def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        title = yt.title
        title_label.config(text="Video Title: " + title)
        download_label.config(text="Downloading...")
        yt.streams.first().download()
        download_label.config(text="Download completed!!")
    except Exception as e:
        download_label.config(text="Error: " + str(e))


# create the main window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

# create the label and entry widgets
url_label = Label(root, text="Enter YouTube Video Link:")
url_label.pack(pady=10)

url_entry = Entry(root, width=50)
url_entry.pack(pady=5)

title_label = Label(root, text="")
title_label.pack(pady=10)

download_button = Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

download_label = Label(root, text="")
download_label.pack()

# run the main loop
root.mainloop()
