import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar usuários temporariamente
users = {}

# Tela de Login
def tela_login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x250")
    login_window.configure(bg="#f0f0f0")

    tk.Label(login_window, text="Usuário:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    usuario_entry = tk.Entry(login_window, font=("Arial", 12), bd=2)
    usuario_entry.pack(pady=5)

    tk.Label(login_window, text="Senha:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    senha_entry = tk.Entry(login_window, font=("Arial", 12), bd=2, show="*")
    senha_entry.pack(pady=5)

    def verificar_login():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        
        if usuario in users and users[usuario] == senha:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            login_window.destroy()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    tk.Button(login_window, text="Entrar", bg="black", fg="white", font=("Arial", 12), command=verificar_login).pack(pady=20)

# Tela de Registro
def tela_registro():
    registro_window = tk.Toplevel(root)
    registro_window.title("Registro")
    registro_window.geometry("300x300")
    registro_window.configure(bg="#f0f0f0")

    tk.Label(registro_window, text="Novo Usuário:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    novo_usuario_entry = tk.Entry(registro_window, font=("Arial", 12), bd=2)
    novo_usuario_entry.pack(pady=5)

    tk.Label(registro_window, text="Nova Senha:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    nova_senha_entry = tk.Entry(registro_window, font=("Arial", 12), bd=2, show="*")
    nova_senha_entry.pack(pady=5)

    tk.Label(registro_window, text="Confirmar Senha:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    confirmar_senha_entry = tk.Entry(registro_window, font=("Arial", 12), bd=2, show="*")
    confirmar_senha_entry.pack(pady=5)

    def registrar():
        usuario = novo_usuario_entry.get()
        senha = nova_senha_entry.get()
        confirmar_senha = confirmar_senha_entry.get()

        if not usuario or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        if usuario in users:
            messagebox.showerror("Erro", "Usuário já existe!")
        else:
            users[usuario] = senha
            messagebox.showinfo("Sucesso", "Registro realizado com sucesso!")
            registro_window.destroy()

    tk.Button(registro_window, text="Registrar", bg="black", fg="white", font=("Arial", 12), command=registrar).pack(pady=20)

# Janela Principal
root = tk.Tk()
root.title("Sistema de Login")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Bem-vindo!", bg="#f0f0f0", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Login", bg="black", fg="white", font=("Arial", 12), command=tela_login).pack(pady=10)
tk.Button(root, text="Registre-se", bg="black", fg="white", font=("Arial", 12), command=tela_registro).pack(pady=10)

root.mainloop()
