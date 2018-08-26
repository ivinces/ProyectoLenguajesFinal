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
        titulo=html.find('div', {'class': 'tit'}).getText()
        tabla= html.find_all('table', {'id': 'qs-rankings'}) #webomwtrics

        for i, entrada1 in enumerate(tabla):
            rank=""
            uni=""
            country=""
            if(entrada1.find('tr', {'class': 'odd'})!=None):
                rank=entrada1.find('tr', {'class': 'even'}).find('td', {'class': ' rank'}).find('span', {'class': 'rank '}).getText()
                uni=entrada1.find('tr', {'class': 'even'}).find('td', {'class': ' uni'}).find('a', {'class': 'title'}).getText()
                #country=entrada1.find('tr', {'class': 'even'}).find('td', {'class': ' country'}).find('div', {'class': 'td-wrap'}).getText()

            elif(entrada1.find('tr', {'class': 'even'})!=None):
                rank=entrada1.find('tr', {'class': 'even'}).find('td', {'class': ' rank'}).find('span', {'class': 'rank '}).getText()
                uni=entrada1.find('tr', {'class': 'even'}).find('td', {'class': ' uni'}).find('a', {'class': 'title'}).getText()
                #country=entrada1.find('tr', {'class': 'even'}).find('td', {'class': ' country'}).find('div', {'class': 'td-wrap'}).getText()
            myData.append(str(rank)+","+str(uni))

    else:
        print ("Status Code %d" % status_code)


    ar=titulo.strip(' ')

    myFile = open("../Procesamiento/Scraping/"+ar+".csv", 'w')
    for linea in myData:
        myFile.write(linea+"\n")



URLtags =["https://www.topuniversities.com/university-rankings/university-subject-rankings/2018/life-sciences-medicine"]

for i in URLtags:
    busquedatags(i)



