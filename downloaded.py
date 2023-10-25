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

for x in audio_files:
    highest_kbps = f"{abr_list[0]}kbps"
    # print(f"{highest_kbps}kbps")
    if x.abr == highest_kbps:
        x.download("downloaded")