import os
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document

# OCR Fallback
import pytesseract
from pdf2image import convert_from_path

def extract_text(file_path):
    text = ""
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".pdf":
            text = pdf_extract_text(file_path)
            # Fallback if text is empty → use OCR
            if not text.strip():
                images = convert_from_path(file_path)
                for img in images:
                    text += pytesseract.image_to_string(img)
        elif ext == ".docx":
            doc = Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"❌ Error extracting text: {e}")

    return text.strip()
