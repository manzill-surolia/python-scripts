import json
from docx import Document  # library for reading DOCX

# --- File locations (edit these paths as needed) ---
docx_file = r"C:\Users\manzill.surolia\Desktop\resume.docx"    # Input DOCX full path
json_file = r"C:\Users\manzill.surolia\Desktop\output.json" # Output JSON full path

# Function to extract DOCX text paragraph by paragraph
def docx_to_json(docx_file, json_file):
    doc = Document(docx_file)  # open the docx file
    
    data = {}
    # Loop through all paragraphs
    for i, para in enumerate(doc.paragraphs, start=1):
        text = para.text.strip()
        if text:  # skip empty paragraphs
            data[f"para_{i}"] = text
    
    # Save output as JSON
    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(data, jf, indent=4, ensure_ascii=False)

# --- Example usage ---
docx_to_json(docx_file, json_file)
