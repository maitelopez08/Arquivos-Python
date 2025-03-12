import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# Criar a janela principal do Tkinter
root = tk.Tk()
root.title("Loja God is Good")
root.geometry("500x600")

# Lista para armazenar os produtos adicionados ao carrinho
cart = []
desconto_aplicado = 0  # Variável global para armazenar o desconto aplicado
frete_valor = 0  # Valor do frete
cupom_aplicado = ""  # Variável global para armazenar o cupom aplicado

# Função para calcular frete
def calcular_frete(tipo_frete):
    if tipo_frete == "Normal":
        return 15.00
    elif tipo_frete == "Expresso":
        return 30.00
    return 0.00

# Função para aplicar cupom de desconto uma única vez
def aplicar_desconto(total, cart_window):
    global desconto_aplicado, frete_valor, cupom_aplicado

    if desconto_aplicado > 0 or cupom_aplicado:
        messagebox.showinfo("Cupom já aplicado", "Você já aplicou um cupom de desconto ou frete grátis.")
        return total

    codigo = simpledialog.askstring("Cupom de Desconto", "Digite o código do cupom:")
    descontos = {"FRETEGRATIS": "frete", "10PERCENT": 0.1, "GODISGOOD": 0.15}  

    if codigo in descontos:
        if descontos[codigo] == "frete":
            # Se o cupom for de frete grátis
            frete_valor = 0
            cupom_aplicado = "Frete Grátis"
            messagebox.showinfo("Frete Grátis", "Frete grátis aplicado!")
        else:
            desconto_aplicado = descontos[codigo]
            total = total * (1 - desconto_aplicado)
            cupom_aplicado = f"Desconto de {desconto_aplicado * 100}%"
            messagebox.showinfo("Desconto Aplicado", f"Desconto de {desconto_aplicado * 100}% aplicado!")
    else:
        messagebox.showwarning("Cupom Inválido", "O código do cupom não é válido.")

    atualizar_carrinho(cart_window)
    return total

# Função para escolher forma de pagamento
def escolher_pagamento():
    pagamento = simpledialog.askstring("Forma de Pagamento", "Escolha a forma de pagamento: Cartão ou PIX")
    if pagamento and pagamento.lower() in ["cartão", "pix"]:
        return pagamento.capitalize()
    else:
        messagebox.showwarning("Forma de Pagamento Inválida", "Escolha uma forma de pagamento válida.")
        return escolher_pagamento()

# Função para gerar Nota Fiscal
def gerar_nota_fiscal(total, frete, tipo_frete):
    pagamento = escolher_pagamento()
    nota_window = tk.Toplevel()
    nota_window.title("Nota Fiscal")
    nota_window.geometry("400x500")

    tk.Label(nota_window, text="🛙️ NOTA FISCAL - LOJA GOD IS GOOD", font=("Arial", 12, "bold")).pack(pady=5)

    for product in cart:
        tk.Label(nota_window, text=f"{product['name']} - {product['price']}", font=("Arial", 10)).pack()

    tk.Label(nota_window, text=f"Forma de Pagamento: {pagamento}", font=("Arial", 10)).pack(pady=5)
    if pagamento == "Pix":
        tk.Label(nota_window, text="Chave PIX: 123e4567-e89b-12d3-a456-426614174000", font=("Arial", 10), fg="blue").pack(pady=5)
    
    tk.Label(nota_window, text=f"Total: R$ {total:.2f}", font=("Arial", 12, "bold")).pack(pady=10)

    # Exibir o frete na Nota Fiscal
    tk.Label(nota_window, text=f"Frete: R$ {frete:.2f}", font=("Arial", 10)).pack(pady=5)
    total_com_frete = total + frete
    tk.Label(nota_window, text=f"Total com Frete: R$ {total_com_frete:.2f}", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Label(nota_window, text="✅ COMPRA FINALIZADA COM SUCESSO!", font=("Arial", 12, "bold"), fg="green").pack(pady=5)
    cart.clear()  
    reset_cupons()  # Resetando os cupons após a finalização da compra

# Função para resetar cupons
def reset_cupons():
    global desconto_aplicado, frete_valor, cupom_aplicado
    desconto_aplicado = 0
    frete_valor = 0
    cupom_aplicado = ""

# Função para atualizar o carrinho
def atualizar_carrinho(cart_window):
    global desconto_aplicado, frete_valor, cupom_aplicado

    for widget in cart_window.winfo_children():
        widget.destroy()  

    tk.Label(cart_window, text="Itens no Carrinho:", font=("Arial", 12, "bold")).pack(pady=5)

    if len(cart) == 0:
        tk.Label(cart_window, text="O carrinho está vazio.", font=("Arial", 10)).pack(pady=5)
        return 0

    total = sum(float(p['price'].replace("R$", "").replace(",", ".")) for p in cart)

    for product in cart:
        tk.Label(cart_window, text=f"{product['name']} - {product['price']}", font=("Arial", 10)).pack()

    if desconto_aplicado > 0:
        total *= (1 - desconto_aplicado)
        tk.Label(cart_window, text=f"Desconto aplicado: {desconto_aplicado * 100}%", fg="green", font=("Arial", 10)).pack()

    if cupom_aplicado:
        tk.Label(cart_window, text=f"**{cupom_aplicado}**", fg="green", font=("Arial", 10)).pack()

    tk.Label(cart_window, text=f"Total: R$ {total:.2f}", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(cart_window, text="Aplicar Cupom", command=lambda: aplicar_desconto(total, cart_window)).pack()
    
    tk.Button(cart_window, text="Finalizar Compra", bg="green", fg="white", font=("Arial", 12), command=lambda: gerar_nota_fiscal(total, calcular_frete("Normal"), "Normal")).pack(pady=10)

# Função para exibir os produtos
def display_products():
    products = [
        {"name": "Camiseta Fé & Devoção", "price": "R$ 69,99", "original_price": "R$ 79,99", "discount": "5% OFF", "image": "img/img1.jpg"},
        {"name": "Camiseta Jesus King", "price": "R$ 39,99", "original_price": "R$ 44,99", "discount": "10% OFF", "image": "img/img2.jpg"},
        {"name": "Camiseta Jesus & Cruz", "price": "R$ 59,64", "original_price": "R$ 69,64", "discount": "15% OFF", "image": "img/img3.jpg"},
    ]
    
    for product in products:
        # Carregar a imagem da camiseta
        img = Image.open(product["image"])
        img = img.resize((100, 100))  # Reduzir o tamanho da imagem para 100x100
        img_tk = ImageTk.PhotoImage(img)
        
        # Criar o frame para cada produto
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=10)

        # Exibir a imagem
        img_label = tk.Label(frame, image=img_tk)
        img_label.image = img_tk  # Manter referência à imagem
        img_label.pack()

        # Exibir o nome e preço
        info_label = tk.Label(frame, text=f"{product['name']}\n{product['price']}", font=("Arial", 10))
        info_label.pack()

        # Botão "Adicionar" ao carrinho
        add_button = tk.Button(frame, text="Adicionar", command=lambda p=product: add_to_cart(p))
        add_button.pack()

# Função para adicionar produto ao carrinho
def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Produto Adicionado", f"{product['name']} foi adicionado ao carrinho.")

# Função para abrir a janela do carrinho
def open_cart_window():
    cart_window = tk.Toplevel()
    cart_window.title("Carrinho de Compras")
    cart_window.geometry("400x500")
    atualizar_carrinho(cart_window)

# Início da interface
tk.Label(root, text="Bem-vindo à Loja God is Good", font=("Arial", 16, "bold")).pack(pady=20)

# Exibir os produtos disponíveis
display_products()

# Botão para abrir o carrinho
tk.Button(root, text="Ver Carrinho", command=open_cart_window, bg="orange", fg="white", font=("Arial", 12)).pack(pady=20)

# Iniciar o loop principal do Tkinter
root.mainloop()




