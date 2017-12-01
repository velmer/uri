TAMANHO_LABIRINTO = 5

def gera_labirinto():
    matriz = []
    
    for i in range(TAMANHO_LABIRINTO):
        matriz.append(raw_input().split())

    return matriz

def caminha_labirinto(labirinto, linha, coluna, capturou):
    if capturou or ((linha, coluna) == (4, 4) and labirinto[linha][coluna] == "0"): return True
    if (linha == TAMANHO_LABIRINTO or coluna == TAMANHO_LABIRINTO or linha == -1 or coluna == -1): return False
    if (linha, coluna) in posicoes_visitadas:
        return capturou
    else:
        posicoes_visitadas[(linha, coluna)] = True
    if (labirinto[linha][coluna] == "1"): return False
    
    i = coluna

    while (i < TAMANHO_LABIRINTO and not capturou):
        capturou = caminha_labirinto(labirinto, linha+1, coluna, capturou)
        if not capturou: capturou = caminha_labirinto(labirinto, linha, coluna+1, capturou)
        if not capturou: capturou = caminha_labirinto(labirinto, linha, coluna-1, capturou)

        i += 1
    
    return capturou

posicoes_visitadas = {}

import random

def gera_matriz():
    _matriz = []

    for i in range(5):
        linha = []
        for j in range(5):
            if (random.random() < 0.4):
                linha.append("1")
            else:
                linha.append("0")

        _matriz.append(linha)
    
    return _matriz

def imprime_matriz(matriz):
    for j in range(5):
        print " ".join(matriz[j])

def main():
    # n = int(raw_input())

    for i in range(100):
        labirinto = gera_matriz()

        capturou = caminha_labirinto(labirinto, 0, 0, False)

        imprime_matriz(labirinto)

        if capturou:
            print "COPS"
        else:
            print "ROBBERS"
        
        print

        posicoes_visitadas.clear()

if __name__ == "__main__":
    main()