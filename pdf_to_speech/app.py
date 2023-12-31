import os

from configs import HEADER_FOOTER_TRIM
from pdf_to_speech.pdf_to_text.text_extract import page_reader
from pdf_to_speech.text_to_speech.voicerss_connection import Connection


class App:
    def __init__(self):
        self.voice_cut_per_page = "YES"
        self.file_loc = None
        self.pages_num_input = "2-3"
        self.page_order_list = []

    def preparation_input(self):
        self.file_loc = input("1. Input absolute path of your pdf file:  ")
        self.pages_num_input = input("2. Which pages do you want to convert to speech? \n"
                                     "Usable formats: e.g. ( 2-5 for range ), ( 2,3,4 for individuals) \n")

        if "," in self.pages_num_input or "-" in self.pages_num_input:
            self.voice_cut_per_page = input("3. Do you want voices to be separate per page? (yes or no) \n")

        self.file_loc = fr"{self.file_loc}"
        self.pages_num_input = self.pages_num_input.replace(" ", "")
        self.voice_cut_per_page = self.voice_cut_per_page.upper().replace(" ", "")

        self.manager()

    def page_orderer(self):
        """ This Function makes a listr of the desired pages."""
        # Page Range Selection
        if "-" in self.pages_num_input:
            page1, page2 = self.pages_num_input.split("-")
            page_order_list = [int(i) - 1 for i in range(int(page1), int(page2)+1)]

        # individual page selection
        elif "," in self.pages_num_input:
            page_order_list = [int(i) - 1 for i in self.pages_num_input.replace(" ", "").split(",")]

        # one-page selection
        else:
            page_order_list = [int(self.pages_num_input) - 1]

        return page_order_list

    def manager(self):
        page_order_list = self.page_orderer()
        contents = page_reader(self.file_loc, pages_list=page_order_list, head_foot_trim=HEADER_FOOTER_TRIM)
        print("_____________\nText Extracted!")
        # make a folder with pdf name
        if not os.path.exists(self.file_loc[0:-4]):
            os.mkdir(self.file_loc[0:-4])
        save_name_prefix = os.path.basename(self.file_loc)[:-4]

        if self.voice_cut_per_page == "YES":
            for content in contents:
                resp = Connection(text=content[1], file_save_name=f"{save_name_prefix}-page{content[0]}",
                           file_save_folder=self.file_loc[0:-4]).to_voice()

        elif self.voice_cut_per_page == "NO":
            parts = []
            for content in contents:
                parts.append(content[1])
            text = " ".join(parts)
            resp = Connection(text=text, file_save_name=f"{save_name_prefix}",
                       file_save_folder=self.file_loc[0:-4]).to_voice()

        if resp:
            print("Job Finished")
            print('-------------------')



