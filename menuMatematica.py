from funcionesMatematicasAp import funciones

opcion=str(input(f"Elija opción: \n 1)Rectas paralela y perpendicular a una dada \n 2)Análisis de una recta \n 3)Análisis de una parábola \n Su Opcion => "))
   

if opcion == "1":
    funciones.opcion1()
    opcion=""
elif opcion== "2":
    funciones.opcion2()
    opcion=""
elif opcion== "3":
    funciones.opcion3()
    opcion=""
else:
    if opcion != "1" or opcion !="2" or opcion !="3":
        funciones.opcion4()    



    






