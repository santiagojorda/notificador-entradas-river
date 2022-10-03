import requests
import re
from bs4 import BeautifulSoup
from src.date import *

URL_RIVER = 'https://www.cariverplate.com.ar/'
URL_CALENDARIO_LIGA = 'https://www.cariverplate.com.ar/calendario-de-partidos'
URL_NOTICIAS_ENTRADAS_LIGA = 'https://www.cariverplate.com.ar/noticias-de-entradas'



def getSoup(url):
    page = requests.get(url).content
    return BeautifulSoup(page, 'html.parser')

# ENTRADAS

def getUltimoCartelDeEntradas():
    soup = getSoup(URL_NOTICIAS_ENTRADAS_LIGA)
    ePrincipal = soup.find(id = "principal")
    eFigure = ePrincipal.find('figure')
    eTexto = eFigure.find('p').getText()
    eLink = eFigure.find('a')
    return {
        'titulo': eLink['title'],
        'texto': eTexto,
        'url': URL_RIVER + eLink['href']
    }


# PROX PARTIDO

def getProxPartido():
    soup = getSoup(URL_CALENDARIO_LIGA)
    eMeses = soup.find_all(class_ = "l_calendario")

    seEncontroProxPartido = False
    proxPartidos = []
    for eMes in eMeses:
        ePartidos = eMes.find_all('li')
        for ePartido in ePartidos:
            if(esRiverLocal(ePartido) and estaConfirmado(ePartido) and todaviaNoSeJugo(ePartido)):
                proxPartidos.append({
                    'rival': getRival(ePartido),
                    'fecha': getFecha(ePartido)
                })

    proxPartido = proxPartidos[0]
    return proxPartido

def esRiverLocal(ePartido):
    titulo = getTitulo(ePartido)
    return titulo.find('River Plate', 0, 11) == 0

def todaviaNoSeJugo(ePartido):
    return getFecha(ePartido) > now()


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



