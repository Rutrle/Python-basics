from PyPDF2 import PdfFileWriter


pdf_writer = PdfFileWriter()

page = pdf_writer.addBlankPage(width=72, height=72)

with open(r'..\Python-basics\chapter 14 working with PDF\blank.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)