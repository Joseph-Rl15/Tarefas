from banco import Banco
from time import sleep


banco = Banco()
banco.carregar()
while True:
    print("1 - Criar conta")
    print("2 - Entrar ")
    print("0 - Sair")
    op = input("Escolha: ")
    
    
    if op == "0":
        break

    if op == "1":
        nome = input("Nome?: ")
        banco.cadastrar(nome)

    if op == "2":
        if not banco.conta:
            print("Nenhuma conta encontrada !")
            continue
        banco.ver()
        idx = int(input("Numero da conta: "))
        sleep(2)
        conta = banco.conta[idx]
        
    
        while True:
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Mostrar saldo")
            print("0 - Voltar")

            escolha = input("Escolha: ")


            if escolha == "0":                
                banco.salvar()
                break

            if escolha == "1":
                valor = int(input("valor: "))
                conta.deposito(valor)
                sleep(1)

            if escolha == "2":
                valor = int(input("valor: "))
                try:
                    conta.saque(valor)
                    sleep(1)
                except Exception as e:
                    print(e)
            if escolha == "3":
                conta.mostrar()
                sleep(2)