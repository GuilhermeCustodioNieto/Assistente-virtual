import keyboard
import subprocess

def on_hotkey():
    
    subprocess.Popen('dist/main.exe')


HOTKEY = 'ctrl + alt + shift'

keyboard.add_hotkey(HOTKEY, on_hotkey)

keyboard.wait()
