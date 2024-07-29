from email_extractor import extract_emails_from_pdf
from google_sheet import save_emails_to_sheet

def main():
    pdf_path = 'E:/Projects/PDFproject/cv.pdf'  # Replace with your PDF file path
    emails = extract_emails_from_pdf(pdf_path)
    save_emails_to_sheet(emails)
    print(f"Extracted emails: {emails}")

if __name__ == "__main__":
    main()
