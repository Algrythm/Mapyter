import os
import time
os.system("color 7D")

print("Welcome to Mapyter Console! V2.0.1")
mapver = "V2.0.1"


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
            print("Commands are: payam, cls, exit, shutdown, pause, spam, color, files, sendkey, help, PNINSTL, start, vol, mkdir, taskkill, date, update, mapyter, title, cmd")

        if (what == "instl"):
            print("Download PYTHON off python.org to use this coding language.")
        if (what == "args"):
            print("Args List: Shutdown(s,r,i), Color(r,g,b,w,k), mapyter(--version, --uninstall, --info, --owner)")


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

    if (code == "mapyter"):
        print("Insufficient arguments provided!")

    if (code == "mapyter --version"):
        print("Current Installed Mapyter version is: " + mapver)

    if (code == "mapyter --uninstall"):
        print("Uninstalling mapyter! Close program to cancel!")
        time.sleep(15)
        os.remove("Mapyter.py")
        exit()

    if (code == "mapyter --info"):
        print("Mapyter is a coding language coded my Marsden Cannon in Python.")

    if (code == "mapyter --owner"):
        os.system("start chrome.exe https://www.youtube.com/channel/UC5yR6zakk5yEXmJ3iwKdiRQ")
    
    if (code == "cmd"):
        os.system("cmd")

    
    if (code == "title"):
        titlee = input("What do you want to title the window?: ")
        os.system(titlee)
    
    

    

   

    
        
        

    

    
