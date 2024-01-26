import PySimpleGUI as sg
from delete_songs import delete_songs
from video_download import DownloadVideo
from song import create_song
import os
import shutil

layout = [
    [sg.Text("Build Your Own Playlist!")],
    [sg.InputText(key="user_input", size=(43, 1.5))],
    [sg.Text("Enter a start time and end time for your clip in seconds.")],
    [sg.Text("Start Time")],
    [sg.InputText(key="user_start", size=(5, 1.5), enable_events=True)],
    [sg.Text("End Time")],
    [sg.InputText(key="user_end", size=(5, 1.5))],
    [sg.Button("Submit")],
    [sg.Button("Delete Songs"), sg.Button("Export")]
]

window = sg.Window(title="Playlist Builder", layout=layout, margins=(50, 50))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        user_input = values["user_input"]   #Retrieves user input
        song_name = sg.popup_get_text('Enter a song/clip name.', title="Song Name")
        user_start = values["user_start"]
        user_end = values["user_end"]
        path = f"downloaded/{user_input}"

        if os.path.isfile(path):
            create_song(path, song_name, user_start, user_end)
        else:
            #input_path = download_video(user_input)
            video_to_download = DownloadVideo(user_input)
            video_to_download.download_video()
            create_song(f"downloaded/{video_to_download.get_title()}.mp4", song_name, user_start, user_end)
    
    if event == "Delete Songs":
        user_confirmation = sg.popup_get_text("Are you sure? Please type yes or no.")
        if user_confirmation == "yes":
            delete_songs()
    
    #if event == "Export":


window.close()