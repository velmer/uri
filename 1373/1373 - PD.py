k = int(raw_input())

while k != 0:
    x = raw_input()
    y = raw_input()

    n = len(x)
    m = len(y)

    matriz = [[0]*(m+1) for z in xrange(n+1)]

    for i in xrange(1, n+1):
        for j in xrange(1, m+1):
            matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])
            tam_seg = 0

            while (tam_seg <= i - 1 and tam_seg <= j - 1 and x[i-tam_seg-1] == y[j-tam_seg-1]):
                tam_seg += 1

                if (tam_seg >= k):
                    matriz[i][j] = max(matriz[i][j], matriz[i-tam_seg][j-tam_seg] + tam_seg)

    print matriz[n][m]

    k = int(raw_input())