from jarvis.functions.apps import check_applications
import speech_recognition as sr
import threading
import os
import asyncio
from PyQt5.QtCore import QTimer
from jarvis.needs.audio import text_to_speech, play_audio
from jarvis.needs.image import prompt_image
from jarvis.functions.weather import get_weather, get_weather_tomorrow
from jarvis.functions.action import check_all_actions
from jarvis.functions.sys_info import chech_system_info
from jarvis.functions.commands import check_calender_cmd
from jarvis.functions.news import manage_news

class SpeechRecognizer:
    def __init__(self, widget, app, model, ai):
        self.widget = widget
        self.app = app
        self.model = model
        self.ai = ai
        self.commands = []
        self.img = 0
        self.img_cmd = ""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def update_image(self):
        self.img = 2

    def listen_and_update(self):
        while True:
            with self.microphone as source:
                print("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=3)
                print("Listening for command...")

                # Update the widget state to listening
                self.widget.state = 'listening'
                self.widget.update()

                try:
                    print("Waiting for audio...")
                    audio = self.recognizer.listen(source, timeout=5)
                    self.widget.state = 'recognizing'
                    self.widget.update()
                    print("Recognizing command...")

                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Recognized: {command}")

                    self.process_command(command)

                except sr.WaitTimeoutError:
                    print("Listening timed out. No speech detected.")
                    self.widget.state = 'not_recognized'
                    self.widget.update()
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    self.widget.state = 'not_recognized'
                    self.widget.update()
                except Exception as e:
                    print(f"Error occurred: {e}")
                    self.widget.state = 'not_recognized'
                    self.widget.update()

    def process_command(self, command):
        if self.img == 2:
            response = self.ai.generate_content(self.model, self.img_cmd + " don't tell me unnecessary context. just tell me the command is completed successfully in 10 to 30 words.")
            asyncio.run(text_to_speech(response, "image.mp3"))
            play_audio("image.mp3")
            self.img = 0
            image_path = os.listdir("generated_image")
            image_path = image_path[-1]
            threading.Thread(target=os.system, args=(f"gwenview generated_image/{image_path}",)).start()

        if "generate image" in command:
            if self.img == 1:
                asyncio.run(text_to_speech("Already image generation is in progress", "image.mp3"))
                play_audio("image.mp3")
                return
            self.widget.state = 'recognized'
            self.widget.update()
            self.img = 1
            response = self.ai.generate_content(self.model, command + " don't tell me unnecessary context. just tell me the command is started and it will take some to generate that image in 10 to 30 words.")
            asyncio.run(text_to_speech(response, "image.mp3"))
            play_audio("image.mp3")
            threading.Thread(target=prompt_image, args=(command, self)).start()
            self.commands.append({"user": command, "jarvis": "Image generated"})
            return

        if "check image generation" in command:
            self.widget.state = 'recognized'
            self.widget.update()
            if self.img == 1:
                response = self.ai.generate_content(self.model, self.img_cmd + " don't tell me unnecessary context. just tell me the command is on the way in 10 to 30 words.")
                asyncio.run(text_to_speech(response, "image.mp3"))
                play_audio("image.mp3")
            else:
                asyncio.run(text_to_speech("No image generation is in progress", "image.mp3"))
                play_audio("image.mp3")
            self.commands.append({"user": command, "jarvis": "Image generation checked"})
            return

        if "what's the weather" in command.lower():
            self.widget.state = 'recognized'
            if "tomorrow" in command.lower():
                weather_report = get_weather_tomorrow()
            else:
                weather_report = get_weather()
            self.widget.update()
            print(weather_report)
            self.commands.append({"user": command, "jarvis": weather_report})
            asyncio.run(text_to_speech(weather_report, "weather.mp3"))
            play_audio("weather.mp3")
            return

        app_result, app_message = check_applications(command)
        if app_result:
            self.widget.state = 'recognized'
            self.widget.update()
            asyncio.run(text_to_speech(app_message, "app.mp3"))
            play_audio("app.mp3")
            self.commands.append({"user": command, "jarvis": app_message})
            return

        result = manage_news(command)
        if result[0]:
            self.widget.state = 'recognized'
            self.widget.update()
            print(result[1].get_news())
            res = ""
            for i in result[1].get_news():
                res += i["title"] + ". "
            response = self.ai.generate_content(self.model, res + " This is the news content i want you to narrate it to me.")
            asyncio.run(text_to_speech(response, "news.mp3"))
            play_audio("news.mp3")
            self.commands.append({"user": command, "jarvis": response})
            return

        elif check_all_actions(command):
            self.widget.state = 'recognized'
            self.widget.update()
            asyncio.run(text_to_speech("Action completed", "action.mp3"))
            play_audio("action.mp3")
            self.commands.append({"user": command, "jarvis": "Action completed"})
            return

        resp = check_calender_cmd(command)
        if resp[0]:
            self.widget.state = 'recognized'
            self.widget.update()
            print(resp[1])
            response = self.ai.generate_content(self.model, resp[1] + " no unnecessary context like What would you like me to do?  I'm ready to tackle any task you throw my way. just tell me " + command)
            asyncio.run(text_to_speech(response, "calender.mp3"))
            play_audio("calender.mp3")
            self.commands.append({"user": command, "jarvis": response})
            return

        resp = chech_system_info(command)
        if resp[0]:
            self.widget.state = 'recognized'
            self.widget.update()
            print(resp[1])
            response = self.ai.generate_content(self.model, resp[1] + "rewrite the response")
            asyncio.run(text_to_speech(response, "system_info.mp3"))
            play_audio("system_info.mp3")
            self.commands.append({"user": command, "jarvis": response})
            return

        elif "exit jarvis" in command.lower() or "close jarvis" in command.lower() or "execute shutdown sequence" in command.lower():
            print("Exit command received. Closing application...")
            self.widget.state = 'recognized'
            self.widget.update()
            response = self.ai.generate_content(self.model, "ok bye i am leaving")
            asyncio.run(text_to_speech(response, "exit.mp3"))
            play_audio("exit.mp3")
            QTimer.singleShot(0, self.app.quit)
            with open("commands.txt", "w") as file:
                file.write(str(self.commands))
            return

        elif "jarvis" in command:
            response = self.ai.generate_content(self.model, command)
            self.widget.state = 'recognized'
            self.widget.update()
            asyncio.run(text_to_speech(response, "response.mp3"))
            play_audio("response.mp3")
            self.commands.append({"user": command, "jarvis": response})
            return

        print("Unknown command")
        self.widget.state = 'not_recognized'
        self.widget.update()

    # Add other helper methods as needed
