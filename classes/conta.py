class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def deposito(self, valor):
        if valor <= 0:
            raise Exception("Deposite um valor acima de 0 reais")
        self.saldo += valor


    def saque(self, valor):
        if valor > self.saldo:
            raise Exception("Voce não possui esse valor")
        self.saldo -= valor
    
    def mostrar(self):
        print(f"O seu saldo atual é de {self.saldo} reais")


    def to_dict(self):
        return {
            "titular":self.titular,
            "saldo": self.saldo
        }
    
    @classmethod
    def from_dict(cls, dados):
        conta = cls(dados["titular"])
        conta.saldo = dados["saldo"]
        return conta