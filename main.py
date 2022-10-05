import schedule
import time
from src.scraping import *
from src.api import *


proxPartido = getProxPartido()
cartelEntradas = getUltimoCartelDeEntradas()


# cada dia
def func1():
    proxPartido = getProxPartido()
    print('b')

def func2():
    cartelEntradas = getUltimoCartelDeEntradas()
    if proxPartido['rival'] in cartelEntradas['titulo'] and str(proxPartido['fecha'].day) in cartelEntradas['texto']: 
        print("🏟️ Hay entras a la venta ⚪️❤️⚪️ " + cartelEntradas['url'])
        # tweet("🏟️ Hay entras a la venta ⚪️❤️⚪️ " + cartelEntradas['url'])


schedule.every(.day.do(func1)
schedule.every(1).minute.do(func2)

while True:
    schedule.run_pending()
    time.sleep(1)
