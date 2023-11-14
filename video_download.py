from pytube import YouTube
import shutil
from pytube.exceptions import VideoUnavailable, VideoPrivate, RegexMatchError
import os
import re


def download_video(url):
    """Takes in a url in string form and downloads the highest quality sound from the video"""
    
    url = f"{url}"
        
            
    if "youtube.com/watch?v=" not in url:
        print("URL is not from YouTube. Please provide a YouTube URL.")
        return
    
    print(url)
    yt = YouTube(url)
    pattern = r'[\\/:*?"<>|]'
    yt.title = re.sub(pattern, "", yt.title)
    path = f"downloaded/{yt.title}.mp4"
    
    try:
        if yt.streams:
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
                    return yt.title
        else:
            raise Exception("No streamable content found in the provided URL.")
    except VideoPrivate:
        print("Video is private and cannot be downloaded.")
    except VideoUnavailable:
        print("Video is unavailable or restricted.")
