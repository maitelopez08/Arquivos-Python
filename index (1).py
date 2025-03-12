import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os


class LojaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIG")
        self.root.geometry("900x600")

        # Lista de produtos com o preço original adicionado
        self.products = [
            {"name": "Camiseta Fé & Devoção", "price": "R$ 69,99", "original_price": "R$ 79,99", "discount": "5% OFF", "image": "img/img1.jpg"},
            {"name": "Camiseta Jesus King", "price": "R$ 39,99", "original_price": "R$ 44,99", "discount": "10% OFF", "image": "img/img2.jpg"},
            {"name": "Camiseta Jesus & Cruz", "price": "R$ 59,64", "original_price": "R$ 69,64", "discount": "15% OFF", "image": "img/img3.jpg"},
        ]

        # Canvas e barra de rolagem
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Frame dentro do Canvas
        self.content_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Cabeçalho
        self.header = tk.Frame(self.content_frame, bg="black", height=50)
        self.header.pack(fill="x")

        self.logo_label = self.create_logo(self.header)
        self.create_header_text(self.header)

        # Barra de Navegação
        self.nav_bar = tk.Frame(self.content_frame, bg="black")
        self.nav_bar.pack(fill="x")
        self.create_nav_buttons(self.nav_bar) 
        
        # Área de Produtos
        self.product_frame = tk.Frame(self.content_frame)
        self.product_frame.pack(fill="both", expand=True)

        self.display_products()

        # Atualiza a região visível do canvas
        self.content_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Rodapé dentro do content_frame
        self.footer = tk.Frame(self.content_frame, bg="black", height=30)
        self.footer.pack(fill="x", side="bottom")
        self.create_footer(self.footer)

    def create_logo(self, parent):
        logo_path = "img/logo.png"
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((120, 120))
            logo = ImageTk.PhotoImage(img)
            logo_label = tk.Label(parent, image=logo, bg="black")
            logo_label.image = logo
            logo_label.pack(side="left", padx=10)
            return logo_label
        else:
            return tk.Label(parent, text="LOGO NÃO ENCONTRADA", bg="black", fg="white", font=("Arial", 10, "bold"))

    def create_header_text(self, parent):
        tk.Label(
            parent, text=" Loja God Is Good - Promoção de Frete Grátis apenas nessa semana de inauguração!", 
            bg="black", fg="white", font=("Times New Roman", 15, "bold")
        ).pack(side="left", padx=20, pady=10)

    def create_nav_buttons(self, parent):
        btn_frame = tk.Frame(parent, bg="black")
        btn_frame.pack(expand=True)
        for item in ["Início", "Contato", "Sobre Nós"]:
            tk.Button(btn_frame, text=item, bg="black", fg="white", font=("Arial", 10), relief="flat", command=lambda i=item: self.open_section(i)).pack(side="left", padx=10, pady=5)
        tk.Button(btn_frame, text="Administração", bg="black", fg="white", font=("Arial", 10), relief="flat", command=self.open_admin_window).pack(side="left", padx=10, pady=5)

    def create_footer(self, parent):
        footer_label = tk.Label(
            parent, text="© 2025 Loja God Is Good - Todos os direitos reservados.",
            bg="black", fg="white", font=("Arial", 10)
        )
        footer_label.pack(pady=5)

    def load_image(self, path, size):
        img = Image.open(path).resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def display_products(self):
        cols = 3
        for i, product in enumerate(self.products):
            frame = tk.Frame(self.product_frame, relief="ridge", borderwidth=2, padx=10, pady=10)
            frame.grid(row=i // cols, column=i % cols, padx=10, pady=10)

            try:
                img = self.load_image(product["image"], (150, 150))
                label_img = tk.Label(frame, image=img)
                label_img.image = img
                label_img.pack()
            except:
                tk.Label(frame, text="Imagem não encontrada").pack()

            # Exibe o nome do produto
            tk.Label(frame, text=product["name"], font=("Times New Roman", 10, "bold")).pack()

            # Preço com desconto
            tk.Label(frame, text=product["price"], fg="green", font=("Times New Roman", 10)).pack()

            # Preço original riscado, sobrepondo o preço com desconto
            original_price_label = tk.Label(frame, text=product["original_price"], fg="red", font=("Times New Roman", 10, "italic", "underline"), relief="flat")
            original_price_label.place(x=0, y=0)  # Posiciona o preço original riscado sobre o preço atual

            # Exibe o desconto
            tk.Label(frame, text=product["discount"], fg="red", font=("Times New Roman", 10, "bold")).pack()

            # Botão para abrir a janela de compra
            tk.Button(frame, text="Comprar", bg="blue", fg="white", font=("Times New Roman", 10), 
                      command=lambda p=product: self.open_product_window(p)).pack(pady=5)

    def open_product_window(self, product):
        window = tk.Toplevel(self.root)
        window.title(f"Comprar {product['name']}")
        window.geometry("400x500")

        tk.Label(window, text=product["name"], font=("Arial", 14, "bold")).pack(pady=10)

        try:
            img = self.load_image(product["image"], (200, 200))
            label_img = tk.Label(window, image=img)
            label_img.image = img
            label_img.pack()
        except:
            tk.Label(window, text="Imagem não encontrada").pack()

        tk.Label(window, text=f"Preço: {product['price']}", fg="green", font=("Arial", 12)).pack()
        tk.Label(window, text=f"Desconto: {product['discount']}", fg="red", font=("Arial", 12)).pack()

        # Seleção de tamanho
        tk.Label(window, text="Escolha o tamanho:", font=("Arial", 10)).pack(pady=5)
        size_var = tk.StringVar(value="M")
        sizes = ["P", "M", "G", "GG"]
        for size in sizes:
            tk.Radiobutton(window, text=size, variable=size_var, value=size).pack()

        # Informações de envio
        tk.Label(window, text="Nome completo:", font=("Arial", 10)).pack(pady=5)
        name_entry = tk.Entry(window, font=("Arial", 10))
        name_entry.pack()

        tk.Label(window, text="Endereço:", font=("Arial", 10)).pack(pady=5)
        address_entry = tk.Entry(window, font=("Arial", 10))
        address_entry.pack()

        tk.Label(window, text="E-mail:", font=("Arial", 10)).pack(pady=5)
        email_entry = tk.Entry(window, font=("Arial", 10))
        email_entry.pack()

        # Escolha da forma de pagamento
        payment_var = tk.StringVar(value="Cartão de Crédito")
        payment_label = tk.Label(window, text="Escolha a forma de pagamento:", font=("Arial", 10))
        payment_label.pack(pady=5)

        payment_options = ["Cartão de Crédito", "Boleto", "Pix"]
        for option in payment_options:
            tk.Radiobutton(window, text=option, variable=payment_var, value=option).pack()

        # Botão de compra
        def finalizar_compra():
            tamanho = size_var.get()
            nome = name_entry.get()
            endereco = address_entry.get()
            email = email_entry.get()
            pagamento = payment_var.get()

            # Calculando o valor final com o desconto
            price_value = float(product["price"].replace("R$", "").replace(",", ".")) 
            discount_value = float(product["discount"].replace("% OFF", "")) / 100
            final_price = price_value * (1 - discount_value)

            nota_fiscal = f"""
            Loja God Is Good
            -----------------------
            Produto: {product['name']}
            Preço: {product['price']}
            Desconto: {product['discount']}
            Tamanho: {tamanho}
            Nome: {nome}
            Endereço: {endereco}
            E-mail: {email}
            Forma de pagamento: {pagamento}
            Total: R$ {final_price:.2f}
            -----------------------
            Obrigado pela sua compra!
            """
            messagebox.showinfo("Nota Fiscal", nota_fiscal)
            window.destroy()

        tk.Button(window, text="Finalizar Compra", bg="green", fg="white", font=("Arial", 12), command=finalizar_compra).pack(pady=10)





    def show_contacts(self):
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("Contatos")
        contacts_window.geometry("400x400")
        contacts_window.configure(bg="black")

        # Cabeçalho da janela
        header_frame = tk.Frame(contacts_window, bg="black", height=50)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="Contatos Loja God Is Good", font=("Times New Rome", 16, "bold"), fg="white", bg="black").pack(pady=10)

        # Estilo dos detalhes de contato ( Não ligue para mim )
        contact_frame = tk.Frame(contacts_window, bg="black")
        contact_frame.pack(expand=True, pady=20)

        # Instagram 🔥
        try:
            instagram_img = self.load_image("img/instagram_icon.png", (20, 20))  # Coloque um ícone de Instagram
            instagram_label = tk.Label(contact_frame, text="Instagram: @god_is_good", font=("Arial", 12), fg="white", bg="black", image=instagram_img, compound="left")
            instagram_label.image = instagram_img  # Garantir que a imagem não seja coletada
            instagram_label.pack(pady=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem do Instagram: {e}")
            tk.Label(contact_frame, text="Instagram: @god_is_good", font=("Arial", 12), fg="white", bg="black").pack(pady=10)

        # WhatsApp
        try:
            whatsapp_img = self.load_image("img/whatsapp_icon.png", (20, 20))  # Coloque um ícone de WhatsApp
            whatsapp_label = tk.Label(contact_frame, text="WhatsApp: (47) 9090-6745", font=("Arial", 12), fg="white", bg="black", image=whatsapp_img, compound="left")
            whatsapp_label.image = whatsapp_img  # Garantir que a imagem não seja coletada
            whatsapp_label.pack(pady=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem do WhatsApp: {e}")
            tk.Label(contact_frame, text="WhatsApp: (47) 9090-6745", font=("Arial", 12), fg="white", bg="black").pack(pady=10)

        # E-mail
        try:
            email_img = self.load_image("img/email_icon.png", (20, 20))  # Coloque um ícone de E-mail
            email_label = tk.Label(contact_frame, text="E-mail: god_is_good@gmail.com", font=("Arial", 12), fg="white", bg="black", image=email_img, compound="left")
            email_label.image = email_img  # Garantir que a imagem não seja coletada
            email_label.pack(pady=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem do E-mail: {e}")
            tk.Label(contact_frame, text="E-mail: god_is_good@gmail.com", font=("Arial", 12), fg="white", bg="black").pack(pady=10)

        # Créditos
        footer_label = tk.Label(contacts_window, text="Desenvolvido por MJR", font=("Arial", 10, "italic"), fg="white", bg="black")
        footer_label.pack(side="bottom", pady=10)

    def open_section(self, section):
        if section == "Contato":
            self.show_contacts()
        elif section == "Sobre Nós":
            self.show_about_us()


    def show_about_us(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("Sobre Nós")
        about_window.geometry("800x800")
        about_window.configure(bg="black")

        # Cabeçalho da janela
        header_frame = tk.Frame(about_window, bg="black", height=50)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="Sobre a Loja God Is Good", font=("Times New Roman", 16, "bold"), fg="white", bg="black").pack(pady=10)

        # Texto sobre a loja
        about_text = """
        A "God is Good" foi criada pelas irmãs Maite, Jamilly e Raquel Ferreira, que, com corações cheios de fé e paixão, decidiram começar uma jornada para espalhar a palavra de Deus através da moda. 
        Em 1920, elas se mudaram para Joinville com um sonho simples: oferecer roupas que não apenas vestissem, mas que também transmitissem valores cristãos.

        Com o nome "God is Good", que significa "Deus é bom", a loja nasceu com o propósito de evangelizar e impactar a vida das pessoas de uma maneira única. 
        Ao longo dos anos, a missão delas sempre foi mais do que oferecer produtos de qualidade, mas ser um ponto de encontro de fé, acolhimento e amor.

        Hoje, a "God is Good" segue crescendo, mantendo seus valores inabaláveis e tocando vidas através de cada peça que carrega o amor de Deus em cada detalhe. 
        Estamos aqui para vestir sua fé com muito estilo e, acima de tudo, com a certeza de que Deus é bom, sempre.

        E para levar ainda mais a palavra de Deus a todos os cantos, nossa loja online está disponível, para que você possa vestir sua fé de qualquer lugar com a qualidade e o carinho que sempre entregamos.
    
        "\n (Mensagem das Criadoras):\n Criar a God is Good foi uma resposta de Deus para o nosso coração. Sabíamos que Ele nos chamava para algo maior, para levar Sua palavra através do que amamos fazer. Cada estampa, cada peça de roupa, é um testemunho de fé e amor. Agradecemos a Deus por nos permitir viver esse sonho." – Maite Ferreira \n Quando começamos, não imaginávamos o impacto que nossas roupas poderiam ter na vida das pessoas. Mas a cada dia, vemos como Deus usa essa loja para tocar corações. É um privilégio ser parte desse propósito. Que cada peça da God is Good seja uma bênção na vida de quem a veste." – Jamilly Ferreira\n A nossa missão nunca mudou: evangelizar, espalhar amor e vestir as pessoas com a palavra de Deus. Estamos aqui para ser uma luz na vida de cada um que entra na nossa loja e carrega nossa mensagem. Deus é bom, e sempre será." – Raquel Ferreira
     """
        
    
        tk.Label(about_window, text=about_text, font=("Arial", 12), fg="white", bg="black", justify="left", wraplength=600).pack(padx=20, pady=10)


      


    
    # Rodapé
   # footer_label = tk.Label(about_window, text="Desenvolvido por MJR", font=("Arial", 10, "italic"), fg="white", bg="black")
   # footer_label.pack(side="bottom", pady=10)



# Inicia a aplicação
root = tk.Tk()
app = LojaApp(root)
root.mainloop()