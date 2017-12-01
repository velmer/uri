def gera_subsequencias(i, subseq):
    if i == len(seq): return

    for j in range(i, len(seq)):
        subseq_atual = subseq + seq[j]
        
        if subseq_atual not in subseqs:
            subseqs[subseq_atual] = subseq_atual
            gera_subsequencias(j+1, subseq_atual)

while True:
    try:
        seq = raw_input()
    except: break

    subseqs = {}

    gera_subsequencias(0, '')

    subseqs_lista_ordenada = sorted(list(subseqs))

    for subseq in subseqs_lista_ordenada: print subseq
    print