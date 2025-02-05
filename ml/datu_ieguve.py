#iegut daudz masinu datus no ss.lv
import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time

URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
DATI = "ml/dati/"
LAPAS = "ml/lapas/"

def saglaba_lapu(url, nosaukums):
    iegutais = requests.get(url)
    print(iegutais.status_code)
    if iegutais.status_code == 200:
        with open(nosaukums, "w", encoding="utf-8") as f:
            f.write(iegutais.text)
        return
    
# saglaba_lapu(URL, LAPAS+"pirma.html")

def saglaba_visas_lapas(skaits):
    for i in range(1, skaits+1):
        saglaba_lapu(f"{URL}page{i}.html", f"{LAPAS}lapa{i}.html")
        time.sleep(0.5)
    return

# saglaba_visas_lapas(5)

def dabut_info(lapa):
    dati = []
    with open(lapa, "r", encoding="utf-8") as f:
        html = f.read()
    zupa = bs(html, "html.parser")
    galvenais = zupa.find(id="page_main")
    tabulas = galvenais.find_all("table")
    rindas = tabulas[2].find_all("tr")
    for rinda in rindas[1:-1]:
        lauki = rinda.find_all("td")
        if len(lauki)<8:
            print("Dīvaina rinda")
            continue
        auto = {}
        auto["sludinajuma_saite"] = lauki[1].find("a")["href"]
        auto["bilde"] = lauki[1].find("img")["src"]
        auto["marka"] = lauki[3].contents
        auto["gads"] = lauki[4].contents
        auto["tilpums"] = lauki[5].contents
        auto["nobraukums"] = lauki[6].contents
        auto["cena"] = lauki[7].contents
        print(auto["marka"])
        dati.append(auto)
    return dati

def saglaba_datus(dati):
    with open(DATI+"sslv.csv", "w", encoding="utf-8") as f:
        lauku_nosaukumi = ["sludinajuma_saite", "bilde", "marka", "gads", "tilpums", "nobraukums", "cena"]
        w = csv.DictWriter(f, fieldnames=lauku_nosaukumi)
        w.writeheader()
        for auto in dati:
            w.writerow(auto) 
    return

# saglaba_datus(dabut_info(LAPAS+"pirma.html"))

def dabut_info_daudz(skaits):
    visi_dati = []
    for i in range(1, skaits+1):
        dati = dabut_info(f"{LAPAS}lapa{i}.html")
        visi_dati += dati
    return visi_dati

saglaba_visas_lapas(250)
info = dabut_info_daudz(250)
saglaba_datus(info)
