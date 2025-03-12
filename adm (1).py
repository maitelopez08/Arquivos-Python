# Aqui é a sede secreta dos administradores 🔥😍
# Só é permitido os membros vitalícios da MJR (Ruan de Mello e seus cumplices estão Banidos por roubo!)🫢

# Membros Vitalícios:

# DONAS:

# Maite Cullen😎- Dona da MJR, Cria os designs das roupas e acompanhou fervorosamente o desenvolvimento do site!
# Jamilly Cullen - Dona da MJR, deu o pontapé inicial para a estrutura do site, ela que trouxe a ideia perfeita para
# construirmos o nosso site! Ela também administrou nossa equipe como Scrum Master e ajudou muito na programação da
# interface do site.
# Kel Cullen -  Dona da MJR, ajudou a criar as estruturas de códigos e acompanhou o desenvolvimento da equipe. 
# Participou de inúmeras reuniões com empresas amigas e sempre está divulgando todo o trabalho da MJR

# AMIGOS/PARCEIROS VITALÍCIOS:

# Nicoly Juliana Felipa Luisa Albuquerque Virginia Pereira dos Santos Lima Castro Silva Costa Figueiredo Garcia Ribeiro Neta de Constantinopla II : Maravilhosa amiga, sempre está trazendo conselhos para vida, e ajudando nos
# designs mais bafónicos da época! Advogada perfeita para nossa empresa e, sempre maravilhosa e respeitada ❤️ 
# Yan Juan Hernandez: Nosso parceiro de negócios, Dono de uma pizzaria perfeita para a familia que quer comer algo delicioso
# Foi um amigo perfeito para Maite e ambos sempre estão juntos para espalhar a palavra de Deus🙏. (Os sabores das pizzas são estranhamente bons...)
# Tatiane Marietto Santos Garibaldi IV: Nossa queridissíma assistente de moda, ela sempre tem ideias incríveis e inovadoras e sempre faz um cafezinho daora.
# Pedro Marietti Garibaldi XXV: Rico, infleuncer e trabalhador, super fiel à sua amada esposa, sempre apoiando suas ideias malucas e inovadoras.
# Mikaleke Mokele Mbembe da Silva de Jerusalém V: Assessor da Pizzaria do Yan Juan, e garoto propaganda, ele se veste de Mokele Mbembe, na frente da Pizzaria, se sentindo bem com seu novo eu transformado, dançando sempre que pode, chocoalhando os quadris em uma dança sensual para atrair todas as Mokele Mbembas e para todos comerem na pizzaria lol.
# Marayza Miranda Machado: Amiga da Jamilly...
# Camila da Luz Bruxa de Salem: Ela é a mais poderosa das bruxas de salém, tendo ganhado seu prêmio nobel da bruxaria, e sendo a mulher mais bonita e venerada. Dizem que ela tem certos contratos com um mago poderosíssimo, inteligente e foda.
# Dom Luis Fernandes de Freitas Bragança Barroso Henrique L: Programador front-end da pizzaria Mokele Mbembes, ele é o responsável por cozinhar e definir o cardápio. Ele também é responsável por ficar junto com Mikaleke como Mokele Mbemba. Casado com uma dama de primeira classe, Antonella, a mais rica de Marte. Ela é uma Marciana super gente fina, linda de morrer, meu deus, esse Luis é sortudo viu.

# LISTA DE BANIDOS PELA ETERNIDADE:

# Ruan de Mello👽 - O maldito que foi banido por direitos autorais!!!
# Yan Amanda Ruan Hernandez = Banido por ser uma cópia barata, cruel que é insensível conspirou com Ruan de Mello para roubar os direitos autorais da MJR e o ingrediente secreto da pizzaria do irmão dele. 

#Administação Fodastica 💕

# Somente a diretoria ;)🤭

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import os

# Dados simulados (banco de dados fictício)
administradores = {"Jamilly Cullen": "12345", "Maite Cullen":"12345", "Kel Cullen":"12345"}
products = []

# Função de login
def login():
    def check_login():
        user = user_entry.get()
        password = pass_entry.get()
        if user in administradores and administradores[user] == password:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            login_window.destroy()
            admin_panel()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")
    
    login_window = tk.Toplevel(root)
    login_window.title("Login do Administrador")
    login_window.geometry("350x250")
    login_window.configure(bg="#f0f0f0")
    
    tk.Label(login_window, text="Usuário:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    user_entry = tk.Entry(login_window, font=("Times New Roman", 12), bd=2)
    user_entry.pack(pady=5)
    
    tk.Label(login_window, text="Senha:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    pass_entry = tk.Entry(login_window, show="*", font=("Times New Roman", 12), bd=2)
    pass_entry.pack(pady=5)
    
    tk.Button(login_window, text="Entrar", bg="black", fg="white", font=("Times New Roman", 12), command=check_login).pack(pady=20)

# Painel administrativo
def admin_panel():
    admin_window = tk.Toplevel(root)
    admin_window.title("Painel Administrativo")
    admin_window.geometry("500x500")
    admin_window.configure(bg="white")
    
    tk.Label(admin_window, text="Bem-vindo ao Painel Administrativo", font=("Times New Roman", 16, "bold"), bg="white").pack(pady=20)
    
    tk.Button(admin_window, text="Adicionar Produto", bg="black", fg="white", font=("Times New Roman", 12), command=janela_cadastro).pack(pady=10, fill="x")
    tk.Button(admin_window, text="Gerenciar Produtos", bg="black", fg="white", font=("Times New Roman", 12), command=gerenciar_produtos).pack(pady=10, fill="x")
    tk.Button(admin_window, text="Cadastrar Administrador", bg="black", fg="white", font=("Times New Roman", 12), command=cadastrar_admin).pack(pady=10, fill="x")
    tk.Button(admin_window, text="Gráfico de Vendas", bg="black", fg="white", font=("Times New Roman", 12), command=mostrar_grafico_vendas).pack(pady=10, fill="x")
    tk.Button(admin_window, text="Logout", bg="black", fg="white", font=("Times New Roman", 12), command=lambda: logout(admin_window)).pack(pady=20, fill="x")

# Função de logout
def logout(admin_window):
    admin_window.destroy()
    messagebox.showinfo("Logout", "Você saiu do painel administrativo.")
    root.deiconify()  # Exibe novamente a janela principal

# Cadastro de produtos
def janela_cadastro():
    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Cadastro de Produto")
    cadastro_window.geometry("400x400")
    cadastro_window.configure(bg="#f0f0f0")

    tk.Label(cadastro_window, text="Nome:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    nome_entry = tk.Entry(cadastro_window, font=("Times New Roman", 12), bd=2)
    nome_entry.pack(pady=5)

    tk.Label(cadastro_window, text="Descrição:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    desc_entry = tk.Entry(cadastro_window, font=("Times New Roman", 12), bd=2)
    desc_entry.pack(pady=5)

    tk.Label(cadastro_window, text="Preço:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    preco_entry = tk.Entry(cadastro_window, font=("Times New Roman", 12), bd=2)
    preco_entry.pack(pady=5)

    tk.Label(cadastro_window, text="Estoque:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    estoque_entry = tk.Entry(cadastro_window, font=("Times New Roman", 12), bd=2)
    estoque_entry.pack(pady=5)

    tk.Label(cadastro_window, text="Imagem:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    img_entry = tk.Entry(cadastro_window, font=("Times New Roman", 12), bd=2)
    img_entry.pack(pady=5)

    def escolher_imagem():
        filename = filedialog.askopenfilename(title="Selecione uma imagem",
                                              filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if filename:
            img_entry.delete(0, tk.END)
            img_entry.insert(0, filename)

    tk.Button(cadastro_window, text="Selecionar Imagem", bg="black", fg="white",
              font=("Times New Roman", 12), command=escolher_imagem).pack(pady=10)

    def salvar_produto():
        products.append({
            "nome": nome_entry.get(),
            "descricao": desc_entry.get(),
            "preco": preco_entry.get(),
            "estoque": estoque_entry.get(),
            "imagem": img_entry.get()
        })
        messagebox.showinfo("Sucesso", "Produto cadastrado!")
        cadastro_window.destroy()

    tk.Button(cadastro_window, text="Salvar", bg="black", fg="white",
              font=("Times New Roman", 12), command=salvar_produto).pack(pady=20)

# Gerenciar produtos
def gerenciar_produtos():
    gerenciar_window = tk.Toplevel(root)
    gerenciar_window.title("Gerenciar Produtos")
    gerenciar_window.geometry("500x400")
    gerenciar_window.configure(bg="#f0f0f0")

    for prod in products:
        frame = tk.Frame(gerenciar_window, relief="ridge", borderwidth=2, bg="#ffffff")
        frame.pack(fill="x", pady=5)
        
        try:
            img = Image.open(prod['imagem']).resize((50, 50))
            img = ImageTk.PhotoImage(img)
            label_img = tk.Label(frame, image=img)
            label_img.image = img  # Mantém referência
            label_img.pack(side="left", padx=5)
        except:
            tk.Label(frame, text="Imagem não encontrada", bg="#ffffff").pack(side="left", padx=5)
        
        tk.Label(frame, text=f"{prod['nome']} - {prod['preco']} - Estoque: {prod['estoque']}", bg="#ffffff", font=("Times New Roman", 10)).pack(side="left", padx=10)
        
        tk.Button(frame, text="Remover", bg="black", fg="white", font=("Times New Roman", 10), command=lambda p=prod: remover_produto(p, gerenciar_window)).pack(side="right", padx=10)

# Remover produto
def remover_produto(prod, window):
    products.remove(prod)
    messagebox.showinfo("Removido", "Produto removido!")
    window.destroy()
    gerenciar_produtos()

# Cadastro de Administrador
def cadastrar_admin():
    def salvar_admin():
        user = user_entry.get()
        password = pass_entry.get()
        if user and password:
            administradores[user] = password
            messagebox.showinfo("Sucesso", "Administrador cadastrado!")
            cadastro_admin_window.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")
    
    cadastro_admin_window = tk.Toplevel(root)
    cadastro_admin_window.title("Cadastro de Administrador")
    cadastro_admin_window.geometry("300x200")
    cadastro_admin_window.configure(bg="#f0f0f0")
    
    tk.Label(cadastro_admin_window, text="Usuário:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    user_entry = tk.Entry(cadastro_admin_window, font=("Times New Roman", 12), bd=2)
    user_entry.pack(pady=5)
    
    tk.Label(cadastro_admin_window, text="Senha:", bg="#f0f0f0", font=("Times New Roman", 12)).pack(pady=10)
    pass_entry = tk.Entry(cadastro_admin_window, show="*", font=("Times New Roman", 12), bd=2)
    pass_entry.pack(pady=5)
    
    tk.Button(cadastro_admin_window, text="Salvar", bg="black", fg="white", font=("Times New Roman", 12), command=salvar_admin).pack(pady=20)

# Função para mostrar gráfico de vendas
def mostrar_grafico_vendas():
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    vendas = [1000, 1500, 1200, 1800, 2200, 2000, 1500, 2500, 3500, 4000, 1000, 5000]

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

# Criando a janela principal
root = tk.Tk()
root.title("Sistema de Administração")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Botão de login
tk.Button(root, text="Login Administrador", bg="black", fg="white", font=("Times New Roman", 14), command=login).pack(pady=50)

# Inicia a interface
root.mainloop()
