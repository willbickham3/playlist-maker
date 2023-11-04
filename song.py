from pytube import YouTube
from moviepy.editor import *
import shutil

def create_song(input_path, start, end):
    print("Please enter a name for your song/clip.")
    name = str(input())
    song = VideoFileClip(f"{input_path}").subclip(start, end)
    song = song.audio
    output_file = f"{name}.mp3"
    song.write_audiofile(output_file)
    shutil.move(output_file, "songs")