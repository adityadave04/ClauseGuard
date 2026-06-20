# llm/grok_client.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class GrokClient:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROK_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

    def invoke(self, prompt: str):

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=1500
        )

        return response.choices[0].message.content