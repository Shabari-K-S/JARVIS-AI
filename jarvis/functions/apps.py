import os
import pyautogui as pg
import time
import sys
import webbrowser

def open_instagram():
    webbrowser.open("https://www.instagram.com")

def open_whatsapp():
    webbrowser.open("https://www.whatsapp.com")

def open_gmail():
    webbrowser.open("https://mail.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google():
    webbrowser.open("https://www.google.com")

def open_file_explorer():
    if sys.platform == "win32":
        pg.hotkey('win', 'e')
    else:
        os.system("nautilus")

def open_vs_code():
    if sys.platform == "win32":
        pg.press('win')
        pg.write("vscode")
        pg.press('enter')
    else:
        os.system("code")

def open_terminal():
    if sys.platform == "win32":
        pg.press('win')
        pg.write("cmd")
        pg.press('enter')
    else:
        os.system("gnome-terminal")

def open_vs_code_for_project():
    if sys.platform == "win32":
        pg.press('win')
        pg.write("vscode")
        pg.press('enter')
    else:
        os.system("code")
    time.sleep(0.5)
    pg.keyDown('ctrl')
    pg.press('k')
    pg.press('o')
    pg.keyUp('ctrl')

def open_github():
    webbrowser.open("https://github.com")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com")

def open_spotify():
    webbrowser.open("https://open.spotify.com")

def check_applications(command):
    if "instagram" in command.lower():
        open_instagram()
        return True, "Opening Instagram"
    elif "whatsapp" in command.lower():
        open_whatsapp()
        return True, "Opening WhatsApp"
    elif "gmail" in command.lower():
        open_gmail()
        return True, "Opening Gmail"
    elif "youtube" in command.lower():
        open_youtube()
        return True, "Opening YouTube"
    elif "google" in command.lower():
        open_google()
        return True, "Opening Google"
    elif "file explorer" in command.lower():
        open_file_explorer()
        return True, "Opening File Explorer"
    elif "vs code" in command.lower():
        open_vs_code()
        return True, "Opening Visual Studio Code"
    elif "terminal" in command.lower():
        open_terminal()
        return True, "Opening Terminal"
    elif "project" in command.lower():
        open_vs_code_for_project()
        return True, "Opening Visual Studio Code for the project"
    elif "github" in command.lower():
        open_github()
        return True, "Opening GitHub"
    elif "linkedin" in command.lower():
        open_linkedin()
        return True, "Opening LinkedIn"
    elif "spotify" in command.lower():
        open_spotify()
        return True, "Opening Spotify"
    else:
        return False, ""

