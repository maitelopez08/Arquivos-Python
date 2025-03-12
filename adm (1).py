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
