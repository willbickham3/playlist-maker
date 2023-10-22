from pytube import YouTube
from moviepy.editor import *
import shutil

yt = YouTube('https://www.youtube.com/watch?v=vJpo5dW3Ze4')

print(yt.title)

#audio_files = yt.streams.filter(only_audio = True)
audio_files = yt.streams.filter(file_extension='mp4')
audio_files = audio_files
#print(audio_files)
abr_list = []
for x in audio_files:
    if x.abr == None:
        continue
    bitRate = x.abr

    bitRate = bitRate.split("kbps")
    bitRate = int(bitRate[0])
    abr_list.append(bitRate)
abr_list.sort(reverse=True)

# for x in audio_files:
#     highest_kbps = f"{abr_list[0]}kbps"
#     # print(f"{highest_kbps}kbps")
#     if x.abr == highest_kbps:
#         x.download("downloaded")

#file_to_download = audio_files.get_by_itag(140)
# class Song:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

song_1 = VideoFileClip("downloaded/WoW Synthwave Beats to Chill To  Journey to BlizzCon.mp4").subclip(0, 274)
song_1 = song_1.audio
output_file = "Orgrimmar.mp3"
song_1.write_audiofile(output_file)

song_2 = VideoFileClip("downloaded/WoW Synthwave Beats to Chill To  Journey to BlizzCon.mp4").subclip(273.3, 576)
song_2 = song_2.audio
song2 = "Thrall-Aggra.mp3"
song_2.write_audiofile(song2)

song_3 = VideoFileClip("downloaded/WoW Synthwave Beats to Chill To  Journey to BlizzCon.mp4").subclip(576.4, 942)
song_3 = song_3.audio
song3 = "Orc-2-Orc.mp3"
song_3.write_audiofile(song3)

song_4 = VideoFileClip("downloaded/WoW Synthwave Beats to Chill To  Journey to BlizzCon.mp4").subclip(943, 1201)
song_4 = song_4.audio
song4 = "The-Barrens.mp3"
song_4.write_audiofile(song4)

shutil.move('Orgrimmar.mp3', 'songs')
shutil.move('Thrall-Aggra.mp3', 'songs')
shutil.move('Orc-2-Orc.mp3', 'songs')
shutil.move('The-Barrens.mp3', 'songs')

#print(file_to_download)

#audio_files.stream.download('downloaded')

#file_to_download.download("downloaded")