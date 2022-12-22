import PyPDF2

def pdf_to_text(pdf_file):
  with open(pdf_file, 'rb') as file:
    pdf = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf.numPages):
      page_text = pdf.getPage(page).extractText()
      text += page_text
    return text.split()