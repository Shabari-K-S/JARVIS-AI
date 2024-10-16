import edge_tts
import asyncio
import os

# Function to convert text to speech and save it as an MP3 file using edge_tts
async def text_to_speech(text, output_file="output.mp3"):
    communicator = edge_tts.Communicate(text, voice="en-US-EmmaMultilingualNeural", rate="+5%", volume="+10%")  # You can change the voice
    await communicator.save(output_file)

# Function to play the generated MP3 file using pygame
def play_audio(file):
    os.system(f"mpg123 {file}")
    os.remove(file)
