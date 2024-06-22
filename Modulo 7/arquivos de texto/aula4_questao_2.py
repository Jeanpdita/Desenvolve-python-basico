# -*- coding: utf-8 -*-
"""aula4_questao 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

import re

def processar_frase(arquivo_origem, arquivo_destino):
    try:
        # Abrir o arquivo de origem para leitura
        with open(arquivo_origem, 'r') as file:
            # Ler a frase do arquivo
            frase = file.read().strip()

        # Remover espaços em branco e caracteres não alfabéticos
        frase_processada = re.sub(r'[^a-zA-Z\s]', '', frase)

        # Separar cada palavra em uma linha
        palavras = frase_processada.split()

        # Abrir o arquivo de destino para escrita
        with open(arquivo_destino, 'w') as file:
            # Escrever cada palavra em uma linha no arquivo
            for palavra in palavras:
                file.write(palavra + '\n')

        # Ler o conteúdo do arquivo de destino e imprimir
        with open(arquivo_destino, 'r') as file:
            conteudo = file.read()
            print(conteudo)

    except IOError:
        print(f"Erro ao tentar abrir o arquivo {arquivo_origem} ou {arquivo_destino}")

# Nome dos arquivos
arquivo_origem = "frase.txt"
arquivo_destino = "palavras.txt"

# Chamada da função para processar a frase e salvar as palavras
processar_frase(arquivo_origem, arquivo_destino)