# -*- coding: utf-8 -*-
"""aula4.2_questao4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
# quantidade de jogos
N = int(input())

# variaveis para contagem
vitorias = 0
empates = 0
derrotas = 0

# processamento
for _ in range(N):
    gols_galo = int(input())
    gols_oponente = int(input())

    if gols_galo > gols_oponente:
        vitorias += 1
    elif gols_galo == gols_oponente:
        empates += 1
    else:
        derrotas += 1

#total
pontuacao = vitorias * 3 + empates * 1

#saida
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontuacao}")