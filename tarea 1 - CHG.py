# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 23:53:33 2021

@author: HP
"""

#%%
# Ejercicio 1: la estrategia general es usar el operador mod para verificar si la diferencia de la división de 2 numeros es igual a 0 o no (en este último caso, el dividendo sería un número primo)
# Esta estrategia usa 

num=int(input("numero: "))
primos = []
if num > 0: # el valor debe ser mayor que 0
    for x in range(2, num + 1): # determina loop para valores del primer rango (entre 2 y el valor ingresado), es decir, determina el rango de valores que será probado
        for i in range(2, x): # 
            if x % i == 0: # se prueba si los valores x del rango (2, num +1), son divisibles entre este nuevo rango. Como parte en 2, cualquier numero que sea excatamente divisible entre 2 (x%2 == 0), no será primo (pues los primos solo son exact divisibles entre 1 y ellos mismos)
                break # si la diferencia de la divisón es igual a 0, entonces el valor x no es primo: se termina el loop para que siga con el siguiente valor del rango (2, num)
        else:
            primos.append(x) # si la diferencia de la división es distinta de 0, incorpora valor de x a lista de valores primos
    print(primos)
else:
    print("el numero debe ser mayor que 0 !!")



#%% Ejercicio 2: La respuesta está escrita en el print !

print("El programa identifica la cantidad de valores distintos ingresados. De esta manera, el 'out' entrega como resultado esta cantidad de valores distintos. Si los valores a, b y c son todos distintos, no se habrán activado contadores, por lo que el out sera = 3. Si hay dos valores iguales se habrá activado un contador por lo que out será = 2; si son los tres valores iguales, se habrán activado dos contadores y out será = 1.")


#%%
# Ejercicio 3. El algoritmo fue sacado de: https://es.wikipedia.org/wiki/Rol_Único_Tributario#:~:text=número%20del%20RUT.-,Procedimiento%20para%20obtener%20el%20dígito%20verificador,conocemos%20o%20que%20queremos%20verificar.
rut = input("Ingrese rut sin verificador: ")
rut = list(rut) # transforma rut a lista
lista_mult = [3, 2, 7, 6, 5, 4, 3, 2] # lista de multiplicadores predeterminados por los que se deben multiplicar los numeros del rut (o elementos de la lista)
mult_listas = [int(x)*int(y) for x,y in zip(rut, lista_mult)] # función zip para multiplicar listas (especificamente, para multiplicar cada elemento de una lista con su elemento correlacionado por posicion de la otra lista)
suma = sum(mult_listas) # suma los elementos de la lista anterior
# operacion 1:
op1 = suma / 11
# operación 2:
op2 = suma - (11 * int(op1)) # usa valor entero, pues resultado final no admite valores flotantes. Por eso, de aquí en más se usan valores enteros mediante función int().
# operación 3:
op3 = 11 - int(op2)    
# Reportar resultado:
if op3 == 11: 
    print("0")
elif op3 == 10:
    print("k")    
else:
    print("El número verificador de su rut es:", op3)
    

#%%
# Ejercicio 4: los criterios para determinar un año bisiesto son:
# Es bisiesto si es exactamente divisible entre 4 (pero debe cumplir otras cosas); 
# si no es exac. divisible entre 4, no es bisiesto
# Si es exac. divisible entre 4, pero no exac. divisible entre 100, es bisiesto
# Si es exac. divisible entre 4 y entre 100, debe ser exact. divisible entre 400

año=int(input("Ingrese año: "))
if año % 4 == 0: # primera condición: debe ser exactamente divisible entre 4
    if año % 100 != 0: # además debe no ser exact. divisible entre 100
        print ("ES bisiesto")
    else:
        if año % 400 == 0: # solo será bisiesto si es exact divisibe en 100 y exact. divisible en 400
            print ("ES bisiesto")
        else:
            print ("NO es bisiesto")
else:
    print ("NO es bisiesto")

