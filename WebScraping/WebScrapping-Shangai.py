# - * - coding: UTF- 8 - * - o # codificación = UTF-8
from bs4 import BeautifulSoup
import requests
import csv

def busquedatags(url,tagtx):
    req = requests.get(url)

    status_code = req.status_code
    if status_code == 200:

        html = BeautifulSoup(req.text, "html.parser")
        valores=[["Tema", "Votos", "Respuestas", "Vistas"]]
        myData = []

        #*entrada3=html.find_all('div', {'id': 'content'})  #shangai
        #for i, entrada4 in enumerate(entrada3):
         #   tag=entrada4.find('div', {'id': 'rankingarea'})
          #  if tag!=None:
           #     tagtx=tag.getText()
            #else:
             #   tagtx=""

        cont=1
        entradas = html.find_all('tr', {'class': 'bgfd'}) #principal universidad
        for i,entrada in enumerate(entradas):

            universidad= entrada.find('a', {'target': '_blank'})
            if universidad!=None:
                universidadtx=str(universidad.getText().encode('utf-8')).split("'")[1]


            else:
                universidadtx=""

            myData.append(str(cont)+","+universidadtx)
            cont+=2
            if(cont>100):
                break



        cont2=2
        entradas2 = html.find_all('tr', {'class': 'bgf5'}) #principal universidad
        for i,entrada2 in enumerate(entradas2):

            universidad= entrada2.find('a', {'target': '_blank'})
            if universidad!=None:
                universidadtx=str(universidad.getText().encode('utf-8')).split("'")[1]


            else:
                universidadtx=""

            myData.append(str(cont2)+","+universidadtx)
            cont2+=2
            if(cont2>100):
                break

    else:
        print ("Status Code %d" % status_code)


    ar=tagtx.strip(' ')

    myFile = open("../Procesamiento/Scraping/Shangai/"+ar+".csv", 'w')
    for linea in myData:
        myFile.write(linea+"\n")



URLtags =["Mundo-http://www.shanghairanking.com/es/ARWU2015.html","Matematicas-http://www.shanghairanking.com/es/SubjectMathematics2015.html"
        ,"Fisica-http://www.shanghairanking.com/es/SubjectPhysics2015.html","Quimica-http://www.shanghairanking.com/es/SubjectChemistry2015.html",
          "Computacion-http://www.shanghairanking.com/es/SubjectCS2015.html","Economia-http://www.shanghairanking.com/es/SubjectEcoBus2015.html"
          ,"Science-http://www.shanghairanking.com/es/FieldSCI2015.html","Ingenieria-http://www.shanghairanking.com/es/FieldENG2015.html",
          "Medicina-http://www.shanghairanking.com/es/FieldMED2015.html","Sociales-http://www.shanghairanking.com/es/FieldSOC2015.html"]

for i in URLtags:
    l=i.split("-")
    tag=l[0]
    url=l[1]
    busquedatags(url,tag)



