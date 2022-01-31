# Video Splitter

This is a simple Python tool with visual GUI that helps with splitting video's into seperate frames. This could be useful for labeling images for machine learning.

![image](https://user-images.githubusercontent.com/75781464/151802255-0d75b195-40a6-44da-b4ab-44ca611774db.png)

# Requirements
- Python 3
- OpenCV
`pip3 install opencv-python opencv-contrib-python`

- PySimpleGUI
`pip3 install pysimplegui`

# How to start
1. Download the code and place the `split.py` file in a directory of your choosing;
2. Open a Command Propt and change your working directory to the directory where you placed your `split.py` file; [Tutorial here](https://www.howtogeek.com/659411/how-to-change-directories-in-command-prompt-on-windows-10/)
3. In your command prompt, write `python split.py`. A window now pops up;
4. Select your video file by clicking on browse;
5. Select the amount of frames to skip for each image (1 saves every frame from the video, 120 skips 120 frames and then saves an image)
6. Once the progress bar is full and the status text says 'Done', the program is ready for you to select a new video.

The program automatically creates a directory called 'Frames' inisde the directory where the `split.py` file is located. Every new Video split will be saved inside a new 'Frames' directory, so the files will never merge.

If you have any ideas on how to improve this simple tool, please let me know by sending me a message on Instagram `@lesleynatrop`

Have a nice day!
