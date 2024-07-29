from flask import Flask, request, redirect, url_for, render_template, flash
import os
from email_extractor import extract_emails_from_pdf
from google_sheet import save_emails_to_sheet, delete_emails_from_sheet

app = Flask(__name__)
app.secret_key = 'supersecretkey'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        flash('No files part')
        return redirect(url_for('upload_form'))
    files = request.files.getlist('files')
    all_emails = []
    for file in files:
        if file.filename == '':
            continue
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            emails = extract_emails_from_pdf(filepath)
            all_emails.extend(emails)
    save_emails_to_sheet(all_emails)
    return render_template('upload_complete.html', emails=all_emails)

@app.route('/delete_emails', methods=['POST'])
def delete_emails():
    emails = request.form.getlist('emails')
    if emails:
        delete_emails_from_sheet(emails)
    return redirect(url_for('upload_form'))

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
