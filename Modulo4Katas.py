##EJERCICIO 1

texto = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

textodiv = texto.split(". ")

keyWords = ["average", "temperature", "distance"]

for oracion in textodiv:
    for keyWord in keyWords:
        if keyWord in oracion:
            oracion = oracion.replace("C","Celsius")
            print(oracion)
            break


##EJERCICIO 2

name = "Moon"
gravity = 0.00162 #Km/s
planet = "Earth"

title = "Datos de gravedad sobre " + planet

datos = f"""Nombre del planeta: {planet}
Gravedad en {name}: {gravity * 1000} m/s2
"""

plantilla = f"""{title.title()}
------------------------------------
{datos}"""

print(plantilla)

planeta = "Marte"
gravedad = .00143
nombre = "Ganimides"

nuevaPlantilla = """Datos de Gravedad Sobre: {0}
Nombre del planeta: {1}
Gravedad en {0}: {2} m/s2"""

print(nuevaPlantilla.format(nombre, planeta, gravedad*1000))