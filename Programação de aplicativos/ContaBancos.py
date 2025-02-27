from datetime import datetime
import pytz
from random import randint

class ContaCorrente:


    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome(str): Nome do Cliente
        cpf(str): CPF do Cliente. Deve ser inserido com ponto e traços (XXX.XXX.XXX-XX)
        agencia(str): Número da agência
        num_conta(str): Número de Conta Corrente do Cliente
        saldo: Saldo disponível pelo Cliente
        limite: Limite de cheque especial daquele Cliente
        transacoes: Histórico de Transações do Cliente 
    """
    
    

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

        
    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))
        pass    
    
    def depositar_dinheiro(self, valor): 
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass
    
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor!')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def consultar_historico_transacoes(self):
        print('Histórico de Transações: ')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self,valor,conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor,self._saldo,ContaCorrente._data_hora()))
        conta_destino._saldo += valor 
        conta_destino.trasacoes.append((valor,conta_destino.saldo,ContaCorrente._data_hora()))
        

# programa

conta_maeLira = ContaCorrente("Beth", "222.333.444-55", "5555", "656565" )

conta_lira = ContaCorrente("Lira", "111.222.333-45", "1234", "56789")
conta_lira.consultar_saldo()

conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()


conta_lira.sacar_dinheiro(1000)

print('Saldo Final:')
conta_lira.consultar_saldo
conta_lira.consultar_historico_transacoes()



class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self,titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular 
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)
        
        
# Informações da conta >-<
#Cria uma nova instância da classe ContaCorrente (conta_lira)
conta_lira = ContaCorrente("Lira", "111.222.333-45",1234,34062) #34062 é respectivamente o número da conta corrente.

#Cria uma nova instância da classe CartaoCredito (cartao_lira)
cartao_lira = CartaoCredito("Lira", conta_lira)
#Cria um número aleatório de cartão apenas para o exemplo
cartao_lira.numero= 123,'/'

print(cartao_lira.__dict__)

#Retorna o número da conta associada ao cartao_lira 
print(cartao_lira.conta_corrente._num_conta)
#Retorna a lista de cartões associados a conta corrente conta_lira
print(conta_lira._cartoes)


#Acessando o primeiro item da lista
print(conta_lira._cartoes[0].numero)
 
 # WAR IS OVEEEEER!!!!!