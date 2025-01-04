import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re


def extract_text_from_image(file_path):
    """Extract text from an image file using Tesseract OCR."""
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)


def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using Tesseract OCR."""
    pages = convert_from_path(file_path)
    text = " ".join([pytesseract.image_to_string(page) for page in pages])
    return text


def clean_item(item):
    """Clean and normalize item names."""
    item = re.sub(r'[^\w\s]', '', item)  # Remove special characters
    item = re.sub(r'\s+', ' ', item)  # Replace multiple spaces with a single space
    return item.strip()


def validate_price(price):
    """Validate and normalize price."""
    try:
        price = float(price)
        return price if 0 < price < 10000 else None  # Valid price range
    except ValueError:
        return None

def extract_menu_items(text):
    """Extract menu items, descriptions, and prices using regex."""
    menu_items = []
    lines = text.split("\n")
    for line in lines:
        # Regex to capture item, optional description, and price
        match = re.match(r"(.*?)(?:\s+-\s+(.*?))?\s+\$?(\d+(\.\d{2})?)$", line.strip())
        if match:
            item, description, price = match.groups()[0], match.groups()[1], match.groups()[2]
            
            # Clean and normalize data
            item = clean_item(item)
            description = clean_item(description) if description else ""
            price = validate_price(price)
            
            # Exclude rows where item is purely numeric
            if not item.isdigit() and not re.match(r'^\d+(\s+\d+)*$', item) and price is not None:
                menu_items.append({"Item": item, "Description": description, "Price": price})
    return menu_items
