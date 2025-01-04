import os
from extractor import extract_text_from_image, extract_text_from_pdf, extract_menu_items


def load_files(directory):
    """Load all image and PDF files from the directory."""
    image_files = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith((".jpg", ".jpeg", ".png"))
    ]
    pdf_files = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith(".pdf")
    ]
    return image_files, pdf_files


def process_files(directory):
    """Process all image and PDF files in the directory."""
    image_files, pdf_files = load_files(directory)
    all_menu_items = []

    # Process images
    for file in image_files:
        print(f"Processing image: {file}")
        text = extract_text_from_image(file)
        menu_items = extract_menu_items(text)
        all_menu_items.extend(menu_items)

    # Process PDFs
    for file in pdf_files:
        print(f"Processing PDF: {file}")
        text = extract_text_from_pdf(file)
        menu_items = extract_menu_items(text)
        all_menu_items.extend(menu_items)

    return all_menu_items
