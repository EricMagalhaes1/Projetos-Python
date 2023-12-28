from abc import abstractclassmethod , ABC, abstractproperty
from datetime import *

class Cliente:

    def __init__(self,endereco):
        self.endereco = endereco
        self.conta = []

    def realiza_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def criar_conta(self, conta):
        self.conta.append(conta)  
    
class Pessoa_Fisica(Cliente):
    def __init__(self, endereco,cpf,dt_nacimento,nome):
        super().__init__(endereco)
        self.nome = nome
        self.dt_nascimento = dt_nacimento
        self.cpf = cpf

class Conta:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(inst,cliente, numero):
        return inst(cliente,numero)        

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  
            print('Deposito com sucesso!')
        else:
            print('Valor Invalido!')
            return False
    
        return True
    
    def sacar(self,valor):
        saldo = self._saldo
        verifica_saldo = saldo < valor

        if verifica_saldo:
            print("Saldo Indisponivel")

        elif valor > 0:
            saldo -= valor
            print('Saque realizado com sucesso')
            return True

        else:
            print('Valor invalido')    
            
        return False

class Conta_Corrente(Conta):
    def __init__(self, numero, cliente,limite=100,limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
        
    def sacar(self,valor):
        nmr_saque = len[transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]

        excedeu_limite = valor > self.limite
        excedeu_saque = nmr_saque > self.limite_saque

        if excedeu_limite:
            print('Erro!! Valor acima do valor de saque permitido!')

        elif excedeu_saque:
            print('Erro! Quantidade de seques excedida!')

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f""" 
            Agencia: {self.agencia}
            Conta: {self.numero}
            Titular: {self.cliente.nome}
            """
    
class Historico:
    def __init__(self):
        self._transacao = []
    
    @property
    def transacoes(self):
        return self._transacao
    
    def add_transacoes(self,transacao):
        self.transacao.append(
            {
                "tipo":  transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )