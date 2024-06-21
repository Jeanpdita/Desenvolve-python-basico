
SALARIOHORA = 20.0
HORASEMANA = 40
INSS = 0.10
SINDICATO = 0.05

salario_bruto = SALARIOHORA * HORASEMANA
inss = salario_bruto * INSS
sindicato = salario_bruto * SINDICATO
salario_liquido = salario_bruto - (inss + sindicato)


print(f"Salário semanal bruto: R${salario_bruto:.2f}")
print(f"Desconto INSS: R${inss:.2f}")
print(f"Desconto Sindicato: R${sindicato:.2f}")
print(f"Salário semanal líquido: R${salario_liquido:.2f}")