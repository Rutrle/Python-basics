from PyPDF2 import PdfFileReader
from pathlib import Path


pdf_path = (r"chapter 14 working with PDF\zen.pdf")


pdf = PdfFileReader(pdf_path)

print(pdf.getNumPages())

first_page = pdf.getPage(0)

print(first_page.extractText())
