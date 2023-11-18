import pdfplumber
import json
import os
from os.path import join

path = join(os.getcwd(), "pdf_folder/lista_completa.pdf")

tabella_sigarette = []
with pdfplumber.open(path) as pdf:
  for numero, pagina in enumerate(pdf.pages):
    tabella = pdf.pages[numero].extract_table()
    tabella_sigarette.extend(tabella)

print(tabella_sigarette)


with open("sigarette.json", "r") as jsonFile:
  elenco = json.load(jsonFile)

modifiche_prezzo = []

# Aggiorna prezzo sigaretta se esiste nell'elenco pdf
for sigaretta in elenco['lista_sigarette']:
  for x in tabella_sigarette:
    if sigaretta["codice_aams"] in x:
      prezzo_adm = x[-1]
      if prezzo_adm != sigaretta["prezzo"]:
        sigaretta["prezzo"] = prezzo_adm
        modifiche_prezzo.append(f'cod aams: {sigaretta["codice_aams"]} - nome: {sigaretta["nome"]}')

print(modifiche_prezzo)

with open("sigarette.json", "w") as jsonFile:
    json.dump(elenco, jsonFile)

print("-- FINE --")