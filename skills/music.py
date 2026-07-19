import os


def play_music():

    music_folder = r"C:\Users\HP\Music"

    if os.path.exists(music_folder):
        os.startfile(music_folder)
        return True

    return False