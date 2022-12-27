import youtube_dl

# Prompt the user for a YouTube link
link = input("Enter the YouTube link: ")

# Set the options for the audio file
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

# Download the audio file
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("MP3 download complete!")
