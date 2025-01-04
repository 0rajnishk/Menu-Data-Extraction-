# Menu Data Extraction Project

## Overview
This project extracts structured data (menu items, descriptions, and prices) from restaurant menu files in PDF and image formats. The extracted data is saved in a CSV file for easy use in applications like inventory systems, analytics, or digitized menu services.

## Objectives
1. Process menu files (images and PDFs) through a web-based interface.
2. Extract relevant data fields:
   - **Item Name**
   - **Description (if available)**
   - **Price**
3. Save the extracted data into a `CSV` file that can be downloaded.

## Steps Performed
1. **Uploading Files**:
   - Users can upload multiple files (images and PDFs) through a web interface.

2. **Processing**:
   - **Images**: OCR (Optical Character Recognition) is performed using Tesseract to extract text.
   - **PDFs**: Text is extracted directly or through OCR (for image-based PDFs).

3. **Data Extraction**:
   - Using regular expressions to parse text and identify menu items, descriptions, and prices.

4. **Temporary File Management**:
   - Uploaded files are stored in a temporary directory during processing and removed after use.

5. **Displaying Results**:
   - The processed data is displayed in a table format on the web interface, showing the first 30 rows initially, with an option to view all rows.

6. **Saving Results**:
   - The extracted data is saved in `processed_data.csv` for further use, which can be downloaded directly from the interface.

## Deployment Plan
This project can be deployed using Docker and Docker Compose for scalability and portability. Below are the steps:

### Docker Setup
1. **Dockerfile**:
   - A Dockerfile is used to containerize the application, installing dependencies and setting up the environment.

   ```dockerfile
   FROM python:3.9-slim
   RUN apt-get update && apt-get install -y \
       tesseract-ocr \
       libsm6 libxext6 libxrender-dev \
       && rm -rf /var/lib/apt/lists/*

   WORKDIR /app
   COPY . /app

   RUN pip install --no-cache-dir -r requirements.txt

   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

2. **docker-compose.yml**:
   - Docker Compose is used to manage the application container.

   ```yaml
   version: '3.8'

   services:
     app:
       build:
         context: .
         dockerfile: Dockerfile
       container_name: menu-data-extraction
       ports:
         - "5000:5000"
       volumes:
         - ./data:/app/data  # Persistent storage for uploaded files
         - ./temp_uploads:/app/temp_uploads  # Temporary storage for processing
       environment:
         - PYTHONUNBUFFERED=1
       restart: always
   ```

3. **Build and Run**:
   - Build and start the application using:
     ```bash
     docker-compose up --build -d
     ```

   - Access the application at `http://localhost:5000`.

4. **Stopping the Application**:
   - Stop the running containers with:
     ```bash
     docker-compose down
     ```

## Usage
1. Install dependencies locally (optional):
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure Tesseract OCR is installed and configured. Refer to [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract).

3. Run the Flask application locally (optional):
   ```bash
   python app.py
   ```

4. Access the web interface at `http://localhost:5000` to:
   - Upload menu files (PDFs or images).
   - View extracted data in a table format.
   - Download the processed CSV file.

## Key Libraries Used
- **pytesseract**: For OCR processing.
- **pdf2image**: To convert PDF pages to images for OCR.
- **Pillow**: For image handling.
- **pandas**: For saving and manipulating extracted data.
- **Flask**: For building the web interface.

## Output
The output file, `processed_data.csv`, contains:
- **Item**: Name of the menu item.
- **Description**: A brief description (if available).
- **Price**: Price of the menu item.

The data is displayed in the web interface and is available for download.

## Notes
- Uploaded files are stored temporarily in the `temp_uploads` directory and removed after processing.
- The application is containerized for easy deployment and scalability.
- Deployment instructions are provided for both local and Docker-based environments.
