from PyPDF2 import PdfFileReader
from pathlib import Path


pdf_path = (r"chapter 14 working with PDF\Pride_and_Prejudice.pdf")
output_file_path = r"chapter 14 working with PDF\Pride_and_Prejudice.txt"

pdf = PdfFileReader(pdf_path)


with open(output_file_path, 'w') as output_file:
    title = pdf.documentInfo.title
    num_pages = pdf.getNumPages()
    output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")

    for page in pdf.pages:
        text = page.extractText()
        output_file.write(text)


'''
first_page = pdf.getPage(0)
print(first_page.extractText())



for page in pdf.pages:
    print(page.extractText())  # prints the whole book
'''
