from diffusers import DiffusionPipeline
import os
import sys
import edge_tts
if sys.platform == "win32":
    import pyttsx3

# Function to convert text to speech and save it as an MP3 file using edge_tts
async def text_to_speech(text, output_file="output.mp3"):
    if sys.platform == "win32":
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    elif sys.platform == "darwin":
        os.system(f"say {text}")
    else:
        communicator = edge_tts.Communicate(text, voice="en-US-EmmaMultilingualNeural", rate="+5%", volume="+10%")  # You can change the voice
        await communicator.save(output_file)

# Function to play the generated MP3 file using pygame
def play_audio(file):
    if sys.platform == "win32":
        pass
    elif sys.platform == "darwin":
        pass
    else:
        os.system(f"mpg123 {file}")
        os.remove(file)

