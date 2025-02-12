texto = input("Digite um texto: ").replace(" ", "")
s = texto.replace(" ", "").lower()
contagem = {}

for letra in s:
    contagem[letra] = contagem.get(letra, 0) + 1
letra_mais_frequente = max(contagem, key=contagem.get)
print("A letra mais comum é:", letra_mais_frequente)
