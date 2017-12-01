# import random

# def gera_matriz():
#     _matriz = []

#     for i in range(5):
#         linha = []
#         for j in range(5):
#             if (random.random() > 0.8):
#                 linha.append("1")
#             else:
#                 linha.append("0")

#         _matriz.append(linha)

#     return _matriz

def salva_matriz(matriz):
    

    matriz_str = ""

    for j in range(5):
        matriz_str += " ".join(matriz[j]) + "\n"

    f.write(matriz_str)

# for i in range(100):
#     matriz = gera_matriz()

#     imprime_matriz(matriz)

#     print

import itertools

# zeros = [0,0,0,0,0]
# ums = [1,1,1,1,1]
a = list(itertools.permutations(['0','0','0','1','1']))
b = list(itertools.permutations(['1','0','1','0','1']))
c = list(itertools.permutations(['0','1','0','0','1']))
d = list(itertools.permutations(['0','1','0','1','0']))

f = open('labirintos.txt', 'w')

for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    matriz = [a[i1], b[i2], c[i3], c[i4], d[i5]]
                    salva_matriz(matriz)

f.close()