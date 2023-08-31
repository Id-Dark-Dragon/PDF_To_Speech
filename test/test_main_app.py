import unittest
from unittest.mock import patch

from pdf_to_speech.app import App


class TestApp(unittest.TestCase):
    @patch('builtins.input', side_effect=["path/to/your/pdf", "1", "no"])
    def test_app_single_page(self, mock_input):
        app = App()
        app.preparation()
        self.assertEqual(app.file_loc, "path/to/your/pdf")
        self.assertEqual(app.pages_num, "1")
        self.assertEqual(app.voice_cut_per_page, "no")

    @patch('builtins.input', side_effect=["path/to/your/pdf", "2,3,4", "yes"])
    def test_app_multiple_pages(self, mock_input):
        app = App()
        app.preparation()
        self.assertEqual(app.file_loc, "path/to/your/pdf")
        self.assertEqual(app.pages_num, "2,3,4")
        self.assertEqual(app.voice_cut_per_page, "yes")

    @patch('builtins.input', side_effect=["path/to/your/pdf", "2-5", "no"])
    def test_app_page_range(self, mock_input):
        app = App()
        app.preparation()
        self.assertEqual(app.file_loc, "path/to/your/pdf")
        self.assertEqual(app.pages_num, "2-5")
        self.assertEqual(app.voice_cut_per_page, "no")


if __name__ == "__main__":
    unittest.main()
