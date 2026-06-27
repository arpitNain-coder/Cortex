import os
import subprocess
import keyboard
import sys
import webbrowser
from speech import speak
from commands.apps import apps
from commands.websites import sites
from speech import listen
from commands.websites import search
from brain import process_command
speak("Hello Jarvis is ready")



while True:
    keyboard.wait("ctrl+5+8")
    speak("Listening")
    
    command = listen()
    process_command(command)

