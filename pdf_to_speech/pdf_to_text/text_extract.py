import PyPDF2
from configs import HEADER_SIZE, FOOTER_SIZE


def page_reader(file_path: str, pages_list: list, head_foot_trim: bool = False):
    reader = PyPDF2.PdfReader(file_path)
    contents = []
    for page_num in pages_list:
        page_text = reader.pages[page_num]

        if head_foot_trim:
            parts = []

            def visitor_body(text, cm, tm, fontDict, fontSize):
                y = tm[5]
                # FOOTER  and  HEADER
                if FOOTER_SIZE < y < HEADER_SIZE:
                    parts.append(text)

            page_text.extract_text(visitor_text=visitor_body)
            page_text = "".join(parts)

        else:
            page_text = page_text.extract_text()

        contents.append((page_num+1, page_text))

    return contents
