import PyPDF2

# Open the PDF file
with open('document.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfFileReader(file)
    # Iterate over each page
    for page in range(reader.numPages):
        # Extract the text from the page
        text = reader.getPage(page).extractText()
        # Print the text
        print(text)
