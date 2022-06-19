import os

resource_dir = os.path.join(os.path.dirname(__file__), 'downloads');


def startMusic(filename):
    name = "It's my life-Bon Jovi.mp4"
    os.startfile(os.path.join(resource_dir, name))
