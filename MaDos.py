import os
import time

import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


print("Welcome to MaDos Console! V3.5.1")
mapver = "V3.5.1"



while (True):
    code = input("C:\>: ")
    if (code):
        if (code == " " or ""):
            print("Not a valid command.")

    if (code == "payam"):
        state = input("What to print: ")
        print(state)

    if (code == "cls"):
        os.system("cls")

    if (code == "exit"):
        exit()

    if (code == "help"):
        what = input("With what? instl, args, or cmds?: ")
        if (what == "cmds"):
            print("Commands are: payam, cls, exit, shutdown, pause, spam, color, files, sendkey, help, PNINSTL, start, vol, mkdir, taskkill, date, update, mapyter, cmd, time, diskpart, cd, tasklist")

        if (what == "instl"):
            print("Download PYTHON off python.org to use this coding language.")
        if (what == "args"):
            print("Args List: Shutdown(s,r,i), Color(r,g,b,w,k), mados(--version, --uninstall, --info, --owner)")


    if (code == "pause"):
        input("Press any key to continue")
        os.system("cls")

    if (code == "shutdown"):
        que = input("Args: ")
        if (que == "r"):
            os.system("shutdown -r")
        if (que == "s"):
            os.system("shutdown -s")

        if (que == "i"):
            os.syetem("shutdown -i")
    
    if (code == "files"):
        print(os.system("tree"))

    if (code == "color"):
        arg = input("Args: ")
        if (arg == "r"):
            os.system("color 0c")

        if (arg == "g"):
            os.system("color 2")
        if (arg == "b"):
            os.system("color 1")
        if (arg == "w"):
            os.system("color 7")
        if (arg == "k"):
            os.system("color E")

    if (code == "spam"):
        waaaa = input("Spam what?: ")
        while (True):
            print(waaaa)

    if (code == "sendkey"):
        print("WARNING! THIS ONLY WORKS IF YOU HAVE PYNPUT INSTALLED! IF YOU DO NOT, USE THE COMMAND PNINSTL")
        key = input("What would you like to type: ")
        if (key):
            from pynput.keyboard import Key, Controller
            keyb = Controller()

            keyb.press(key)
            keyb.release(key)

    if (code == "PNINSTL"):
        os.system("pip install pynput")

    if (code == "start"):
        dirr = input("File location: ")
        os.system("start " + dirr)

    if (code == "vol"):
        print(os.system("vol"))

    if (code == "taskkill"):
        task = input("Task name: ")
        os.system("taskkill /f /IM " + task)
    
    if (code == "mkdir"):
        os.system("mkdir")

    if (code == "date"):
        os.system("date")

    if (code == "update"):
        browser = input("Enter your browser name! (chrome or msedge): ")
        if (browser == "chrome"):
            os.system("start chrome.exe https://github.com/Algrythm/Mapyter")

        if (browser == "msedge"):
            os.system("start msedge.exe https://github.com/Algrythm/Mapyter")

    if (code == "mados"):
        print("Insufficient arguments provided!")

    if (code == "mados --version"):
        print("Current Installed Mapyter version is: " + mapver)

    if (code == "mados --uninstall"):
        print("Uninstalling mapyter! Close program to cancel!")
        time.sleep(15)
        Mbox('Uninstalled!', "We're sorry to see you go! ):", 1)
        time.sleep(2)
        os.remove("MaDos.py")
        exit()

    if (code == "mados --info"):
        print("Mapyter is a coding language coded my Marsden Cannon in Python.")

    if (code == "mados --owner"):
        os.system("start chrome.exe https://www.youtube.com/channel/UC5yR6zakk5yEXmJ3iwKdiRQ")
    
    if (code == "cmd"):
        os.system("cmd")

    if (code == "time"):
        os.system("time")

    if (code == "tasklist"):
        os.system("tasklist")

    if (code == "diskpart"):
        os.system("diskpart")
    if (code == "cd"):
        os.system("cd")

    

        

    
    
    

    

   

    
        
        

    

    
