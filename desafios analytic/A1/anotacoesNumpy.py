#   ANOTACOES:
#Indexing e Slicing
#Index e o padrao se usado para se referencia um indice de uma array ou list [n]  
#Slicing pode determinar o inicio e o fim [i:f] ou se quisermos todos ate o um fim [:f]

import numpy as np 
from numpy import random

dados =  np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

# Uma array de inteiros de 0 a 10 e 100 indices
#Por algum motivo no lugar do 11 se eu colocar 10 o rand nao coloca o 10 na lista 
de_zero_cem = np.random.randint(0, 11, 100)

def media(arr):
    soma = 0
    for el in arr:
        soma += el
    return soma / len(arr)

def desvio_padrao(arr):
    media_aritmetica = media(arr)
    somatorio_square = 0
    for el in arr:
        somatorio_square += (el - media_aritmetica)**2
    resultado = (somatorio_square/len(arr))**0.5
    return resultado

print('='*50)
#print(f"A media foi: {media(dados)}")
#print(f"O desvio padrao foi: {desvio_padrao(dados)}")
#print(f"A ordenacao ficou: {np.sort(dados)}")
#print('='*50)
#print(f"A shape: {np.shape(dados)} mostra o memso tamanho da len: {len(dados)}") #obvio ne
#print(f"Media utilizando mean: {dados.mean()}")
#print(f"Desvio padrao usando std: {np.std(dados)}")
#print(f"MAX : {np.max(dados)}")
#print(f"MIN : {np.min(dados)}")

print(f"SHAPE: {np.shape(de_zero_cem)}")
print(f"MEDIA: {de_zero_cem.mean()}")
print(f"DESVIO PADRAO: {np.std(de_zero_cem)}")
print(f"MAX: {np.max(de_zero_cem)}")
print(f"MIN: {np.min(de_zero_cem)}")