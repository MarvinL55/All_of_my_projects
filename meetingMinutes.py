import PyPDF2
pdfFileObj = open('C:\\Users\\marvi\\Downloads\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()

pdfFileObj.close()