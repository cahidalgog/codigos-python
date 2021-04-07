# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:59:02 2021

@author: HP
"""

#%% expansion taylor coseno

import numpy as np

x = int(input("Ingrese numero a evaluar: "))

cos_x = 1 - (x**2/np.math.factorial(2)) + (x**4/np.math.factorial(4)) - (x**6/np.math.factorial(6)) + (x**8/np.math.factorial(8)) - (x**10/np.math.factorial(10))

print(cos_x)

#%% mod
dividendo = int(input("Ingrese divisor: "))
divisor = int(input("Ingrese dividendo: "))

x = dividendo / divisor

mod = dividendo - (divisor * int(x))

print(mod)

#%% **
x = int(input("Ingrese numero a elevar: "))
potencia = int(input("Ingrese potencia: "))

resultado = 1

for i in range (potencia):
    resultado = resultado * x
    
print(resultado)

#%% TRAFFIC JAM:
import matplotlib.pyplot as plt


# t = 0

#posiciones:
pos = np.linspace(2, 20, 10)

#velocidad:
vel_rand = np.random.rand(10)
a = -0.2 # define minimo de variación
b = 0.2 # max variacion
vel_escalada = a + (b-a) * vel_rand
vel_promedio = 1.5
vel_inicial = vel_promedio + vel_escalada

# ploteo incial:
plt.scatter(pos, np.zeros(10), c=pos)


# loop          

t = list(range(10))

for x in t:
    pos = pos + vel_inicial*1
    plt.scatter(pos, t, c = pos)

    


