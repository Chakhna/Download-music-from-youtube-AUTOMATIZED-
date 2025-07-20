import yt_dlp

LINKS_FILE = "playlistlink.txt"

def load_links(filepath):
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Choose your preferred audio codec and quality here:
# For MP3:
audio_postprocessor = {
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '320',  
}

# Or for M4A (generally better quality and smaller files):
# audio_postprocessor = {
#     'key': 'FFmpegExtractAudio',
#     'preferredcodec': 'm4a',
#     'preferredquality': '192', # you can set 320 for max quality
# }

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    'postprocessors': [audio_postprocessor],
    #'cookiefile': 'youtube_cookies.txt', #provide cookies only if you are downloading from age restricted video
    'quiet': False
}

def download_all(links):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in links:
            try:
                print(f"\n▶ Downloading: {url}")
                ydl.download([url])
            except Exception as e:
                print(f"❌ Failed to download {url}: {e}")

if __name__ == "__main__":
    links = load_links(LINKS_FILE)
    if not links:
        print("⚠ No valid links found in provided txt file.")
    else:
        download_all(links)
