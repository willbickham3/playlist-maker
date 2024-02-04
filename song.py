from pytube import YouTube
from moviepy.editor import *
import shutil


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
            return f"{int(length / 60)} minutes and {length % 60} seconds"
        return f"{length} seconds"
    
    def create_song(self):
        """Creates a song based on the class parameters"""
        print("Please enter a name for your song/clip.")
        song = VideoFileClip(f"{self._file_name}").subclip(self._start, self._end)
        song = song.audio
        output_file = f"{self._song_name}.mp3"
        song.write_audiofile(output_file)
        shutil.move(output_file, "songs")
        return
    
    def create_clip(self):
        """Creates a video clip with audio"""
        clip = VideoFileClip(f"{self._file_name}").subclip(self._start, self._end)
        output_file = f"{self._song_name}.mp4"
        clip.write_videofile(output_file)
        shutil.move(output_file, "clips")
        return


if __name__ == "__main__":
    new_song = Song("downloaded/VØJ Narvent - Memory Reboot.mp4", "monk", 0, 60)
    new_song.create_clip()