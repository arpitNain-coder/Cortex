from speech import speak
from commands.apps import apps
from commands.websites import sites
from speech import listen
from commands.websites import search
import os
import subprocess
import keyboard
import sys

def process_command(command): 
    if "shutdown" in command or "shut" in command:
        speak("Shutting down")
        subprocess.run(["shutdown", "/s", "/t", "10"])
    elif "open" in command:
        found = False
        for appname in apps: 
            if appname in command:
                found = True
                speak(f"Opening {appname}")
                subprocess.run(apps[appname], shell = True)
        for webname in sites:
            if webname in command:
                found = True
                speak(f"Opening {webname}")
                subprocess.run(sites[webname], shell = True)
        if not found :
            speak("I didn't catch that")
    elif "search" in command :
        if "youtube" in command:
            command = command.replace("search ", "")
            command = command.replace(" on youtube", "")
            command = command.strip()
            speak(f"searching {command}")
            command = command.replace(" ", "+")
            
            subprocess.run(f"start https://www.youtube.com/results?search_query={command}", shell = True)
        elif "brave" in command:
            command = command.replace("search ", "")
            command = command.replace(" on brave", "")
            command = command.strip()
            speak(f"searching {command}")
            command = command.replace(" ", "+")
            subprocess.run(f"start https://search.brave.com/search?q={command}", shell = True)
    else:
        speak("I didnt catch that")
