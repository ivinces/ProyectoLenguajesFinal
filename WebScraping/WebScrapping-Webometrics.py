# - * - coding: UTF- 8 - * - o # codificación = UTF-8
from bs4 import BeautifulSoup
import requests
import csv

def busquedatags(url):
    req = requests.get(url)

    status_code = req.status_code
    if status_code == 200:

        html = BeautifulSoup(req.text, "html.parser")
        valores=[["Tema", "Votos", "Respuestas", "Vistas"]]
        myData = []

        entrada2= html.find_all('div', {'id': 'siteContent'}) #webomwtrics
        for i, entrada1 in enumerate(entrada2):
            tag=entrada1.find('h1', {'id': 'page-title'})
            if tag!=None:
                tagtx=tag.getText()+"-webometrics"
            else:
                tagtx="webometrics"

        cont=1
        entradas = html.find_all('tr', {'class': 'odd'}) #principal universidad
        for i,entrada in enumerate(entradas):

            universidad= entrada.find('a', {'target': '_blank'})
            if universidad!=None:
                universidadtx=str(universidad.getText().encode('utf-8')).split("'")[1]


            else:
                universidadtx=""

            myData.append(str(cont)+","+universidadtx)
            cont+=2



        cont2=2
        entradas2 = html.find_all('tr', {'class': 'even'}) #principal universidad
        for i,entrada2 in enumerate(entradas2):

            universidad= entrada2.find('a', {'target': '_blank'})
            if universidad!=None:
                universidadtx=str(universidad.getText().encode('utf-8')).split("'")[1]


            else:
                universidadtx=""

            myData.append(str(cont2)+","+universidadtx)
            cont2+=2

    else:
        print ("Status Code %d" % status_code)


    ar=tagtx.strip(' ')

    myFile = open("../Procesamiento/Scraping/Webometrics"+ar+".csv", 'w')
    for linea in myData:
        myFile.write(linea+"\n")



URLtags =["http://www.webometrics.info/es/world","http://www.webometrics.info/es/Americas",""]

for i in URLtags:
    busquedatags(i)



