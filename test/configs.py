"""this config would be applied automatically in testing environment"""

FOOTER_SIZE = 100  # Bigger size would chop lower parts of the text
HEADER_SIZE = 650  # Lower size would chop top parts of the text

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("voicerss_api_key")
LANGUAGE = "en-ca"
VOICERSS_SIZE_LIMIT = 99 * 1024