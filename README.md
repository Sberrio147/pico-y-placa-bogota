# <p style="color:dodger blue"> Pico y placa en Bogota </p>
![Static Badge](https://img.shields.io/badge/python-yellow?logo=python) | ![Static Badge](https://img.shields.io/badge/ios-gray?logo=apple)  | ![Static Badge](https://img.shields.io/badge/request-blue) | ![Static Badge](https://img.shields.io/badge/lxml-blue)


Este repositorio nos permite saber qué placas tienen pico y placa el día de hoy en la ciudad de Bogotá.

> El pico y placa es una medida adoptada por el gobierno, puntualmente la alcaldía de bogotá, donde los vehiculos con la placa terminada en "x" número no puede circular el día de su restricción.
> Es por ello que es  importante conocer si nuestro vehículo puede o no circular en el día, para así evitar multas.

Empleando un proceso de extracción web sencillo, solamente empleando request, buscamos por medio del **xpath** la posiscón de en la que se halla la información de la restricción, junto con la fecha y el día. Así obtenemos los datos que necesitamos, luego lo imprimimos en pantalla, para adaptarlo así a un "atajo" de iPhone, para que al momento de emplear este atajo el proceso sea sencillo.
