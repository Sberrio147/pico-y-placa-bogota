<p align="center">
  <img src="https://i.imgur.com/NMl7z0I.jpg" alt="Pico y Placa Bogotá"/>
</p>


# Pico y placa en Bogota
![Static Badge](https://img.shields.io/badge/python-yellow?logo=python) | ![Static Badge](https://img.shields.io/badge/ios-gray?logo=apple)  | ![Static Badge](https://img.shields.io/badge/Pyto-lawngreen) | ![Static Badge](https://img.shields.io/badge/request-blue) | ![Static Badge](https://img.shields.io/badge/lxml-blue)


Este repositorio nos permite saber qué placas tienen pico y placa el día de hoy en la ciudad de Bogotá.

> El pico y placa es una medida adoptada por el gobierno, puntualmente la alcaldía de bogotá, donde los vehiculos con la placa terminada en "x" número no puede circular el día de su restricción.
> Es por ello que es  importante conocer si nuestro vehículo puede o no circular en el día, para así evitar multas.

Empleando un proceso de extracción web sencillo, solamente empleando request, buscamos por medio del **xpath** la posiscón de en la que se halla la información de la restricción, junto con la fecha y el día. Así obtenemos los datos que necesitamos, luego lo imprimimos en pantalla, para adaptarlo así a un "atajo" de iPhone, para que al momento de emplear este atajo el proceso sea sencillo.


## ¿Qué necesitaremos?
Ahora, es necesario configurar el atajo en el iphone, para ello podemos descargarlo atravez de [este enlance](https://www.icloud.com/shortcuts/705bcc79d27142ed834d088591fb399a) cabe recordar que para que en el iPhone _pueda correr el script de Python_ es necesario contar con una aplicación que nos permita leer este tipo de archivos, en mi caso utilicé Pyto, si bien es de paga, nos permite reconocerla dentro de la app de atajos y emplear sus automatizaciones, la puedes obtener [aquí](https://apps.apple.com/app/id1436650069).
