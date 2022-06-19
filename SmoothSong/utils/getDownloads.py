import os


def getFolderContent():
    content = os.listdir(os.getcwd() + "\musicPlayer\downloads")  # returns list
    return content
