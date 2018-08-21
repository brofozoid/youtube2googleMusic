import youtube_dl
import sys

youtube_url = sys.argv[1]
playlist = []

opts = {
    'format': 'bestaudio/best',
    'outtmpl': "%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

with youtube_dl.YoutubeDL(opts) as ydl:
    playlist_info = ydl.extract_info(youtube_url, download=False)
    # ydl.download([youtube_url])

if 'entries' in playlist_info:
    for vid in playlist_info['entries']:
        playlist.append(vid['title'])
    # video = playlist['entries'][0]
    playlist.append('FFXIV OST - Test')
else:
    # Just a video
    video = playlist_info

with open('new_playlist.txt', 'w') as file_out:
    for line in playlist:
        file_out.write(line + '\n')


with open('old_playlist.txt', 'r') as file1:
    with open('new_playlist.txt', 'r') as file2:
        diff = set(file2).difference(file1)
        diff.discard('\n')
        print(diff)

