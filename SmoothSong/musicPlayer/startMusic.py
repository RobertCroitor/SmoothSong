import os

# CHANGE THE CURRENT DIRECTORY TO DOWNLOADS
resource_dir = os.path.join(os.path.dirname(__file__), 'downloads');


# STATS THE GIVEN SONG IN A 3RD PARTY APP
def startMusic(filename):
    os.startfile(os.path.join(resource_dir, filename))


def startFolder():
    os.startfile(resource_dir)
