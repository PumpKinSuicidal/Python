salario = float(input("Bem vindo ao central de atendimento da organização Tabajara.\nDigite seu salário atual para calcularmos o reajuste: "))

if salario <= 280:
    aumento = salario * 0.20
    novo_salario = salario + aumento
    print(f"Seu salário era: R${salario:,.2f}\nSeu salário aumentou 20%.\nO valor aumentado foi de R${aumento:,.2f}\nSeu novo salário é R${novo_salario:,.2f}")
elif salario <= 700:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Seu salário era: R${salario:,.2f}\nSeu salário aumentou 15%.\nO valor aumentado foi de R${aumento:,.2f}\nSeu novo salário é R${novo_salario:,.2f}")
elif salario <= 1500:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"Seu salário era: R${salario:,.2f}\nSeu salário aumentou 10%.\nO valor aumentado foi de R${aumento:,.2f}\nSeu novo salário é R${novo_salario:,.2f}")
elif salario > 1500:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    # :,.2f - Limitar a apenas duas casas decimais.
    print(f"Seu salário era: R${salario:,.2f}\nSeu salário aumentou 5%.\nO valor aumentado foi de R${aumento:,.2f}\nSeu novo salário é R${novo_salario:,.2f}")
