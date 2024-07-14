import fitz
import logging
from io import BytesIO

def extract_text_from_pdf(file_path):
   try:
        text = ''
        # Open the PDF file using PyMuPDF (fitz) from bytes
        doc = fitz.open(stream=BytesIO(file_path), filetype='pdf')
        
        # Extract text from each page
        for page in doc:
            text += page.get_text("text") + '\n'
        
        return text
   except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        raise ValueError(f"Error reading PDF: {e}")

    