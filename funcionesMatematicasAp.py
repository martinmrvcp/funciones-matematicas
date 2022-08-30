import os
from random import random
import random
from math import sqrt


class funciones:
    def opcion1():
        a=0
        b=0
        while a == 0:
            a=float(input("Ingrese el coeficiente principal: "))
            b=float(input("Ingrese el coeficiente independiente: "))
            if a != 0:
               print("Algunas rectas paralelas a la dada son: ")
        con = 0
        ListaParalela = []
        while (con < 3):
            bparalela = random.randint(-100,100)
            if bparalela not in ListaParalela:
                ListaParalela.append(bparalela)
            con = con + 1
        for bparalela in ListaParalela:
            if (bparalela!= b):
                if (bparalela >= 0 ):
                    print(f" y = {a} x + {bparalela}")
                else:
                    print(f" y = {a} x  {bparalela}") 
            
        print("Dos o más rectas son paralelas cuando tienen la misma pendiente,\n es decir cuando todas tienen el mismo valor de coeficiente a")

        if a != 0:
            InvCoefa= (-1)* (1/a)
            InvCoefa = round(InvCoefa,2)
            print("Algunas rectas perpendiculares a la dada son: ")
            con = 0
            ListaPerpendicular =[]
            while (con < 3):
                bperpendicular = random.randint(-100,100)
                if bperpendicular not in ListaPerpendicular:
                    ListaPerpendicular.append(bperpendicular)
                con = con + 1
            for bperpendicular in ListaPerpendicular:
                if (bperpendicular!= b):
                    if (bperpendicular >= 0 ):
                        print(f" y = {a} x + {bperpendicular}")
                    else:
                        print(f" y = {a} x  {bperpendicular}")      
            print("Dos o más rectas son perpendiculares cuando \nla pendiente de una es la inversa y opuesta de la otra.")
                

    def opcion2():
        raiz=0
        b=0
        a=0
        
        while a == 0:
            a=float(input("Ingrese el coeficiente principal: "))
            b=float(input("Ingrese el coeficiente independiente: "))
            if a != 0:
                if (b >= 0 ):
                    print(f" y = {a} x + {b}")
                else:
                    print(f" y = {a} x  {b}") 
                raiz=-b/a
                raiz= round(raiz, 2)
        print("El corte con el eje en x es ", raiz)
        print("El corte con el eje en y es ", b)
        if a > 0:
            print("La recta es creciente")
        elif a < 0:
            print("La recta es decreciente")    

         
    def opcion3():
        a=0
        b=0
        c=0
    
        while a == 0:
            while True:
                try:
                    a=float(input("Ingrese el coeficiente de la variable cuadrática: "))
                except ValueError:
                    print("ingreso invalido, ingrese un numero")
                    continue
                else:
                    break
            while True:   
                try:
                    b=float(input("Ingrese el coeficiente lineal: ")) 
                except ValueError:
                    print("ingreso invalido, ingrese un numero")
                    continue
                else:
                    break
            while True:
                try:
                    c=float(input("Ingrese el coeficiente independiente: ")) 
                except ValueError:
                        print("ingreso invalido, ingrese un numero")        
                        continue
   
                else:
                    break
           
            if a != 0:
                if (c >= 0 and b>=0 ):
                    print(f" y = {a} x² + {b} x + {c}")
                elif(c<=0 and b<=0):
                    print(f" y = {a} x²  {b} x  {c}") 
                elif(c>=0 and b<=0):
                    print(f" y = {a} x²  {b} x + {c}")
                elif(c<=0 and b>=0):
                    print(f" y = {a} x² + {b} x  {c}")
                if (b*b-4*a*c) < 0:
                    
                    print("La ecuación no tiene solución dentro de las reglas de los números reales")
                elif(b*b -4*a*c)==0:
                    x1 = (-b)/(2*a)#Como el discriminante es 0 se reduce la expresion para calcular la raiz
                    print(f"La ecuaciontiene unico corte con el eje x en el valor x1= {x1}")
                else:
                    x1 = (-b+sqrt(b*b-4*a*c))/(2*a)  # Fórmula de Bhaskara parte positiva
                    x2 = (-b-sqrt(b*b-4*a*c))/(2*a)  # Fórmula de Bhaskara parte negativa
                    print("Las soluciones de la ecuación son:")
                    print(f"x1= {x1}")#corregir print
                    print(f"x2= {x2}")#corregir print
            if a>0:
                print ("La parabola es concava hacia arriba")
                print(f"El intervalo de decrecimiento del infinito hacia {-b/(2*a)},y crecimiento desde{-b/(2*a)} al Infinito ")
            elif a<0:
                print ("La parabola en concava hacia abajo")
                print(f"El intervalo de crecimiento desde el infinito hasta{(-b/2*a)}, y decrecimiento desde {(-b/2*a)} al Infinito")      
            else:
                print("Si a es igual a 0 la funcion no es cuadratica")            
            print("El corte con el eje y es: ",c ) 
               
                
        
    def opcion4():
        return print("Opción Incorrecta, reinicie el menú y seleccione las opciones dadas")
    
    #comentario de prueba