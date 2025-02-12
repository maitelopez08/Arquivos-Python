n = int(input("Digite um número inteiro positivo: "))

if n == 1:
    print("Não é primo. O número 1 não é primo.")
else:
    numero = 2
    divisores = 0

    while (numero <= n - 1):
        if (n % numero == 0):  # Verifica se 'n' é divisível por 'numero'
            divisores = divisores + 1
        numero = numero + 1 

    if (divisores == 0):
        print("É primo.")
    elif (divisores == 1):
        print("Não é primo. Possui 1 divisor diferente de 1 e", n)
    else:
        print("Não é primo. Possui", divisores, "divisores diferentes de 1 e", n)
