import json
import os
from os.path import join
import pandas as pd

df_sigarette = pd.read_excel("elenco_sigarette.xlsx")

# custom_header = ['codice aams', 'nome', 'confez', '€/kg conv', 'prezzo']
df_codice_aams = df_sigarette["codice aams"].values.tolist()
df_nome = df_sigarette["nome"].values.tolist()
df_conv = df_sigarette["€/kg conv"].values.tolist()
df_prezzo = df_sigarette["prezzo"].values.tolist()

path = "sigarette.json"

dictionary = {
  "lista_sigarette": []
  }
with open(path, "w+") as outfile:
  json.dump(dictionary, outfile)

with open(path, "r") as jsonFile:
  elenco = json.load(jsonFile)

for (codice, nome, conv, prezzo) in zip(df_codice_aams, df_nome, df_conv, df_prezzo):
  elenco['lista_sigarette'].append({
  "nome": nome,
  "codice_aams": codice,
  "prezzo": prezzo,
  "prezzo_conv": conv,
  "alias": ["", "", "", "", "", ""],
  "barcode": "",
  "barcode_stecca": "",
  "min_kgc": "",
  "categoria": "",
  })
# Aggiungi Pod myblu intense tabaggo 18mg
elenco['lista_sigarette'].append({
  "nome": "my blu intense tobacco 18mg",
  "codice_aams": 4853,
  "prezzo": "Chiedere per sicurezza: 9,00",
  "prezzo_conv": "",
  "alias": ["myblu intense tabacco 18mg - V4853", "myblu intense", "my blu intense", "intense tabacco", "V4853", ""],
  "barcode": "",
  "barcode_stecca": "",
  "min_kgc": "",
  "categoria": "",
  })

with open(path, "r+") as jsonFile:
  json.dump(elenco, jsonFile)

print("-- FINE --")