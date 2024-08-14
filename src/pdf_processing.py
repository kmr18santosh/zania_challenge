# src/pdf_processing.py

import fitz  # PyMuPDF
from difflib import get_close_matches

def extract_text_from_pages(pdf_path: str, start_page: int, num_pages: int) -> str:
    """
    Extracts text from a range of pages in the PDF.

    Args:
        pdf_path (str): The path to the PDF file.
        start_page (int): The page number to start extracting text from.
        num_pages (int): The number of pages to extract.

    Returns:
        str: The extracted text from the specified pages.
    """
    try:
        doc = fitz.open(pdf_path)
        end_page = min(start_page + num_pages, doc.page_count)
        text = ""
        for page_num in range(start_page, end_page):
            page = doc.load_page(page_num)
            text += page.get_text("text")
        return text
    except Exception as e:
        print(f"An error occurred while extracting text from page {start_page}: {e}")
        return ""


def get_section_from_toc(pdf_path: str, keyword: str, num_pages: int = 3) -> str:
    """
    Finds the section related to the keyword by using the Table of Contents and extracts text for a given number of pages.

    Args:
        pdf_path (str): The path to the PDF file.
        keyword (str): The keyword to search in the Table of Contents.
        num_pages (int): The number of pages to extract after the section starts.

    Returns:
        str: The text of the relevant section.
    """
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()

    toc_titles = [item[1].lower() for item in toc]
    closest_match = get_close_matches(keyword.lower(), toc_titles, n=1, cutoff=0.4)

    if closest_match:
        for item in toc:
            if closest_match[0] == item[1].lower():
                start_page = item[2] - 1
                return extract_text_from_pages(pdf_path, start_page, num_pages)
    
    return "Relevant section not found."

