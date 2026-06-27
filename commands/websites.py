import subprocess
from speech import speak

sites = {
    "youtube" : "start https://www.youtube.com",
    "code forces" : "start https://codeforces.com/profile/Shura_Oni",
    "discord" : "start https://discord.com/channels/1376380498183589989/1376381279561322586",
    "chat" : "start https://chatgpt.com/",
    "course" : "start https://maang.in/profile",
}

search = {
    "youtube" : "https://www.youtube.com/results?search_query=",
    "brave" : "https://search.brave.com/search?q="
}

def web_handle(command) :
    if "search" in command:
        if "youtube" in command:
                command = command.replace("search ", "")
                command = command.replace(" on youtube", "")
                command = command.strip()
                speak(f"searching {command}")
                command = command.replace(" ", "+")
                
                subprocess.run(f"start https://www.youtube.com/results?search_query={command}", shell = True)
                return True
        elif "brave" in command:
                command = command.replace("search ", "")
                command = command.replace(" on brave", "")
                command = command.strip()
                speak(f"searching {command}")
                command = command.replace(" ", "+")
                subprocess.run(f"start https://search.brave.com/search?q={command}", shell = True)
                return True