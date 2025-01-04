# Menu Data Extraction Project

## Overview
This project extracts structured data (menu items, descriptions, and prices) from restaurant menu files in PDF and image formats. The extracted data is saved in a CSV file for easy use in applications like inventory systems, analytics, or digitized menu services.

## Objectives
1. Process menu files (images and PDFs) located in the `./data` folder.
2. Extract relevant data fields:
   - **Item Name**
   - **Description (if available)**
   - **Price**
3. Save the extracted data into a `CSV` file.

## Steps Performed
1. **Loading Files**:
   - Images (`.jpg`, `.jpeg`) and PDFs (`.pdf`) are loaded from the `./data` directory.

2. **Processing**:
   - **Images**: OCR (Optical Character Recognition) is performed using Tesseract to extract text.
   - **PDFs**: Text is extracted directly or through OCR (for image-based PDFs).

3. **Data Extraction**:
   - Using regular expressions to parse text and identify menu items, descriptions, and prices.

4. **Saving Results**:
   - The extracted data is saved in `processed_data.csv` for further use.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure Tesseract OCR is installed and configured. Refer to [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract).

3. Run the main script:
   ```bash
   python main.py
   ```

4. Find the results in the `processed_data.csv` file.

## Key Libraries Used
- **pytesseract**: For OCR processing.
- **pdf2image**: To convert PDF pages to images for OCR.
- **Pillow**: For image handling.
- **pandas**: For saving extracted data in CSV format.

## Output
The output file, `processed_data.csv`, contains:
- **Item**: Name of the menu item.
- **Description**: A brief description (if available).
- **Price**: Price of the menu item.

## Notes
- Ensure all menu files are placed in the `./data` folder before running the script.
- Tesseract OCR must be installed and added to the system PATH for the script to work correctly.

