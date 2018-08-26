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

        entrada3=html.find_all('div', {'id': 'content'})  #shangai
        for i, entrada4 in enumerate(entrada3):
            tag=entrada4.find('div', {'id': 'rankingarea'})
            if tag!=None:
                tagtx=tag.getText()+"-shangai"
            else:
                tagtx="shangai"


        entrada6=html.find_all('div', {'class': 'pane-content'})  #qs
        for i, entrada7 in (entrada6):
            tag=entrada7.find('div', {'class': 'image-text'})
            if tag!=None:
                tagtx=tag.getText()+"-QS"
            else:
                tagtx="QS"

        entradas = html.find_all('div', {'id': 'content'}) #principal universidad
        for i, entrada in enumerate(entradas):

            universidad= entrada.find('a', {'target': '_blank'})
            if universidad!=None:
                universidadtx=universidad.getText()
            else:
                universidadtx=""

            myData.append(str(i)+","+universidadtx)


        entradas5 = html.find_all('div', {'class': 'dataTables_scrollBody'}) #principal universidad
        for i, entrada in enumerate(entradas5):

            universidad= entrada.find('td', {'class': 'uni'})
            if universidad!=None:
                universidadtx=universidad.getText()
            else:
                universidadtx=""

            myData.append(str(i)+","+universidadtx)

    else:
        print ("Status Code %d" % status_code)


    ar=tagtx.strip(' ')

    myFile = open("../Procesamiento/Scraping/"+ar+".csv", 'w')
    for linea in myData:
        myFile.write(linea+"\n")



URLtags =["http://www.webometrics.info/es/world"]

for i in URLtags:
    busquedatags(i)



