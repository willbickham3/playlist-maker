from pytube import YouTube
import shutil
from pytube.exceptions import VideoUnavailable, VideoPrivate, RegexMatchError
import re


class DownloadVideo:
    """Defines a YouTube Video object that allows a user to download videos"""
    def __init__(self, url) -> None:
        self._url = url
        pass

    def get_title(self):
        """Returns the title of the video"""
        yt = YouTube(self._url)
        pattern = r'[\\/:*?"<>|]'
        yt.title = re.sub(pattern, "", yt.title)

        return yt.title

    def download_video(self):
        """Downloads a video from the given url"""
        url = f"{self._url}"
    
        if "youtube.com/watch?v=" not in url:
            raise NotAYouTubeURL("URL is not from YouTube. Please provide a YouTube URL.")
        
        yt = YouTube(url)
        # pattern = r'[\\/:*?"<>|]'
        # yt.title = re.sub(pattern, "", yt.title)
        
        try:                # Try to find the highest quality audio from the video; Else it provides the 
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
                        return
            else:
                raise NotStreamableContent("No streamable content found in the provided URL.")
        except VideoPrivate:
            print("Video is private and cannot be downloaded.")
        except VideoUnavailable:
            print("Video is unavailable or restricted.")


class NotAYouTubeURL(Exception):
    """Exception that is called when a URL is not from YouTube"""
    pass

class NotStreamableContent(Exception):
    """Exception that is called when a URL/Video is not streamable content"""
    pass

class PrivateVideo(Exception):
    """Exception that is called when a video is private"""
    pass

class VideoUnavailable(Exception):
    """Exception that is called when a video is unavailable"""
    pass
