import PySimpleGUI as sg
from delete_songs import delete_songs
from video_download import DownloadVideo
from song import Song
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
    [sg.Button("Create Song"), sg.Button("Create Clip")],
    [sg.Button("Delete Songs")],
    [sg.Button("Export"), sg.InputText(key="Export_Location", size=(30,1.5)), sg.FolderBrowse()]
]

window = sg.Window(title="Playlist Builder", layout=layout, margins=(50, 50))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "Create Song" or event == "Create Clip":
        user_input = values["user_input"]   #Retrieves user input
        song_name = sg.popup_get_text('Enter a song/clip name.', title="Song Name")
        user_start = values["user_start"]
        user_end = values["user_end"]
        path = f"downloaded/{user_input}"

        if os.path.isfile(path):
            new_song = Song(path, song_name, user_start, user_end)
            if event == "Create Song":
                new_song.create_song()
            else:
                new_song.create_clip()

        else:    
            video_to_download = DownloadVideo(user_input)
            video_to_download.download_video()
            new_song = Song(f"downloaded/{video_to_download.get_title()}.mp4", song_name, user_start, user_end)
            if event == "Create Song":
                new_song.create_song()
            elif event == "Create Clip":
                new_song.create_clip()

            
    
    if event == "Delete Songs":
        user_confirmation = sg.popup_get_text("Are you sure? Please type yes or no.")
        if user_confirmation == "yes":
            delete_songs()
    
    if event == "Export":
        if values["Export_Location"]:
            export_file_location = values["Export_Location"]
            for files in os.listdir("songs"):
                shutil.copy(f"songs/{files}", export_file_location)
        else:
            sg.popup("Please select a place for your files.")
    
    #if event == "Export":


window.close()