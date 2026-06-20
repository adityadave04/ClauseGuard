import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()


class LLMClient:

    def invoke(self, prompt: str):

        response = completion(
            model="xai/grok-3-mini",
            api_key=os.getenv("GROK_API_KEY"),
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