import requests
import re
from bs4 import BeautifulSoup
from src.date import *

URL_CALENDARIO_LIGA = 'https://www.cariverplate.com.ar/calendario-de-partidos'
URL_NOTICIAS_ENTRADAS_LIGA = 'https://www.cariverplate.com.ar/noticias-de-entradas'

def getProxPartido():
    soup = getSoup(URL_CALENDARIO_LIGA)
    eMeses = soup.find_all(class_ = "l_calendario")

    seEncontroProxPartido = False
    proxPartidos = []
    for eMes in eMeses:
        ePartidos = eMes.find_all('li')
        for ePartido in ePartidos:
            if(riverEsLocal(ePartido) and estaConfirmado(ePartido)):
                proxPartidos.append({
                    'rival': getRival(ePartido),
                    'fecha': getFecha(ePartido)
                })

    proxPartido = proxPartidos[0]
    print(proxPartido)
    return proxPartido

def getSoup(url):
    page = requests.get(url).content
    return BeautifulSoup(page, 'html.parser')

def riverEsLocal(ePartido):
    titulo = getTitulo(ePartido)
    return titulo.find('River Plate', 0, 11) == 0

def getTitulo(ePartido):
    return ePartido.find('a')['title']

def getRival(ePartido):
    titulo = getTitulo(ePartido)
    return titulo[16:]

def getTextoFecha(ePartido):
    return ePartido.find('p').getText()

def estaConfirmado(ePartido):
    texto = getTextoFecha(ePartido)
    return 'A confirmar' not in texto

def getFecha(ePartido):
    texto = getTextoFecha(ePartido)
    match = re.search(r"(\d{2}/\d{2}/\d{4}) - (\d{2}.\d{2})", texto)
    fmt = match.group(1) + ' ' + match.group(2).replace('.', ":")+ ':00'
    datetimePartido = datetime.strptime(fmt, '%d/%m/%Y %H:%M:%S')
    return datetimePartido



