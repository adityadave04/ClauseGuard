import os

from dotenv import load_dotenv

load_dotenv()

class Settings:

    def __init__(self):

        self.APP_ENV = os.getenv(
            "APP_ENV",
            "development"
        )

        self.LOG_LEVEL = os.getenv(
            "LOG_LEVEL",
            "INFO"
        )

        self.GROK_API_KEY = os.getenv(
            "GROK_API_KEY"
        )

        self.QDRANT_URL = os.getenv(
            "QDRANT_URL"
        )

        self.QDRANT_API_KEY = os.getenv(
            "QDRANT_API_KEY"
        )

        self.QDRANT_COLLECTION = os.getenv(
            "QDRANT_COLLECTION",
            "contracts"
        )

settings = Settings()