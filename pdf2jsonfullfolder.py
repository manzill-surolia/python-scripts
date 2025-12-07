import json
from pathlib import Path
from pypdf import PdfReader

# ======== CONFIGURE THESE TWO PATHS ========
# Folder that contains your PDFs (searched recursively)
INPUT_FOLDER_PATH = r"c:\Users\...."

# Folder where JSON files will be written (will be created if missing)
OUTPUT_FOLDER_PATH = r"c:\Users\...."
# ==========================================


def extract_text_from_pdf(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    texts = []
    for page in reader.pages:
        text = page.extract_text() or ""
        texts.append(text)
    return "\n".join(texts).strip()


def convert_pdfs_in_folder(input_folder: Path, output_folder: Path) -> None:
    if not input_folder.exists() or not input_folder.is_dir():
        raise ValueError(f"Input folder does not exist or is not a directory: {input_folder}")

    output_folder.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_folder.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files under {input_folder}")

    for pdf_path in pdf_files:
        try:
            text = extract_text_from_pdf(pdf_path)
        except Exception as e:
            print(f"Failed to read {pdf_path}: {e}")
            continue

        # Keep subfolder structure under the output folder
        relative = pdf_path.relative_to(input_folder)
        json_name = relative.with_suffix(".json")
        json_path = output_folder / json_name

        json_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "source_pdf": str(pdf_path),
            "relative_path": str(relative),
            "text": text,
        }

        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {json_path}")


if __name__ == "__main__":
    convert_pdfs_in_folder(Path(INPUT_FOLDER_PATH), Path(OUTPUT_FOLDER_PATH))
    print(f"Done. JSON files are in: {OUTPUT_FOLDER_PATH}")
