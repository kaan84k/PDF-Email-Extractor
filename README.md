# **PDF Email Extractor and Google Sheets Integration**

This project is a web application that allows users to upload PDF files, extract emails from the content, and save the emails to a Google Sheet. Additionally, users can manage the extracted emails by selecting and deleting specific entries.

## **Getting Started**

Follow these instructions to set up and run the project on your local machine.

### **Prerequisites**

Before you begin, ensure you have the following software installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip**: Comes with Python, but ensure it's up-to-date:
  ```bash
  pip install --upgrade pip
  ```
  
### **1. Install Dependencies**

Install the necessary Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **2. Set Up Google API Credentials**

To use Google Sheets API, you need to set up credentials:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the Google Sheets API and Google Drive API.
4. Create credentials for a desktop application or a web application and download the `credentials.json` file.
5. Place the `credentials.json` file in the root directory of your project.

### **3. Run the Application**

Start the Flask web server:

```bash
python app.py
```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### **4. Upload PDFs and Manage Emails**

- **Upload PDFs**: Use the web interface to upload one or more PDF files.
- **View Extracted Emails**: The application will display extracted emails after processing.
- **Manage Emails**: Select emails to remove from the Google Sheet if necessary.

### **5. Contributing**

Feel free to fork the project, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---
