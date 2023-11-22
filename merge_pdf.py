
# importing required modules
import os
from os.path import join
import pdfplumber
import json
from PyPDF2 import PdfMerger

path = os.chdir(join(os.getcwd(), "pdf_folder"))
pdf_list = [a for a in sorted(os.listdir()) if a.endswith('.pdf') and a != "lista_completa.pdf"]
merger = PdfMerger()

for pdf in pdf_list:
  merger.append(open(pdf, 'rb'))

filepath = "lista_completa.pdf"
if os.path.exists(filepath):
  os.remove(filepath)
  print("Rimozione pdf vecchio")
  with open(filepath, "wb") as fout:
    merger.write(fout)
  print("Pdf aggiornato correttamente")
else:
  with open(filepath, "wb") as fout:
    merger.write(fout)
  print("Pdf creato con successo")