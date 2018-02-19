TAMANHO_LABIRINTO = 5
VISITADO = '2'

def caminha_labirinto(linha, coluna):
    if (linha >= TAMANHO_LABIRINTO
        or coluna >= TAMANHO_LABIRINTO
        or linha <= -1
        or coluna <= -1
        or labirinto[linha][coluna] == '1'
        or labirinto[linha][coluna] == VISITADO):
        return
    
    labirinto[linha][coluna] = VISITADO

    caminha_labirinto(linha+1, coluna)
    caminha_labirinto(linha, coluna+1)
    caminha_labirinto(linha, coluna-1)
    caminha_labirinto(linha-1, coluna)

n = int(raw_input())

for i in range(n):
    labirinto = []

    while len(labirinto) < 5:
        linha = raw_input().split()

        if len(linha) > 0:
            labirinto.append(linha)
    
    if labirinto[0][0] == '1' or labirinto[4][4] == '1' or (labirinto[3][4] == '1' and labirinto[4][3] == '1'):
         print "ROBBERS"
    else:
        caminha_labirinto(0, 0)

        capturou = labirinto[4][4] == VISITADO

        if capturou:
            print "COPS"
        else:
            print "ROBBERS"