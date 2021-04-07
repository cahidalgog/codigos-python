# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:25:39 2021

@author: HP
"""

#%% Ejercicio 1: las respuestas las dejo en los print, separadas por listas

# 1: [len(x) for x in df.texto]
print('Se crea una lista nueva, que contiene la cantidad de caracteres por frase')

# 2: [len(x.split( )) for x in df.texto]

print('Se crea una nueva lista en la que se cuentan la cantidad de palabras \
 por frase. Esto porque con el método split se separan las palabras de \
 una misma frase. Luego el método len cuenta la cantidad de elementos \
 (palabras) por frase. Así, esta linea genera una lista en la que, en cada \
 elemento de i se registra la cantidad de oalabras de la frase i de \
 la columna "texto".')

# 3: [1 if x%10==0 else 0 for x in df.num]

print('Se crea una nueva lista en la que una observación tomará el valor 1 \
si el mod entre el valor x de la columna "num" y 10 es igual a 0 (es decir, \
en la nueva lista se registrará el valor 1 si x es exactamente divisible por 10). \
Si el valor  x de la observación i de la columna "num"no es exacatmente \
dividible por 10, en la nueva lista se registra el valor 0.')

#4: [x>50 for x in df.num]

print('Se crea una nueva lista en la que se recorren las observacioes de la \
      columna "num". En la lista nueva solo se registran los valores \
          de x si son mayores a 50.')

#5: [x if x>75 else 0 for x in df.num]

print('Se crea una nueva lista en la que se recorren las observaciones de la \
 columan "num", que tiene numeros enteros aleatorios entre 0 y 100. Esta \
 linea crea una nueva lista en la que se registra el valor de x si x \
 es mayor a 75, y si es igual o menor a 75 se registra como valor 0.')

#6: [[len (y) for y in x.split()] for x in df.texto]

print('Se crea una lista nueva, en la que se imprime la cantidad de letras \
     (len(y)) por palabra (x.split()) de cada frase de a columna texto.')

#7: [x.split() for x in df.texto]

print('Se crea una lista nueva. Cada elemento es una nueva lista (por observación \
      de la columna texto), conformada por el set de palabras que conforman \
    la frase de la observación i de la columna texto.')

#8: [1 if x%10==0 else 0 if x%5==0 else x for x in df.num]

print('Se crea una nueva lista. Por cada observacion de la columna "num" \
 se registra en la nueva lista el valor 1 si el valor x de "num" es \
exactamente divisible entre 10 (si la diferencia de la división es = 0); \
se registra el valor 0 si el x es exactamente divisible entre 5; \
o se registra el mismo valor de x en la nueva lista, si no cumple las \
condiciones anteriores (si no es exactamente divisible entre 10 ni entre 5).')
    
#%% Ejercicio 2:
palabra = input("Ingrese palabra: ")

final = [] # lista donde se iran sumando letras 
aux = (0) # variable auxiliar que será utilizada para diferenciar outputs.

for letra in range (len(palabra)): #genera el rango en base al indice de palabra
    if palabra[letra] != palabra[letra - 1]: #si letras de dos indices son distintas:
        final.append(palabra[letra]) #se suma la letras a la lista final
        aux = aux + 1 # si las letras son distintas, se suma un valor al contador

if aux > 1: # si las letras son distintas, el contador debe ser mayor a 1. entonces:
    print("".join(final)) #se imprime palabra y se una método join para juntar las letras no repetidas

else: # si las letras eran todas iguales, el contador se mantuvo en 0 y entonces:
    print(palabra) #se imprime palabra 

#%% Ejercicio 3:
    
import numpy as np

#a1: array 20 elementos binarios aleatorios
a1 = np.random.rand(20)
a1[a1>=0.5]=1
a1[a1<0.5]=0


#  La estrategia general es: se genera dos listas (a1 y a2). a2 irá siguiendo
# la regla establecida en la ayudantía (ira evolucionando a partir de sus vecinos)
# en cada loop for por tiempo, en el rango 1, 19. Luego, en el tiempo 2, la 
# lista a1 sobre la que evolucionará a2 del tiempo 2, será la lista a2 del rango
# 19 del tiempo 1:

#ciclos:
for tiempo in range(5): # loop por tiempo
    a2 = np.zeros(20) #se resetea a 2 antes de volver a iniciar el loop, de acuerdo a lo que vimos en la ayudantía: se genera un array de 0, menos el primer y ultimo termino, que copia los valores del arrai a1. 
    a2[0]=a1[0]
    a2[-1]=a1[-1]
    for ix in range(1,19): #loop for para rango del leng del array
        aux = a1[ix-1] + a1[ix+1]
        if aux==1:
            a2[ix]=a1[ix]
        elif aux==2:
            a2[ix]=1
        elif aux==0:
            a2[ix]=0
        print (tiempo, "a1", a1) # para ir chequeando resultados.
        print (tiempo, "a2", a2) # para ir chequeando resultados.
    a1 = a2[:] # antes de comenzar un nuevo ciclo de tiempo, el array a2 del 
    # ultimo ciclo range 19 del tiempo anterior, pasa a ser el array a1 del
    # nuevo tiempo.
    


print("Interpretación: El modelo termina convergiendo en patrones de bloques \
      de valores, es decir, grande sgrupos de 0 o 1, independiente de la \
          distribución aleatoria final. Esto me parece que se asemeja mucho al \
              modelo de vecindad lineal y segregación espacial de Thomas \
                  Schelling, en el cual se derivaba a un resultado similar \
                      de vecinadrios homogeneos.")
    



