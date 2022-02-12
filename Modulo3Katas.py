velAst1 = 49
velAst2 = 19
velAst3 = 50
sizeAst3 = 20

#Ejercicio Uno
if velAst1 > 25:
    print("¡¡¡CORRAN ALV VIENE UN ASTEROIDE!!!")
else:
    print("CALMANTES MONTES ALICANTES CANTANTES, EL ASTEROIDE NO VIENE HACIA ACA")

#Ejercicio Dos
if velAst2 > 20:
    print("¡Busquen una estela de luz, puede ser un asteroide!")
elif velAst2 == 20:
    print("¡Busquen una estela de luz, puede ser un asteroide!")
else:
    print("Cuidado hay un asteroide que se aproxima, pero la velocidad no es peligrosa")

#Ejercicio Tres

    #Determinando el tamaño...
if sizeAst3 > 25 and sizeAst3 < 1000 and velAst3 > 25:
    print("NOMAMEN SE VA A ACABAR EL MUNDO")
elif sizeAst3 < 25 and velAst3 > 25:
    print("Awas hay un asteroide surfeando por el espacio.")
elif sizeAst3 < 25 and velAst3 > 20:
    print("Wacha afuera y busca una LUUUUUZ")
else:
    print("Noooo hay nada que ver, reunance por alla")
