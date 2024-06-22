# -*- coding: utf-8 -*-
"""aula3.5_questao1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
operando1 = float(input("Digite o primeiro operando: "))

operador = input("Digite o operador (+, -, /, *, **): ")

operando2 = float(input("Digite o segundo operando: "))

#processamento
if operador == '+':
    resultado = operando1 + operando2
    print(f"Resultado: {operando1} + {operando2} = {resultado}")
elif operador == '-':
    resultado = operando1 - operando2
    print(f"Resultado: {operando1} - {operando2} = {resultado}")
elif operador == '/':
    # saida
    if operando2 == 0:
        print("Erro! Divisão por zero não é permitida.")
    else:
        resultado = operando1 / operando2
        print(f"Resultado: {operando1} / {operando2} = {resultado}")
elif operador == '*':
    resultado = operando1 * operando2
    print(f"Resultado: {operando1} * {operando2} = {resultado}")
elif operador == '**':
    resultado = operando1 ** operando2
    print(f"Resultado: {operando1} ** {operando2} = {resultado}")
else:
    print("Erro! Operação inválida. Por favor, escolha um operador válido (+, -, /, *, **).")