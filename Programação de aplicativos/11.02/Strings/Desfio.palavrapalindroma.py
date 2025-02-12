string = input("Digite um texto: ").replace(" ", "")

inversa = string[::-1]

if string == inversa:
    print("Palíndromo")
else:
    print("Não é palíndromo")


