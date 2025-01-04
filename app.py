from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import pandas as pd
from processor import process_files
import shutil
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = './temp_uploads'
OUTPUT_CSV = './processed_data.csv'

# Ensure temporary upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Render the upload form."""
    return render_template('index.html', data=None, show_all=False)

@app.route('/upload', methods=['POST'])
def upload_files():
    """Handle multiple file uploads and process them."""
    if 'files[]' not in request.files:
        return "No files part in the request", 400

    files = request.files.getlist('files[]')
    if len(files) == 0 or files[0].filename == '':
        return "No files selected", 400

    # Create a unique temporary folder for this session
    session_folder = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()))
    os.makedirs(session_folder, exist_ok=True)

    # Save uploaded files to the session folder
    for file in files:
        file.save(os.path.join(session_folder, file.filename))

    # Process the uploaded files
    new_data = process_files(session_folder)

    # Remove the temporary folder after processing
    shutil.rmtree(session_folder)

    # Create a DataFrame for the UI
    data_frame = pd.DataFrame(new_data)

    # Save the processed data as a temporary CSV file
    data_frame.to_csv(OUTPUT_CSV, index=False)

    # Show the processed data on the UI
    return render_template(
        'index.html',
        data=data_frame.to_dict(orient='records')[:30],  # Only show the first 30 rows initially
        show_all=False,
        download_link=url_for('download_file'),
    )

@app.route('/show_all')
def show_all():
    """Show all rows in the processed CSV file."""
    if os.path.exists(OUTPUT_CSV):
        data_frame = pd.read_csv(OUTPUT_CSV)
        return render_template(
            'index.html',
            data=data_frame.to_dict(orient='records'),
            show_all=True,
            download_link=url_for('download_file'),
        )
    else:
        return redirect(url_for('index'))

@app.route('/download')
def download_file():
    """Provide the processed CSV file for download."""
    if os.path.exists(OUTPUT_CSV):
        return send_file(OUTPUT_CSV, as_attachment=True)
    else:
        return "No processed CSV file available", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
