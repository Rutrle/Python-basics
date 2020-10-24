from PyPDF2 import PdfFileReader
from pathlib import Path
import os


pdf_path = (r"chapter 14 working with PDF\Pride_and_Prejudice.pdf")


pdf = PdfFileReader(pdf_path)


print(pdf.getNumPages())
print(pdf.documentInfo)  # get's the metadata

print(pdf.documentInfo.title)
