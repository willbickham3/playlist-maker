import PySimpleGUI as sg
import tkinter as tk
from video_download import download_video
from song import create_song

layout = [
    [sg.Text("Build Your Own Playlist!")],
    [sg.InputText(key="user_input", size=(43, 1.5))],
    [sg.Text("Enter a start time and end time for your clip in seconds.")],
    [sg.Text("Start Time")],
    [sg.InputText(key="user_start", size=(5, 1.5), enable_events=True)],
    [sg.Text("End Time")],
    [sg.InputText(key="user_end", size=(5, 1.5))],
    [sg.Button("Submit")]
]

window = sg.Window(title="Playlist Builder", layout=layout, margins=(200, 200))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        user_input = values["user_input"]   #Retrieves user input
        input_path = download_video(user_input)
        song_name = sg.popup_get_text('Enter a song/clip name.', title="Song Name")
        user_start = values["user_start"]
        user_end = values["user_end"]

        create_song(f"downloaded/{input_path}.mp4", song_name, user_start, user_end)


window.close()