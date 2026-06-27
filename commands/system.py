
import subprocess
from speech import speak

def handle_system(command):
    if "shutdown" in command or "shut" in command:
        speak("Shutting down")
        subprocess.run(["shutdown", "/s", "/t", "10"])