import os
import requests
from configs import VOICERSS_SIZE_LIMIT, API_KEY, LANGUAGE


class Connection:
    def __init__(self, text: str, file_save_name, file_save_folder):
        self.text_slice_list = None
        self.tx = text
        self.file_save_name = file_save_name
        self.file_save_folder = file_save_folder
        self.progress = '**'

    def to_voice(self):
        """Gets a list contains page-number and text,
        uses slicer to chop it for api standardization and sent it to api"""
        self.text_slicer()
        for i, tx in enumerate(self.text_slice_list):
            print(self.progress)
            self.api_connection(tx, i)
        return True

    def text_slicer(self):
        """ Dou to Voice-rss api limitation for sending text, we need to chp off the text in multiple parts"""
        self.text_slice_list = []
        text_slice = ''

        tx_len = len(self.tx)
        for i, char in enumerate(self.tx):
            text_slice += char
            if len(text_slice.encode("UTF-8")) > VOICERSS_SIZE_LIMIT or i == tx_len - 1:
                self.text_slice_list.append(text_slice)
                text_slice = ""

        return self.text_slice_list

    def api_connection(self,tx, number):
        params = {
            "key": API_KEY,
            "src": tx,
            "hl": LANGUAGE,
        }
        resp = requests.get("http://api.voicerss.org", params=params)

        file_loc_name = self.file_save_folder + r"\\" + self.file_save_name + "-voice" + f'{number+1}' + ".wav"
        with open(file_loc_name, mode="wb",) as audio:
            audio.write(resp.content)


