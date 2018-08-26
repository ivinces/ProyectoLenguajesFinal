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


        entrada2= html.find_all('div', {'id': 'tabs'})
        for i, entrada1 in enumerate(entrada2):
            tag=entrada1.find('a', {'class': 'youarehere is-selected '})
            if tag!=None:
                tagtx=tag.getText()
            else:
                tagtx=""


        entrada3=html.find_all('div', {'id': 'explore-tags'})
        for i, entrada4 in enumerate(entrada3):
            tag=entrada4.find('a', {'class': 'post-tag selected no-tag-menu'})
            if tag!=None:
                tagtx=tag.getText()
            else:
                tagtx=""

        entradas = html.find_all('div', {'class': 'question-summary narrow'})
        for i, entrada in enumerate(entradas):

            tema= entrada.find('a', {'class': 'question-hyperlink'})
            if tema!=None:
                tematx=tema.getText()
            else:
                tematx=""

            votos = entrada.find('div', {'class': 'votes'})
            votostx = votos.getText().replace('\n',' ')

            respuestas = entrada.find('div', {'class': 'status answered'})
            if respuestas!=None:
                respuestastx= respuestas.getText().replace('\n',' ')
            else:
                respuestastx=" 0 respuestas"


            vistas = entrada.find('div', {'class': 'views'}).getText().replace('\n',' ')


            myData.append(tematx+"--"+votostx+"--"+respuestastx+"--"+vistas)


    else:
        print ("Status Code %d" % status_code)


    ar=tagtx.strip(' ')

    myFile = open(ar.replace('\n','').replace(' ','').replace('\r','')+'.csv', 'w')
    for linea in myData:
        myFile.write(linea+"\n")



URLtags =["https://es.stackoverflow.com/?tab=featured","https://es.stackoverflow.com/?tab=active","https://es.stackoverflow.com/?tab=hot",
      "https://es.stackoverflow.com/?tab=week","https://es.stackoverflow.com/?tab=month","https://es.stackoverflow.com/?tags=php",
      "https://es.stackoverflow.com/?tags=javascript","https://es.stackoverflow.com/?tags=java","https://es.stackoverflow.com/?tags=android",
      "https://es.stackoverflow.com/?tags=html","https://es.stackoverflow.com/?tags=c%23","https://es.stackoverflow.com/?tags=jquery",
      "https://es.stackoverflow.com/?tags=python","https://es.stackoverflow.com/?tags=android-studio"]

for i in URLtags:
    busquedatags(i)



