from distutils.command.config import LANG_EXT
import os # to open the mp4 file automatically 
from gtts import gTTS # import this module fot text to speech conversion


text = "Kumusta? Kumain ka na ba?" # text that you want to convert


# if you want to convert text from file
'''abc = open('Text to Audio\sample.txt')
   text = abc.read()''' 


language = 'tl' # tl is for Tagalog Language

obj = gTTS(text = text, lang = language, slow = False)
# slow = False to have high speed 

obj.save("audio.mp3")

os.system("audio.mp3")
