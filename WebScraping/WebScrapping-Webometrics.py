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
                tagtx=tag.getText().replace("/","-")
            else:
                tagtx=""

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

    myFile = open("../Procesamiento/Scraping/Webometrics/"+ar+".csv", 'w')
    for linea in myData:
        myFile.write(linea+"\n")



URLtags =["http://www.webometrics.info/es/world","http://www.webometrics.info/es/Americas","http://www.webometrics.info/es/Americas/North_America"
          ,"http://www.webometrics.info/es/Americas/USA","http://www.webometrics.info/es/Americas/Latin_America","http://www.webometrics.info/es/Americas/Caribbean",
          "http://www.webometrics.info/es/Asia_Pacifico","http://www.webometrics.info/es/Asia_Pacifico/Asia_incl_ME","http://www.webometrics.info/es/Asia_Pacifico/Middle_East"
          ,"http://www.webometrics.info/es/Asia_Pacifico/South%20Asia","http://www.webometrics.info/es/Asia_Pacifico/South%20East%20Asia","http://www.webometrics.info/es/Asia_Pacifico/Oceania",
          "http://www.webometrics.info/es/Ranking_Europe","http://www.webometrics.info/es/Ranking_africa","http://www.webometrics.info/es/Arab_world",
          "http://www.webometrics.info/es/North_america_es/Estados%20Unidos%20de%20Am%C3%A9rica","http://www.webometrics.info/es/North_america_es/M%C3%A9xico",
          "http://www.webometrics.info/es/North_america_es/Canad%C3%A1","http://www.webometrics.info/es/Latin_America_es/Ecuador","http://www.webometrics.info/es/Latin_America_es/Brasil"
          ,"http://www.webometrics.info/es/Latin_America_es/Argentina","http://www.webometrics.info/es/Latin_America_es/Chile","http://www.webometrics.info/es/Europe_es/Alemania",
          "http://www.webometrics.info/es/Europe_es/Espa%C3%B1a","http://www.webometrics.info/es/Europe_es/Francia","http://www.webometrics.info/es/Europe_es/Italia",
          "http://www.webometrics.info/es/Europe_es/Rusia%20","http://www.webometrics.info/es/Asia_es/China%20","http://www.webometrics.info/es/Asia_es/Corea%20del%20Sur",
          "http://www.webometrics.info/es/Asia_es/Jap%C3%B3n","http://www.webometrics.info/es/Asia_es/Tailandia","http://www.webometrics.info/es/aw_es/Emiratos%20%C3%81rabes%20Unidos",
          "http://www.webometrics.info/es/aw_es/Egipto","http://www.webometrics.info/es/Oceania_es/Australia","http://www.webometrics.info/es/Oceania_es/Nueva%20Zelanda"]

for i in URLtags:
    busquedatags(i)



