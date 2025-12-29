import fitz  # PyMuPDF

def parse_pdf_text(file_path):
    """
    Extract text from a PDF or TXT file
    """
    if file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    # PDF handling
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text




