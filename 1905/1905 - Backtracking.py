TAMANHO_LABIRINTO = 5

def gera_labirinto():
    matriz = []
    
    for i in range(TAMANHO_LABIRINTO):
        matriz.append(raw_input().split())

    return matriz

def caminha_labirinto(labirinto, linha, coluna, capturou):
    if capturou or ((linha, coluna) == (4, 4) and labirinto[linha][coluna] == "0"): return True
    if (linha >= TAMANHO_LABIRINTO or coluna >= TAMANHO_LABIRINTO or linha <= -1 or coluna <= -1): return False
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

def main():
    n = int(raw_input())

    for i in range(n):
        labirinto = gera_labirinto()

        capturou = caminha_labirinto(labirinto, 0, 0, False)

        if capturou:
            print "COPS"
        else:
            print "ROBBERS"

        posicoes_visitadas.clear()

if __name__ == "__main__":
    main()