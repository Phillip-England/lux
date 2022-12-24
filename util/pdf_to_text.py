import PyPDF2

def pdf_to_text(pdf_file):
  with open(pdf_file, 'rb') as file:
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(pdf.pages)):
      page_text = pdf.pages[page].extract_text()
      text += page_text
    return text.split()