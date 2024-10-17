import google.generativeai as genai
from jarvis.config import Config  
import pickle

class AI:
    def __init__(self):
        self.chat = None

    def connect(self):
        api_key = Config.get_gemini_api_key()
        genai.configure(api_key=api_key)

        generation_config = {
            "temperature": 0.5,
            "top_p": 0.90,
            "top_k": 40,
            "max_output_tokens": 400,
            "response_mime_type": "text/plain"
        }

        model = genai.GenerativeModel("gemini-1.5-flash", generation_config=generation_config)

        with open('./jarvis/data/datas.pkl', 'rb') as file:
            loaded_data = pickle.load(file)

        self.chat = model.start_chat(history=[])
        jarvis_data = loaded_data.get("jarvis", {}).get("content", "No data found")
        creators = loaded_data.get("shabari", {}).get("content", "No data found")
        self.chat.send_message(jarvis_data + creators + " Don't give unnecessary compliments; just give the content. You need to remember this until the end of the conversation.")
        return model


    def generate_content(self, model, prompt):

        best_prompt_response_for_audio = f"""
        Generate the content for the following prompt without any formatting just need the content alone. 
        Give some emotions in the text. 
        Here you are a voice assisstant capablable of speaking. 
        And tell the user like you can handle wide range of task assigned to you. 
        No emojis in the text.
        No hashtags in the text.
        No URLs in the text.
        Here is the prompt:
        {prompt}
        """
        # Send the user's message to the chat session
        response = self.chat.send_message(best_prompt_response_for_audio)

        filtered_content = response.text.replace("* **", "").replace("**", "")
        
        print("JARVIS: ", filtered_content)

        return filtered_content
