n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1 #leu um número
ordenado = True #ordenado é a variável indicadora

for i in range(n-1):
    print("Informe o número: ")
    atual = int(input())
    i = i + 1 #leu mais um número
    if atual < anterior:
        ordenado = False
        break
    anterior = atual

if (ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
