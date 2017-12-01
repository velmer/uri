# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(300000000)

alfabeto = ['N','O','P']
TAMANHO_ALFABETO = 3

def pode_adicionar_genoma(genoma, nova_seq):
    if (len(genoma) < 2): return True

    genoma_juncao = genoma + nova_seq
    indice_meio = len(genoma_juncao) / 2

    i = len(genoma_juncao)-2
    j = i - 2

    while i >= indice_meio and j >=0:
        if (genoma_juncao[j:i] == genoma_juncao[i:]): return False

        i -= 1
        j -= 2

    return True

def forma_genoma(genoma, gene_a_ser_adicionado, tamanho):
    if (tamanho == 1): return gene_a_ser_adicionado
    
    indice = 0

    while indice < TAMANHO_ALFABETO:
        if alfabeto[indice] == gene_a_ser_adicionado:
            indice += 1
            continue

        gene_atual = alfabeto[indice]

        if pode_adicionar_genoma(genoma, gene_a_ser_adicionado + gene_atual):
            if (len(genoma + gene_a_ser_adicionado + gene_atual) == tamanho):
                genoma += gene_a_ser_adicionado + gene_atual
                break
            else:
                genoma_dfs = forma_genoma(genoma + gene_a_ser_adicionado, gene_atual, tamanho)

                if genoma_dfs != genoma + gene_a_ser_adicionado:
                    genoma = genoma_dfs
                    break
                    

        indice += 1
    
    return genoma

while True:
    tamanho = int(raw_input())

    if (tamanho == 0): break

    print forma_genoma('', alfabeto[0], tamanho)
