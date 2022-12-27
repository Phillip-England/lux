from pdfminer.high_level import extract_pages, extract_text
import PyPDF2

def pdf_to_text(file_path):
  pdf_text = []
  for page_layout in extract_pages(file_path):
    for element in page_layout:
      try:
        text = pdf_text.append(element.get_text())
      except:
        pass
  return pdf_text