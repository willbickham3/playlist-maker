from pytube import YouTube
import shutil

def download_video(url):
    """Takes in a url in string form and downloads the highest quality sound from the video"""
    yt = YouTube(url)
    audio_files = yt.streams.filter(file_extension="mp4")
    bitrate_list = []
    for x in audio_files:
        if x.abr == None:
            continue
        bitrate = x.abr.split('kbps')
        bitrate_list.append(int(bitrate[0]))
    bitrate_list.sort(reverse=True)
    highest_bitrate = f"{bitrate_list[0]}kbps"


    for y in audio_files:
        if y.abr == highest_bitrate:
            file_to_download = audio_files.get_by_itag(y.itag)
            shutil.move(file_to_download.download(), "downloaded")