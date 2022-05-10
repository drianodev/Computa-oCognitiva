import PyPDF2
import re

# Abre o arquivo pdf 
arquivo = "texto1.pdf"
pdf_file = open(arquivo, 'rb')

#Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()

#lê a primeira página completa
page = read_pdf.getPage(0)

#extrai apenas o texto
page_content = page.extractText()

# faz a junção das linhas 
parsed = ''.join(page_content)

# remove as quebras de linha
parsed = re.sub('\n', '', parsed)
print(parsed)