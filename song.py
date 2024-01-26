from pytube import YouTube
from moviepy.editor import *
import shutil

def create_song(input_path, name, start, end):
    print("Please enter a name for your song/clip.")
    song = VideoFileClip(f"{input_path}").subclip(start, end)
    song = song.audio
    output_file = f"{name}.mp3"
    song.write_audiofile(output_file)
    shutil.move(output_file, "songs")

class Song:
    """Instantiates a song object that can be called to retrieve a song's name or create a song"""
    def __init__(self, file_name, song_name, start, end):
        self._file_name = file_name
        self._song_name = song_name
        self._start = start
        self._end = end
    
    def get_song_length(self):
        """Returns length of song"""
        length = self._end - self._start
        if length / 60 >= 1:
            return "longer than a minute"
        return f"{length} seconds"
    
    def create_song(self):
        """Creates a song based on the class parameters"""
        print("Please enter a name for your song/clip.")
        song = VideoFileClip(f"{self._file_name}").subclip(self._start, self._end)
        song = song.audio
        output_file = f"{self._song_name}.mp3"
        song.write_audiofile(output_file)
        shutil.move(output_file, "songs")


if __name__ == "__main__":
    new_song = Song("downloaded/Chill Monkey listening to the Deep Stone Lullaby.mp4", "monk", 0, 20)
    print(new_song.get_song_length())