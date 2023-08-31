import unittest
from pdf_to_speech.pdf_to_text.text_extract import page_reader

test_file_path = r"app_test.pdf"
expected_text1 = """header  
 
 
 this is page one of the document  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Footer """
expected_text2 = """
 this is page one of the document  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 """


class Test(unittest.TestCase):
    def test_page_reader(self):
        self.assertEqual(page_reader(test_file_path, 0), expected_text1)

    def test_page_reader_with_trim(self):
        self.assertEqual(page_reader(test_file_path, 0, True), expected_text2)


if __name__ == "__main__":
    unittest.main()
