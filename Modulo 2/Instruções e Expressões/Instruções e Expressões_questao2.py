SALARIOHORA = 20.0
HORASEMANA = 40
INSS = 0.10
SINDICATO = 0.05


salario_bruto = SALARIOHORA * HORASEMANA
salario_liquido = salario_bruto * (1 -INSS - SINDICATO)


print(f"Salário semanal bruto: R${salario_bruto:.2f}")
print(f"Salário semanal líquido: R${salario_liquido:.2f}")