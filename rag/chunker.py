import re
import pdfplumber
from models.chunk import Chunk
import logging
import fitz
from rag.ocr_reader import extract_text_ocr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SECTION_PATTERN = re.compile(
    r"^(?:SECTION\s+)?(\d+(?:\.\d+)?)\s*(?:[—\-\.])?\s+([A-Za-z].+)$",
    re.IGNORECASE
)


class ContractChunker:

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_pages(self):

        doc = fitz.open(self.pdf_path)

        pages = []

        total_chars = 0

        for i, page in enumerate(doc):

            text = page.get_text()

            total_chars += len(text)

            pages.append(
                {
                    "page_number": i+1,
                    "text": text
                }
            )

        # fallback to OCR
        if total_chars < 100:
            print("No text layer detected. Using OCR...")
            pages = extract_text_ocr(self.pdf_path)

        return pages

    def create_chunks(self):
        pages = self.extract_pages()

        chunks = []

        current_section_number = "Unknown"
        current_section_title = "Unknown"
        current_text = ""
        current_page = 1

        for page in pages:

            lines = page["text"].split("\n")

            for line in lines:
                logger.debug(
                    f"New section: {current_section_number} {current_section_title}"
                )

                line = line.strip()

                match = SECTION_PATTERN.match(line)

                if match:
                    # save previous section
                    if current_text.strip():
                        chunks.append(
                            Chunk(
                                text=current_text.strip(),
                                section_number=current_section_number,
                                section_title=current_section_title,
                                page_number=current_page,
                            )
                        )

                    current_section_number = match.group(1)
                    current_section_number = match.group(1)
                    current_section_title = match.group(2)
                    current_text = ""
                    current_page = page["page_number"]

                else:
                    current_text += line + "\n"

        # last chunk
        if current_text.strip():
            chunks.append(
                Chunk(
                    text=current_text.strip(),
                    section_number=current_section_number,
                    section_title=current_section_title,
                    page_number=current_page,
                )
            )
        logger.info(f"Created {len(chunks)} semantic chunks")
        return chunks
