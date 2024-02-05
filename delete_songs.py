import os

directory_path = 'songs'

def delete_songs():
    for files in os.listdir(directory_path):
        file_path = os.path.join(directory_path, files)
        if os.path.isfile(file_path):
            os.remove(file_path)