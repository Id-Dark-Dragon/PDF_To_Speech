# PDF to Speech

*This is a little practice project to make my hands dirty on:* 
- *Using voice generator APIs*
- *Making a package-based-structure app*
- *Writing Unit test scripts*

This script converts a PDF file to speech. It uses `pypdf2` to extract text from the PDF and `voicerss` API to convert the text to speech.




## Run

If you ever wish to run this script, you need a **unique `VoiceRSS` API key**. *(Sign-up in https://www.voicerss.org/ to get one for no charge.)*

Use the API key to modify `config.py`:

```bash
  API_KEY = os.getenv("voicerss_api_key") #delete this to replace your own api-key
```
Then run `run.py`.

If you answer the first 3 inputs at the console and everything goes well, You get a folder of voices inside the same directory as your PDF.



## Appendix

There are some more capabilities I am eager to mention

- **Trim header and footer to not be included in the voice file**
  
  achieve this by modifying the below variables inside `configs.py`: 
    ```bash
  
    HEADER_FOOTER_TRIM = False
    FOOTER_SIZE = 50  # Bigger size would chop lower parts of the text
    HEADER_SIZE = 720  # Lower size would chop the top parts of the text


    ```



- **Change language if your PDF is not in English**
  
  achieve this by modifying the below variable inside `configs.py`: 
    ```bash
    LANGUAGE = "en-ca"

    ```
   [Here is a list of available languages and accents](https://www.voicerss.org/api/)
## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)