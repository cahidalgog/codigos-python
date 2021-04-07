# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 17:29:42 2021

@author: HP
"""

#%%
# Ejercicio 1:
#La respuesta la dejé en el print

print("El código pide inicialmente una frase como input. \
Luego crea la lista aux que, mediante el método .split \
divide la frase en palabras (dado el separador de espacios), generando \
una lista en la que los elementos son las palabras que componen la frase. \
luego con el primer for se indica un loop para cada elemento de la lista (cada palabra) \
mientras que sgundo for indica el segundo loop, en el cual se evalua cada letra de cada palabra \
Es decir, con estos dos loops se establece que se evalua cada letra de cada palabra. \
El IF indica que si la letra i de la palabra x es una vocal, se agregue a \
la lista bin un string 0; por el contrario, si la letra i de la palabra x es \
una consonante, se agrega el string 1 a la lista bin. \
El método .join junta los elementos anteriores en un solo string. \
De esta manera, el resultado final indica para cada palabra de la lista \
su composición de ltras bajo la forma de un string binario, donde cada \
consonante toma la forma de 1 y cada vocal la de 0. Por ejemplo, la palabra hola \
sería impresa con el print como 1010. Finalmente, el resultado será \
impreso de esta forma para cada palabra de la frase ingresada en el input.")
           
    
#%%
#Ejercicio 2: Escriba un programa que pida al usuario una palabra y muestre \
# por pantalla el numero de veces que contiene cada vocal
    
Palabra = input("Ingrese una palabra: ") 

# contadores de vocales inicializados en 0
a = 0
e = 0
i = 0
o = 0
u = 0

# loop para identificar vocales por letra e ir sumandole a cada contador
for x in Palabra:    
    if 'a' in x:
        a = a + 1
    if 'e' in x:
        e = e + 1
    if 'i' in x:
        i = i + 1
    if 'o' in x:
        o = o + 1
    if 'u' in x:
        u = u + 1

print('a:', a, 'e:', e, 'i:', i, 'o:', o, 'u:', u)
    
#%%
#Ejercicio 3: Escriba un programa que, dado un p´arrafo de texto, cuente la cantidad de frases (separadas por un punto
# seguido) y la cantidad de palabras por frase.

Parrafo = input("Ingrese un párrafo: ")

# separa párrafos por cada punto seguido (separador ". ")
Parrafo_punto = Parrafo.split(". ")


# Se crea lista vacia para contar cantidad de palabras por frase
Cont = []

for x in Parrafo_punto:    
    Cont = Cont + [x]

print('Frases separadas por punto seguido:', len(Parrafo_punto))
print('Cant. palabras por frase:', Cont)

#print('la frase', Parrafo_punto[i], 'tiene', Cont[i], ' palabras')

#%%
#Ejercicio 4: Escriba un programa que pida al usuario una palabra y un n´umero entero positivo, y cree un nuevo string que
# consista en la palabra replicada tanta veces como el numero diga. Por ejemplo, si palabra es hola y el n´umero es

Palabra = input("Ingrese palabra: ")
Numero = int(input("Ingrese numero positivo: "))
Palabra = Palabra + " "
print(Palabra * Numero)
