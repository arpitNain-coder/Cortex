from speech import speak
from commands.apps import apps
from commands.websites import sites
from speech import listen
from commands.websites import search
import os
import subprocess
import keyboard
import sys
from commands.system import handle_system
from commands.apps import app_handle
from commands.websites import web_handle

def process_command(command): 
    if handle_system(command):
        return
    elif app_handle(command):
        return
    elif web_handle(command):
        return
    else:
        speak("I didnt catch that")
