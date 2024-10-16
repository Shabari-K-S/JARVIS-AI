import os
from dotenv import load_dotenv, set_key

# Load environment variables from .env file
load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

    @classmethod
    def get_gemini_api_key(cls):
        return cls.GEMINI_API_KEY

    @classmethod
    def get_openweather_api_key(cls):
        return cls.OPENWEATHER_API_KEY


def setup_env():
    env_file = '.env'
    
    print("Setting up API keys. Press Enter to skip if you don't want to change the existing key.")

    gemini_key = input("Enter your Gemini API key: ").strip()
    if gemini_key:
        set_key(env_file, 'GEMINI_API_KEY', gemini_key)
        Config.GEMINI_API_KEY = gemini_key

    openweather_key = input("Enter your OpenWeather API key: ").strip()
    if openweather_key:
        set_key(env_file, 'OPENWEATHER_API_KEY', openweather_key)
        Config.OPENWEATHER_API_KEY = openweather_key

    huggingface_key = input("Enter your Hugging Face API key: ").strip()
    if huggingface_key:
        set_key(env_file, 'HUGGINGFACE_API_KEY', huggingface_key)
        Config.HUGGINGFACE_API_KEY = huggingface_key

    print("API keys have been updated in the .env file.")

if __name__ == "__main__":
    setup_env()