import matplotlib.pyplot as plt

# Dados fictícios de vendas
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
vendas = [1000, 1500, 1200, 1800, 2200, 2000, 1500, 2500, 3500, 4000, 1000, 5000]

# Criando o gráfico
plt.figure(figsize=(10, 5))  # Tamanho ajustado
plt.plot(meses, vendas, marker="o", linestyle="-", color="b", label="Vendas Mensais")

# Ajustando os limites do gráfico corretamente
plt.axis([-1, 12, 500, 5500])  # [xmin, xmax, ymin, ymax]

# Personalizando o gráfico 
plt.title("Gráfico de Vendas - Loja God is Good")
plt.xlabel("Meses")
plt.ylabel("Vendas em R$")
plt.xticks(rotation=45)  # Inclina os meses para melhor visualização
plt.grid(True)
plt.legend()

# Exibir o gráfico
plt.show()
