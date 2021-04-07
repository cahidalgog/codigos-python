# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:59:54 2021

@author: chida
"""
import pandas as pd
import numpy as np

discursos = pd.read_csv('df_ejemplo.csv', sep='\t', encoding= 'utf-8')

#visualizar df:
discursos.head() # visualiza las primeras n observaciones
discursos.sample()
discursos.tail() # visualiza las ultimas n observaciones

discursos[discursos.year >= 1950]

# TTR:
discursos['TTR'] = discursos['num_lem_unique'] / discursos['n_palabra']

#CTTR:
discursos['CTTR'] = np.sqrt(discursos['n_palabra'] / 2) * discursos['TTR']

#Fernandez - Huerta index:
discursos['FHI'] = 206.84 - 60 * (discursos['n_silaba'] / discursos['n_palabra'] )- 1.02 * discursos['n_palabra'] 

#%%
# EJ 4:

Binaria= []

for i in discursos['year']:
    if i in [1953, 1954, 1955, 1956, 1957, 1958, 2015]:
        Binaria = Binaria + [1]
    else:
        Binaria = Binaria + [0]

discursos['re_bin'] = Binaria

#%% LIST COMPREHENSION

discursos['dificultad'] = [ 'muy dificil' if x < 30 else 'no dificil' if x < 50 else 'dificil' for x in discursos.FHI]     

#%%

año = int(input("Ingrese año entre 1926 y 2015: "))

discursos[discursos.year == año]:
print('nivel de dificultad:', discursos.FHI[year], ' es incumbente:', discursos.re_bin[year])

#%%
año = int(input("Ingrese año entre 1926 y 2015: "))

for x in range(discursos.shape[0]):
    if discursos.year[x] == año:
        if discursos.Binaria[x] == 0:
            print('no es incumbente')
        else:
            print('es incumbente')
        print('dificultad: ', discursos.FHI[x])

#%% 
from numpy import random

A1 = np.random.rand(20) #genera n random, entre o y 1
A1[A1 < 0.5] = 0
A1[A1 >= 0.5] = 1
A2 = []

for x in range(A1.shape[0]):
    if A1[x+1] == 0 & A1[x-1] == 0:
        A2[x] == A2[x] + [0]
    elif A1[x+1] == 1 & A1[x-1] == 1:
        A2[X] == A2[x] + [1]



    