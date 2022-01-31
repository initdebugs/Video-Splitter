import PySimpleGUI as sg
import cv2
import os.path

file_selection = [
    [
        sg.T("Select video", key="input"),
        sg.In(size=(25, 1), enable_events=True, key="-VIDEO-"),
        sg.FileBrowse(),
        sg.T("Welcome! Select a video to begin...", key="splitStatus"),
    ]
]

layout = [
    [
        sg.Column(file_selection),
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
        sg.ProgressBar(1, orientation='h', size=(60, 10), border_width=4, key='progbar',bar_color=['Green','#a6a6a6'])
    ]
]

window = sg.Window("Video Splitter", layout)

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Start":
        filename = values["-VIDEO-"]

        if filename == "":
            window["splitStatus"].update("Please select a video first...")
            continue
        else:
            window["splitStatus"].update("Starting...")
    
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
        
            progress_bar = window.FindElement('progbar')

            count = 0
            cap = cv2.VideoCapture(filename)
            frameCount =  int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            outputDir = ("Frames")
            checkDir = os.path.isdir(outputDir)

            # If folder doesn't exist, then create it.
            if not checkDir:
                os.makedirs(outputDir)
                print("Created folder: ", outputDir)

            while True:
                window["splitStatus"].update("Splitting video...")
                if event == "Stop":
                    break
                event, values = window.read(timeout=20)
                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                success,image = cap.read()
                if success == True:
                    cv2.imwrite("Frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
                    print('Read a new frame: ', success)

                    count += frames
                    progress_bar.UpdateBar(count,frameCount)
                    cap.set(cv2.CAP_PROP_POS_FRAMES, count)
                else:
                    window["splitStatus"].update("Done.")
                    break
                
# window.close()
