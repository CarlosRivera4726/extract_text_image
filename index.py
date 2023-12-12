import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from markupsafe import escape
from PIL import Image
import pytesseract as pyt
from text_extract import TextExtract

# PATH TO UPLOAD FILES, public folder
UPLOAD_FOLDER = f'C:\\Users\\Public\\Pictures\\'

# Only Images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # path complete
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # save the image befor extract the text 
            file.save(image_path)
            textExtract = TextExtract(image_path)
            extracted_text = textExtract.load_image()
            return "<h3>"+ extracted_text +"</h3>"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file accept="image/*">
      <input type=submit value=Upload>
    </form>
    '''