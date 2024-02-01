import requests
from lxml import html

def obtener_restricciones():
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    url = 'https://www.pyphoy.com/bogota/particulares'
    response = requests.get(url, headers=headers)
    parser = html.fromstring(response.text)

    placas = parser.xpath('(//div[@class="sc-bd02118d-1 cSOIEp"]//div)[2]/text()')[0]
    dia = parser.xpath('(//span[@class="day"])[1]/text()')[0]
    fecha = parser.xpath('(//span[@class="date"])[1]/text()')[0]

    return f"{dia}, {fecha}\nTienen restricción los vehículos con placas terminas en: {placas}"

print(obtener_restricciones())
