# -*- coding: utf-8 -*-
"""aula1_questao 6

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

from collections import Counter

# Função para verificar se duas palavras são anagramas
def sao_anagramas(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())

# Solicita ao usuário que digite a frase
frase = input("Digite uma frase: ")

# Solicita ao usuário que digite a palavra objetivo
palavra_objetivo = input("Digite a palavra objetivo: ")

# Limpa a palavra objetivo de espaços em branco e converte para minúsculas
palavra_objetivo = palavra_objetivo.strip().lower()

# Inicializa uma lista para armazenar os anagramas encontrados
anagramas = []

# Itera sobre cada palavra na frase
for palavra in frase.split():
    # Converte a palavra para minúsculas
    palavra = palavra.lower()

    # Verifica se a palavra é um anagrama da palavra objetivo
    if sao_anagramas(palavra, palavra_objetivo):
        anagramas.append(palavra)

# Imprime os anagramas encontrados
print(f"Anagramas: {anagramas}")