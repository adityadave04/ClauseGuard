# rag/ocr_reader.py

from pdf2image import convert_from_path
import pytesseract


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_ocr(pdf_path):

    pages = convert_from_path(
    pdf_path,
    poppler_path=r"C:\Users\adity\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"
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