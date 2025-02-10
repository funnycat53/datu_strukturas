import pandas as pd
import re
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np

CSV_FAILS = "ml/dati/sslv.csv"

def attirit(value):

    if isinstance(value, str):
        value = re.sub(r"[\[\]',]", "", value)
    match = re.search(r"[\d\.]+", value)
    if match:
        return match.group(0)
    return None

def datu_sagatave(csv_file):
    dati = pd.read_csv(csv_file, encoding="utf-8")

    for col in ['nobraukums', 'gads', 'tilpums', 'cena']:
        dati[col] = dati[col].apply(lambda x: attirit(str(x)))

    dati['nobraukums'] = pd.to_numeric(dati['nobraukums'], errors='coerce')
    dati['gads'] = pd.to_numeric(dati['gads'], errors='coerce')
    dati['tilpums'] = pd.to_numeric(dati['tilpums'], errors='coerce')
    dati['cena'] = pd.to_numeric(dati['cena'], errors='coerce')

    dati = dati.dropna(subset=['nobraukums', 'gads', 'tilpums', 'cena'])

    return dati

def modela_trenesana(csv_file):
    dati = datu_sagatave(csv_file)
    
    X = dati[['nobraukums', 'gads', 'tilpums']]
    y = dati['cena']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    modelis = RandomForestRegressor(n_estimators=500, random_state=42)
    modelis.fit(X_scaled, y)

    return modelis, scaler

cenas_modelis, scaler = modela_trenesana(CSV_FAILS)

def cenas_noteiksana(mileage, year, engine_volume):

    X_new = np.array([[mileage, year, engine_volume]])
    X_scaled = scaler.transform(X_new)

    noteikta_cena = cenas_modelis.predict(X_scaled)[0]
    
    return max(0, noteikta_cena)  

if __name__ == "__main__":
    mileage_example = 300000
    year_example = 2000
    engine_volume_example = 1.9

    cena = cenas_noteiksana(mileage_example, year_example, engine_volume_example)
    print(f"Prognozētā cena mašīnai ar {mileage_example} km nobraukumu, kura ir {year_example} gada un dzinēja tilpums ir {engine_volume_example}L: {cena:.2f} EUR")
