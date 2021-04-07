# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:59:16 2021
LIST COMPREHENSION
@author: HP
"""
import numpy as np

# CREAMOS lista aleatoria
cart = np.random.rand(20)
cashier = []

for item in cart:
    if item > 0.7:
        cashier.append(item)
print(cashier)


#%%
#con list comprehension
#primero, no necesitamos crear la lista vacia
#antes de la linea de codigo.
#partimos con la lista que queremos construir
#luego la igualamos el valor de la list comphension

import numpy as np
cart = np.random.rand(20)
cashier = [item for item in cart if item > 0.7]

print(cashier)

#%%
# Sumar un numero a una lista

lista = [0,1,1,2,3,4,1,2,3]
lista_nueva = [item +1 for item in lista]
print(lista)
print(lista_nueva)

#ahora sumarle 1 solo si es menor a 2.
lista_nueva2 = [item + 1 for item in lista if item < 2]
print()
print()
print(lista_nueva)
print(lista_nueva2)


#%%

#con dos for

inputs = ["1, foo, bar", "2,tom,  jerry"]

outputs1 = [[int(x), y.strip(), z.strip()] for x,y,z in (s.split(',') for s in inputs)]
print(outputs1) 



#%%

lista = "que pasa chuchetumare"
lista0 = lista.split(" ")
print(lista0)



lista1 = [x for x in lista]
print(lista1)

lista2 = [i for i in (x for x in lista)]
print(lista2)

#%%


# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
  
flatten_planets = []
  
for sublist in planets:
    for planet in sublist:
          
        if len(planet) < 6:
            flatten_planets.append(planet)
          
print(flatten_planets)

#%% 
# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
  
# Nested List comprehension with an if condition
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]
          
print(flatten_planets)







