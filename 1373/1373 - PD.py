k = int(raw_input())

while k != 0:
    x = raw_input()
    y = raw_input()

    matriz = [[0]*(len(y)+1) for z in xrange(len(x)+1)]

    for i in xrange(1, len(x)+1):
        for j in xrange(1, len(y)+1):
            matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])
            tam_seg = 0

            while (tam_seg <= i - 1 and tam_seg <= j - 1 and x[i-tam_seg-1] == y[j-tam_seg-1]):
                tam_seg += 1

            if (tam_seg >= k):
                matriz[i][j] = max(matriz[i][j], matriz[i-tam_seg][j-tam_seg] + tam_seg)

    print

    for linha in matriz:
        print linha
    
    print

    print matriz[len(x)][len(y)]

    k = int(raw_input())