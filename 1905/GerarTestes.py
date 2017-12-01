import random

def gera_matriz():
    _matriz = []

    for i in range(5):
        linha = []
        for j in range(5):
            if (random.random() > 0.8):
                linha.append("1")
            else:
                linha.append("0")

        _matriz.append(linha)
    
    return _matriz

def imprime_matriz(matriz):
    for j in range(5):
        print " ".join(matriz[j])

for i in range(100):
    matriz = gera_matriz()

    imprime_matriz(matriz)

    print