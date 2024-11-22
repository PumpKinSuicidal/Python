# upper - converte a letra em maiusculo
# lower - convete a letra para minusculo
genero = input("Escreva F para feminino, M para masculino e O para outro: ").lower()

if genero == "f":
    print("Feminino.")
elif genero == "m":
    print("Masculino.")
elif genero == "o":
    print("Outro.")
else:
    print("Invalido.")