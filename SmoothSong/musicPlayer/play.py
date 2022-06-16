import time
import vlc
import youtube_dl


def run():
    video_url = "https://www.youtube.com/watch?v=xMvQg9kJtoY&ab_channel=RelaxChilloutMusic"
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = "song.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


def playSong():
    p = vlc.MediaPlayer("music.mp3")
    p.play()
    x = input("Smth : ")
    if x == "stop":
        p.stop()
    time.sleep(100)
