# -*- coding: utf-8 -*-
"""aula4_questao1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

#processamento
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


soma = num1 + num2


resultado = par_ou_impar(soma)

# saida
print(f"A soma dos números {num1} e {num2} é {resultado}.")