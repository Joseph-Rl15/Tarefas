from conta import Conta
import json


    
class Banco():
    def __init__(self):
        self.conta = []
        
    def cadastrar(self, nome):
        conta = Conta(nome)
        self.conta.append(conta)
        
    def salvar(self):
        with open("contas.json", "w") as arq:
            json.dump([c.to_dict()for c in self.conta] , arq, indent=4)

    def ver(self):
        for idx, i in enumerate(self.conta):
            print(idx, i.titular, i.saldo)


    def carregar(self):
        try:
            with open("contas.json", "r") as arq:
                dados = json.load(arq)

            self.conta = [Conta.from_dict(c) for c in dados]

        except FileNotFoundError:
            self.conta = []







        