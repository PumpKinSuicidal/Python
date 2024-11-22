genero = input("Em que turno você trabalha? Escreva M para Matutino, V para Vespertino e N para Noturno: ").lower()

if genero == "m":
    print("Bom dia.")
elif genero == "v":
    print("Boa tarde.")
elif genero == "n":
    print("Boa noite.")
else:
    print("Era pra ter digitado M, V ou N.")