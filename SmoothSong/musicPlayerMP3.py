import time
import vlc


def playMp3():
    p = vlc.MediaPlayer("./songs/Test Song.mp4")
    p.play()
    time.sleep(60)
