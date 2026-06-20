# rag/ocr_reader.py

from pdf2image import convert_from_path
import pytesseract
import os
from dotenv import load_dotenv

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_CMD")
POPPLER_PATH = os.getenv("POPPLER_PATH")


def extract_text_ocr(pdf_path):

    pages = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    result = []

    for i, page in enumerate(pages):

        text = pytesseract.image_to_string(page)

        result.append(
            {
                "page_number": i+1,
                "text": text
            }
        )

    return result