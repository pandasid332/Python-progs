import pytube
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

def download():
    url = url_entry.get()
    try:
        yt = YouTube(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo('Downloaded', 'Video downloaded successfully')
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror('Error', 'Invalid URL')
    except pytube.exceptions.VideoUnavailable:
        messagebox.showerror('Error', 'Video is unavailable')
    except pytube.exceptions.LiveStreamError:
        messagebox.showerror('Error', 'Live stream is not supported')
    except pytube.exceptions.VideoPrivate:
        messagebox.showerror('Error', 'Video is private')
    except pytube.exceptions.VideoRegionBlocked:
        messagebox.showerror('Error', 'Video is blocked in your region')
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred: {e}')

# Main window
root = tk.Tk()
root.title('YouTube Video Downloader')

# Create and place the widgets
tk.Label(root, text='Enter URL:').pack(pady=10)
url_entry = tk.Entry(root, width=50)

url_entry.pack(pady=5)
download_button = tk.Button(root, text='Download', command=download)
download_button.pack(pady=20)

# Run the main loop
root.mainloop()