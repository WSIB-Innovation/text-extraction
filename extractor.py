import fitz
import docx2txt
import json
import os

def extract_text_from_pdf(file_path):
    with fitz.open(file_path) as doc:  # open document
        text = chr(12).join([page.get_text() for page in doc])
        return text

def extract_text_from_docx(file_path):
    text = docx2txt.process(file_path)
    return text

def extract_text(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Determine the extraction method based on the file extension
    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a PDF or DOCX file.")

# Use just the file name since it is in the same directory as the script
file_path = "Accommodations - Heat Stress Products (WSIB Newsletter).pdf"  # File name in the same folder

# Extract the file name without extension
file_name = os.path.splitext(os.path.basename(file_path))[0]

# Extract text from the file
extracted_text = extract_text(file_path)

# Create a dictionary with extracted details
file_data = {
    "name": file_name,
    "text": extracted_text
}

print(json.dumps(file_data, indent=4))