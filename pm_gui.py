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
        download_video(user_input)
        sg.popup("You pressed the button!")
        user_start = values["user_start"]
        user_end = values["user_end"]
        create_song("downloaded/Ransom.mp4", "Ransom", user_start, user_end)
        

    if event == "user_start" and values["user_start"] == "Start":
        sg.popup('hi')
        window["user_start"].update(value="")

    if event =="user_end" and values["user_end"] == "End":
        window["user_end"].update(value="")

window.close()