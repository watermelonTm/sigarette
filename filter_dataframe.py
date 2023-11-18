import pandas as pd
import numpy as np
# importing required modules
import pdfplumber
import os
from os.path import join

# read by default 1st sheet of an excel file
df = pd.read_excel('sig.xlsx')
codici_aams = df["Codice AAMS"].values.tolist()

path = join(os.getcwd(), "pdf_folder/lista_completa.xlsx")
df_raw = pd.read_excel(path)

filtered_raw = list()
for codice in codici_aams:
  check = df_raw[df_raw['Codice'] == str(codice)].values
  if check.size == 5:
    filtered_raw.append(check)
filtered_raw2 = np.vstack(filtered_raw)

## convert your array into a dataframe
result_df = pd.DataFrame(filtered_raw2)

filepath = 'elenco_sigarette.xlsx'
custom_header = ['codice aams', 'nome', 'confez', '€/kg conv', 'prezzo']

if os.path.exists(filepath):
  os.remove(filepath)
  print("Rimozione elenco vecchio")
  result_df.to_excel(filepath, header=custom_header, index=False)
  print("Elenco aggiornato correttamente")
else:
  result_df.to_excel(filepath, header=custom_header, index=False)
  print("Elenco creato correttamente")