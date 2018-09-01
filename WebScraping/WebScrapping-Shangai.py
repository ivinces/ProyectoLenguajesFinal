# - * - coding: UTF- 8 - * - o # codificación = UTF-8
from bs4 import BeautifulSoup
import requests
import csv
import os

def busquedatags(url,tagtx,carpeta):#shangai
    req = requests.get(url)

    status_code = req.status_code
    if status_code == 200:

        html = BeautifulSoup(req.text, "html.parser")
        myData = []

        cont=1
        entradas = html.find_all('tr', {'class': 'bgfd'}) #principal universidad
        for i,entrada in enumerate(entradas):

            universidad= entrada.find('a', {'target': '_blank'})
            if universidad!=None:
                universidadtx=str(universidad.getText().encode('utf-8')).split("'")[1]
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
                myData.append(str(cont2)+","+universidadtx)
                cont2+=2
            #else:
            #   universidadtx=""

            if(cont2>100):
                break

    else:
        print ("Status Code %d" % status_code)


    archivo=tagtx.strip(' ')
    myFile = open("../Procesamiento/procesamiento/Scraping/Shangai/"+carpeta+"/"+archivo+".csv", 'w')
    for linea in myData:
        myFile.write(linea+"\n")

URLMundial=["Mundo-http://www.shanghairanking.com/es/ARWU2015.html"]

URLArea =["Matematicas-http://www.shanghairanking.com/es/SubjectMathematics2015.html"
        ,"Fisica-http://www.shanghairanking.com/es/SubjectPhysics2015.html","Quimica-http://www.shanghairanking.com/es/SubjectChemistry2015.html",
          "Computacion-http://www.shanghairanking.com/es/SubjectCS2015.html","Economia-http://www.shanghairanking.com/es/SubjectEcoBus2015.html"
          ,"Science-http://www.shanghairanking.com/es/FieldSCI2015.html","Ingenieria-http://www.shanghairanking.com/es/FieldENG2015.html",
          "Medicina-http://www.shanghairanking.com/es/FieldMED2015.html","Sociales-http://www.shanghairanking.com/es/FieldSOC2015.html"]

URLAnios=["http://www.shanghairanking.com/es/ARWU2015.html","http://www.shanghairanking.com/es/ARWU2014.html",
         "http://www.shanghairanking.com/es/ARWU2013.html","http://www.shanghairanking.com/es/ARWU2012.html",
         "http://www.shanghairanking.com/es/ARWU2011.html","http://www.shanghairanking.com/es/ARWU2010.html",
         "http://www.shanghairanking.com/es/ARWU2009.html","http://www.shanghairanking.com/es/ARWU2008.html",
         "http://www.shanghairanking.com/es/ARWU2007.html","http://www.shanghairanking.com/es/ARWU2006.html"]

if(os.path.exists("../Procesamiento/procesamiento/Scraping")==False):
    os.mkdir("../Procesamiento/procesamiento/Scraping")

if(os.path.exists("../Procesamiento/procesamiento/Scraping/Shangai")==False):
    os.mkdir("../Procesamiento/procesamiento/Scraping/Shangai")

if(os.path.exists("../Procesamiento/procesamiento/Scraping/Shangai/Mundial")):
    for i in URLMundial:
        l=i.split("-")
        tag=l[0]
        url=l[1]
        busquedatags(url,tag,"Mundial")
else:
    os.mkdir("../Procesamiento/procesamiento/Scraping/Shangai/Mundial")
    for i in URLMundial:
        l=i.split("-")
        tag=l[0]
        url=l[1]
        busquedatags(url,tag,"Mundial")

if(os.path.exists("../Procesamiento/procesamiento/Scraping/Shangai/Area")):
    for i in URLArea:
        l=i.split("-")
        tag=l[0]
        url=l[1]
        busquedatags(url,tag,"Area")
else:
    os.mkdir("../Procesamiento/procesamiento/Scraping/Shangai/Area")
    for i in URLArea:
        l=i.split("-")
        tag=l[0]
        url=l[1]
        busquedatags(url,tag,"Area")
if(os.path.exists("../Procesamiento/procesamiento/Scraping/Shangai/Anios")):
    for i in URLAnios:
        anio=str(i.split("ARWU")[1].split(".html")[0])
        busquedatags(i,anio,"Anios")
else:
    os.mkdir("../Procesamiento/procesamiento/Scraping/Shangai/Anios")
    for i in URLAnios:
        anio=str(i.split("ARWU")[1].split(".html")[0])
        busquedatags(i,anio,"Anios")

