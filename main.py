import schedule
from src.scraping import *
from src.api import *

# cada dia
proxPartido = getProxPartido()

# cada minuto
cartelEntradas = getUltimoCartelDeEntradas()
if proxPartido['rival'] in cartelEntradas['titulo'] and str(proxPartido['fecha'].day) in cartelEntradas['texto']:
    
    
    tweet("🏟️ Hay entras a la venta ⚪️❤️⚪️ " + cartelEntradas['url'])

