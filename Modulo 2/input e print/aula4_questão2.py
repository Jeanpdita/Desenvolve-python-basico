#leitura de dados (entrada)

fahrenheit = int(input("digite a temperatura em F: "))

#processamento 
Celsius = (fahrenheit -32) * 5 / 9

#saida (impressao)
print(f"{fahrenheit} Graus fahrenheit São {int(Celsius)} graus celsius. ")
