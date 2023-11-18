import json
import pandas as pd

df_json = pd.read_excel("completa_json.xlsx")

# completa_json = ['aams', '#nome#nonserve', 'alias', 'unita', 'barcode', 'barcode_stecca']
dfj_aams = df_json["aams"].values.tolist()

dfj_alias1 = df_json["alias"].values.tolist()
dfj_barcode = df_json["barcode"].values.tolist()
dfj_barcode_stecca = df_json["barcode stecca"].values.tolist()
dfj_min_kgc = df_json["unita"].values.tolist()
dfj_categoria = df_json["categoria"].values.tolist()

with open("sigarette.json", "r") as jsonFile:
  elenco = json.load(jsonFile)

# Aggiorna prezzo sigaretta se esiste nell'elenco pdf
for sigaretta in elenco['lista_sigarette']:
  for (aams, alias, barcode, barcode_stecca, min_kgc, categoria) in zip(dfj_aams, dfj_alias1, dfj_barcode, dfj_barcode_stecca, dfj_min_kgc, dfj_categoria):
    if sigaretta["codice_aams"] == aams:
      sigaretta["alias"][0] = alias if not pd.isna(alias) else ""
      sigaretta["barcode"] = barcode if not pd.isna(barcode) else ""
      sigaretta["barcode_stecca"] = barcode_stecca if not pd.isna(barcode_stecca) else ""
      sigaretta["min_kgc"] = min_kgc if not pd.isna(min_kgc) else ""
      sigaretta["categoria"] = categoria if not pd.isna(categoria) else ""

with open("sigarette.json", "w") as jsonFile:
    json.dump(elenco, jsonFile)

print("-- FINE MODIFICHE --")
