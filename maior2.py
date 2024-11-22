n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Só mais um: "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} é o maior numero.")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} é o maior numero.")
elif n3 >= n2 and n3 >= n1:
    print(f"{n3} é o maior numero.")