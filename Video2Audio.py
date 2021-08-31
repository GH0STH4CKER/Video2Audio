from moviepy.editor import *
from tkinter.filedialog import *
import os

def os_detect() :
    if os.name == 'nt':
        print('\nSaved Location:\n')
        os.system('cd')
    else :
        print('\nSaved Location:\n')
        os.system('pwd')

def video2audio(videofile,audiofile):
    videoclip=VideoFileClip(videofile)
    audioclip=videoclip.audio
    audioclip.write_audiofile(audiofile)
    audioclip.close()
    videoclip.close()

mp4file = askopenfilename()
mp3file = input('Save as (sample.mp3) : ')

video2audio(mp4file,mp3file)

os_detect() 