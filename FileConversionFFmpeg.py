import ffmpy
import FFmpeg
import os


path = "enterfilepathhere"

for filename in os.listdir(path):
    if (filename.endswith(".mp4")): #or .avi, .mpeg, 
        os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
    else:
        return
