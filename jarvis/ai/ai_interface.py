import google.generativeai as genai
from jarvis.config import Config  
import jarvis.data.data as datas


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

        self.chat = model.start_chat(history=[])
        self.chat.send_message("From now your nickname is JARVIS and just for fun, you were created by a guy named Shabari. Tell them your name if they ask who you are, but otherwise don't react. Don't give unnecessary compliments; just give the content. You need to remember this until the end of the conversation. If you forget, just ask me to remind you.")
        return model


    def generate_content(self, model, prompt):
        if "shabari" in prompt.lower() or "sabari" in prompt.lower():
            prompt += datas.datas["shabari"]["content"] + " Select one of the content from the above and generate content for that."
            prompt = prompt.replace("sabari", "shabari").replace("Sabari", "Shabari")

        best_prompt_response_for_audio = f"""
        generate the content for the following prompt without any formatting just need the content alone. give some emotions in the text. Here you are a voice assisstant capablable of speaking. and tell the user like you can handle wide range of task assigned to you. Here is the prompt:
        {prompt}
        """
        # Send the user's message to the chat session
        response = self.chat.send_message(best_prompt_response_for_audio)

        filtered_content = response.text.replace("* **", "").replace("**", "")
        
        print("JARVIS: ", filtered_content)

        return filtered_content
