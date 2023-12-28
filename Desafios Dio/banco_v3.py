from abc import abstractclassmethod , ABC, abstractproperty


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
    def __init__(self,Cliente,) -> None:
        