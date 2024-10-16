import pyautogui as pg
from jarvis.needs.audio import text_to_speech, play_audio
import asyncio

def scroll_down():
    pg.scroll(-10)

def scroll_up():
    pg.scroll(10)

def scroll_left():
    pg.hscroll(-10)

def scroll_right():
    pg.hscroll(10)

def show_next_window():
    pg.hotkey('alt', 'tab')

def show_previous_window():
    pg.hotkey('alt', 'shift', 'tab')

def show_next_tab():
    pg.hotkey('ctrl', 'tab')

def show_previous_tab():
    pg.hotkey('ctrl', 'shift', 'tab')

def close_current_tab():
    pg.hotkey('ctrl', 'w')

def close_current_window():
    pg.hotkey('alt', 'f4')

async def perform_action_with_audio(action_func, message):
    await text_to_speech(message, "action.mp3")
    play_audio("action.mp3")
    action_func()

def check_all_actions(command):
    if "scroll down" in command.lower():
        scroll_down()
        return True
    elif "scroll up" in command.lower():
        scroll_up()
        return True
    elif "scroll left" in command.lower():
        scroll_left()
        return True
    elif "scroll right" in command.lower():
        scroll_right()
        return True
    elif "next window" in command.lower():
        asyncio.run(perform_action_with_audio(show_next_window, "Switching to the next window"))
        return True
    elif "previous window" in command.lower():
        asyncio.run(perform_action_with_audio(show_previous_window, "Switching to the previous window"))
        return True
    elif "next tab" in command.lower():
        asyncio.run(perform_action_with_audio(show_next_tab, "Switching to the next tab"))
        return True
    elif "previous tab" in command.lower():
        asyncio.run(perform_action_with_audio(show_previous_tab, "Switching to the previous tab"))
        return True
    elif "close tab" in command.lower():
        asyncio.run(perform_action_with_audio(close_current_tab, "Closing the current tab"))
        return True
    elif "close this window" in command.lower():
        asyncio.run(perform_action_with_audio(close_current_window, "Closing this window"))
        return True
    
    return False

