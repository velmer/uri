PESO_SACO = 50

def encontra_qtd_brinquedos_total():
    for i in xrange(1, qtd_pacotes+1):
        for j in xrange(1, PESO_SACO+1):
            if (pesos[i] > j):
                matriz[i][j] = matriz[i-1][j]
            else:
                matriz[i][j] = max(matriz[i-1][j], qtds[i] + matriz[i-1][j-pesos[i]])
    
    return matriz[qtd_pacotes][PESO_SACO]

n = int(raw_input())

for x in xrange(n):
    qtd_pacotes = int(raw_input())

    qtds = [0]
    pesos = [0]

    for y in xrange(qtd_pacotes):
        qtd, peso = map(int, raw_input().split())
        qtds.append(qtd)
        pesos.append(peso)
    
    matriz = [[0]*(PESO_SACO+1) for z in xrange(qtd_pacotes+1)]
    
    qtd_brinquedos_total = encontra_qtd_brinquedos_total()

    qtd_brinquedos_temporaria = 0
    peso_total = 0
    qtd_pacotes_escolhidos = 0

    i = qtd_pacotes
    j = PESO_SACO

    while (qtd_brinquedos_temporaria < qtd_brinquedos_total):
        pacote_foi_escolhido = (matriz[i][j-1] > matriz[i-1][j] or (matriz[i][j] > matriz[i][j-1] and matriz[i][j] > matriz[i-1][j]))

        if (pacote_foi_escolhido):
            qtd_brinquedos_temporaria += qtds[i]
            peso_total += pesos[i]
            qtd_pacotes_escolhidos += 1
            j -= pesos[i]

        i -= 1

    print "%d brinquedos" % qtd_brinquedos_total
    print "Peso: %d kg" % peso_total
    print "sobra(m) %d pacote(s)" % (qtd_pacotes - qtd_pacotes_escolhidos)
    print
