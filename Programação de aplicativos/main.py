from ContaBancos import ContaCorrente, CartaoCredito
# PROGRAMA

# Informações da conta >-<
#Cria uma nova instância da classe ContaCorrente (conta_lira)
conta_lira = ContaCorrente("Lira", "111.222.333-45",1234,34062) #34062 é respectivamente o número da conta corrente.

#Cria uma nova instância da classe CartaoCredito (cartao_lira)
cartao_lira = CartaoCredito("Lira", conta_lira)