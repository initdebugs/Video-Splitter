#Developed by @Initdebugs
from tkinter import DISABLED
import PySimpleGUI as sg
import cv2
import os.path

file_selection = [
    [
        sg.T("Select video ", key="input"),
        sg.In(size=(25, 1), disabled=True , enable_events=True, key="-VIDEO-"),
        sg.FileBrowse(file_types=(("MP4 files", "*.mp4"),)),
        sg.T("Welcome! Select a video to begin...", key="splitStatus"),
    ]
]
output_selection = [
    [
        sg.T("Output folder"),
        sg.In(size=(25, 1), disabled=True , enable_events=True, key="-OUTPUT-"),
        sg.FolderBrowse(),
        sg.T("", key="outputStatus"),
    ]
]

layout = [
    [
        sg.Column(file_selection),
    ],
    [
        sg.Column(output_selection),
    ],
    [
        sg.Radio('1 frame', "frameRadio", key="frame1", default=True),
        sg.Radio('2 frames', "frameRadio", key="frame2", default=False),
        sg.Radio('5 frames', "frameRadio", key="frame5", default=False),           
        sg.Radio('10 frames', "frameRadio", key="frame10", default=False),           
        sg.Radio('30 frames', "frameRadio", key="frame30", default=False),           
        sg.Radio('120 frames', "frameRadio", key="frame120", default=False),           
        sg.Button("Start"),
        sg.Button("Stop"),
    ],
    [
        sg.Radio('Custom', "frameRadio", key="framecustom", default=False),
        sg.Spin([i for i in range(1,2000)], size=(10, 10),initial_value=1, key="customSpin"),
        sg.VSep(),
        sg.T("", key="processingText" ),
    ],
    [
        sg.ProgressBar(1, orientation='h', size=(60, 10), border_width=4, key='progbar',bar_color=['Green','#a6a6a6'])
    ]
]

window = sg.Window("Video Splitter", layout)
folderCount = 0
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Start":
        filename = values["-VIDEO-"]
        outputDir = values["-OUTPUT-"]

        if filename == "":
            window["splitStatus"].update("Please select a video first...")
            continue
        if outputDir == "":
            window["outputStatus"].update("Please select an output folder first...")
            continue
        elif not len(os.listdir(outputDir)) == 0:
            window["outputStatus"].update("The selected folder is not empty")
            continue
        window["splitStatus"].update("Starting...")
        customFrameNumber = values["customSpin"]

        frames = 0
        if values["frame1"] == True:
            frames = 1
        elif values["frame2"] == True:
            frames = 2
        elif values["frame5"] == True:
                frames = 5
        elif values["frame10"] == True:
            frames = 10
        elif values["frame30"] == True:
            frames = 30
        elif values["frame120"] == True:
            frames = 120   
        elif values["framecustom"] == True:
            frames = customFrameNumber     
        
        progress_bar = window.FindElement('progbar')

        count = 0
        cap = cv2.VideoCapture(filename)
        frameCount =  int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        while True:
            window["splitStatus"].update("...")
            window["outputStatus"].update("")

            if event == "Stop":
                break
            event, values = window.read(timeout=20)
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            success,image = cap.read()
            if success == True:
                cv2.imwrite(values["-OUTPUT-"]+"/frame%d.jpg" % count, image)     # save frame as JPEG file      
                print('Read a new frame: ', success)

                count += frames
                progress_bar.UpdateBar(count,frameCount)
                window["processingText"].update("Processing... " + str(count) + " of " + str(frameCount) + " frames")
                cap.set(cv2.CAP_PROP_POS_FRAMES, count)
            else:
                window["processingText"].update("Processing done.")
                window["splitStatus"].update("Ready!")

                break
