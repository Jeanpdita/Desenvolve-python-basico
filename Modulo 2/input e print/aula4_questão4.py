#entrada 
valor = int(input("digite o valor:"))

notas_100 = (valor // 100) 
valor = valor % 100

notas_50 = valor // 50 
valor = valor % 50 

notas_20 = valor // 20 
valor = valor % 20 

notas_10 = valor // 10 
valor = valor - 10 * notas_10

notas_5 = valor // 5 
valor = valor - 5 * notas_5

notas_2 = valor // 2
valor = valor % 2 

moeda_1 = valor // 1 
valor = valor % 1 

#nessa parte eu fiquei tao empolgado que vou tentar com as moedas menores tambem rsrs

moeda_50 = valor // 0.5 
valor = valor % 0.50

moeda_25 = valor // 0.25
valor = valor - 0.25 * moeda_25

moeda_5 = valor // 0.05 
valor = valor % 0.05

# saida 

print (f"{notas_100} nota(s) de 100")
print (f"{notas_50} nota(s) de 50")
print (f"{notas_20} nota(s) de 20")
print (f"{notas_10} nota(s) de 10")
print (f"{notas_5} nota(s) de 5")
print (f"{notas_2} nota(s) de 2")
# separação de moedas e notas
print (f"{moeda_1} moeda(s) de 1")
print (f"{moeda_50} moeda(s) de 50")
print (f"{moeda_25} moeda(s) de 25")
print (f"{moeda_5} moeda(s) de 5")




