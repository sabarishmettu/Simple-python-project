import PyPDF2

# open the pdf file
pdf_file = open('my_pdf_file.pdf', 'rb')

# create pdf reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# get number of pages
num_pages = pdf_reader.numPages

# extract text from each page
for page_num in range(num_pages):
    page = pdf_reader.getPage(page_num)
    print(page.extractText())

# close the pdf file
pdf_file.close()
