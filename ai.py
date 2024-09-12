import speech_recognition as sr
import subprocess
import  pyautogui
import colorama
from colorama import Fore,Back,Style
import time
import webbrowser as web

import datetime
from playsound import playsound
from datetime import date, timedelta
colorama.init(autoreset=True)

def say():
 try:
   r = sr.Recognizer()

   with sr.Microphone() as source:
     print("Say something: ")


     audio = r.listen(source)
     r.pause_threshold=0.5
   text = r.recognize_google(audio)
   print("You said: " + text.lower())
   









   if "lumos" in text.lower() :
          subprocess.call(["say","-v", "Daniel","lumos"])
          print(f"{Fore.WHITE}/////"*5)
   elif "imperio" in text.lower() :
          subprocess.call(["say","-v", "Albert","imperio"])
          print(f"{Fore.GREEN}/////"*5)
   elif "wingardium leviosa" in text.lower() :
          subprocess.call(["say","-v", "Daniel","wingardium leviosa"])
          print(f"{Fore.BLUE}/////"*5)





   elif "what is the time" in text.lower() or "time right now" in text.lower() or "what's the time" in text.lower():
               strtime=datetime.datetime.now().strftime("%H:%M")
               print(f"the time is {strtime}")
               subprocess.call(["say","-v", "Daniel",f"the time is {strtime}"])









 except text.ValueError:
     print("sorry , i can't understand.")
     subprocess.call(["say","-v", "Daniel","sorry , i can't understand."])




