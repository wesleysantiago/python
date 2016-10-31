
import PyPDF2
import os

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('Documento.doc'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('arquivo_pronto.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()