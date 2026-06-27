import subprocess
from speech import speak


sites = {
    "youtube" : "start https://www.youtube.com",
    "code forces" : "start https://codeforces.com/profile/Shura_Oni",
    "discord" : "start https://discord.com/channels/1376380498183589989/1376381279561322586",
    "chat" : "start https://chatgpt.com/",
    "course" : "start https://maang.in/profile",
}

apps = {
    "vs code": "start code",
    "brave": "start brave",
}

def app_handle(command):
    if "open" in command:
        found = False
        for appname in apps: 
            if appname in command:
                found = True
                speak(f"Opening {appname}")
                subprocess.run(apps[appname], shell = True)
                return True
        for webname in sites:
            if webname in command:
                found = True
                speak(f"Opening {webname}")
                subprocess.run(sites[webname], shell = True)
                return True
        if not found :
            speak("I didn't catch that")