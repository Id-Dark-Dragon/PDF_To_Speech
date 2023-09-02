import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
from pdf_to_speech.app import App
from pdf_to_speech.text_to_speech.voicerss_connection import Connection


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.file_loc = r"..\test\app_test.pdf"

    @patch("pdf_to_speech.app.App.manager")
    def test_page_orderer_range(self, mock_manager_func):
        self.app.pages_num_input = "2-4"
        self.app.page_orderer()
        self.assertEqual(self.app.page_orderer(), [1, 2, 3])

        self.app.pages_num_input = "1-2"
        self.assertEqual(self.app.page_orderer(), [0, 1])

    def test_page_orderer_individuals(self):
        self.app.pages_num_input = "2,3,4"
        self.assertEqual(self.app.page_orderer(), [1, 2, 3])

    def test_page_orderer_single(self):
        self.app.pages_num_input = "2"
        self.assertEqual(self.app.page_orderer(), [1])

    @patch('pdf_to_speech.text_to_speech.voicerss_connection.Connection.to_voice',)
    @patch('pdf_to_speech.pdf_to_text.text_extract.page_reader', return_value=[(1, "Page 1 text"), (2, "Page 2 text")])
    @patch("pdf_to_speech.app.App.page_orderer", return_value=[1, 2])
    @patch('pdf_to_speech.app.os.mkdir')
    def test_manager(self, mock_mkdir, mock_page_orderer, mock_page_reader, mock_to_voice):
        self.app.voice_cut_per_page = "YES"
        self.app.manager()
        mock_mkdir.assert_called_once()


    @patch('pdf_to_speech.text_to_speech.voicerss_connection.Connection.to_voice', return_value = [True])
    @patch('pdf_to_speech.pdf_to_text.text_extract.page_reader', return_value=[(1, "Page 1 text"), (2, "Page 2 text")])
    @patch("pdf_to_speech.app.App.page_orderer", return_value=[1, 2])
    @patch('pdf_to_speech.app.os.mkdir')
    def test_manager_voice_per_page(self, mock_mkdir, mock_page_orderer, mock_page_reader, mock_to_voice):
        self.app.pages_num_input = "1-2"
        self.app.voice_cut_per_page = "YES"
        self.app.manager()
        self.assertEqual(mock_to_voice.call_count, 2)

    @patch('pdf_to_speech.text_to_speech.voicerss_connection.Connection.to_voice', return_value = [True])
    @patch('pdf_to_speech.pdf_to_text.text_extract.page_reader', return_value=[(1, "Page 1 text"), (2, "Page 2 text")])
    @patch("pdf_to_speech.app.App.page_orderer", return_value=[1, 2])
    @patch('pdf_to_speech.app.os.mkdir')
    def test_manager_voice_merged(self, mock_mkdir, mock_page_orderer, mock_page_reader, mock_to_voice):
        self.app.pages_num_input = "1-2"
        self.app.voice_cut_per_page = "NO"
        self.app.manager()
        self.assertEqual(mock_to_voice.call_count, 1)


if __name__ == '__main__':
    unittest.main()
