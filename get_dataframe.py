import pandas as pd
import pdfplumber
import os
from os.path import join

tabella_sigarette = list()
path = join(os.getcwd(), "pdf_folder/lista_completa.pdf")
with pdfplumber.open(path) as pdf:
  for numero, pagina in enumerate(pdf.pages):
    tabella = pdf.pages[numero].extract_table()
    tabella_sigarette.extend(tabella)

header=0
columns=list()
for column in tabella_sigarette[header]:
  if column!=None and len(column)>1:
    columns.append(column)

df=pd.DataFrame(tabella_sigarette)
df.columns=columns
filtered = df.drop_duplicates()

filepath = "lista_completa.xlsx"
# custom_header = ['Codice', 'Nome', 'Conf.ne', '€/kg conv.le', 'Prezzo']
if os.path.exists(filepath):
  os.remove(filepath)
  print("Rimozione vecchio excel")
  # filtered.to_excel(path.split('.')[0]+'.xlsx', header=custom_header, index=False)
  filtered.to_excel(path.split('.')[0]+'.xlsx', header=False, index=False)
  print("File excel aggiornato con successo")
else:
  filtered.to_excel(path.split('.')[0]+'.xlsx', header=False, index=False)
  print("File excel creato con successo")
