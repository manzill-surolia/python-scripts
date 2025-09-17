import json
import PyPDF2  # library for reading PDFs

# --- File locations (edit these paths as needed) ---
pdf_file = r"C:\Users\manzill.surolia\Desktop\iso.pdf"   # Input PDF full path
json_file = r"C:\Users\manzill.surolia\Desktop\output.json" # Output JSON full path

# Function to extract PDF text page by page
def pdf_to_json(pdf_file, json_file):
    # Open PDF file
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        
        data = {}
        # Loop through all pages
        for i, page in enumerate(reader.pages, start=1):
            text = page.extract_text()  # extract text from each page
            data[f"page_{i}"] = text.strip() if text else ""
        
        # Save output as JSON
        with open(json_file, "w", encoding="utf-8") as jf:
            json.dump(data, jf, indent=4, ensure_ascii=False)

# --- Example usage ---
pdf_to_json(pdf_file, json_file)
