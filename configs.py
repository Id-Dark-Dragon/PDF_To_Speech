import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("voicerss_api_key")

FOOTER_SIZE = 50  # Bigger size would chop lower parts of the text
HEADER_SIZE = 720  # Lower size would chop top parts of the text
VOICERSS_SIZE_LIMIT = 99 * 1024