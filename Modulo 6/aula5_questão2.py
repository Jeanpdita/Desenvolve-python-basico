# -*- coding: utf-8 -*-
"""Aula5_Questão2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UX8SC-shQ9GZwmHkrvFmqfHcvrpm0aRQ
"""

def testa_equilatero(lados):
    """
    Verifica se um triângulo é equilátero.

    Parâmetros:
    lados (list): Lista contendo os três lados de um triângulo.

    Retorna:
    bool: True se o triângulo for equilátero, False caso contrário.
    """
    return lados[0] == lados[1] == lados[2]

triangulos = [[2, 2, 2], [3, 4, 5], [3, 2, 2], [4, 4, 4]]

triangulos_equilateros = list(filter(testa_equilatero, triangulos))

print(triangulos_equilateros)