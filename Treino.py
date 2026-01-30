from time import sleep
import json
dados = []


def salvar():
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar():
    global dados
    try:   
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []

def cadastrar():
    print("<<< Cadastramento >>>")
    sleep(0.75)    

    nome = input("Qual seria seu nome?: ")

    if nome.replace(" ","").isalpha():
        print("Nome valido !")
        sleep(1.5)
    else:
        print("APENAS LETRAS !")
        sleep(0.5)
        return


    try:
        idade = int(input("Qual e a sua idade?: "))
        altura = float(input("Qual seria sua altura?: "))
    except ValueError:
        print("Por favor somente numeros !")

    dado = {'nome': nome, 'idade': idade, 'altura': altura}
    dados.append(dado)
    salvar()
    print("O CADASTRO FOI BEM SUCEDIDO")

def visualizar():
    carregar()
    if not dados:
        print("Esta vazio aqui !!")
        return
    
    print("JA IREMOS MOSTRAR SEUS DADOS...")
    sleep(1.75)


    for i in dados:
        print(f"Nome: {i['nome']} || Idade: {i['idade']} || Altura: {i['altura']}")


def editar():
    carregar()
    if not dados:
        print("Não a nada para editar aqui !")
        return
    


    procurar = input("Diga o nome do cadastro: ")
    for i in dados:
        if procurar == i['nome']:
            print(f"Nome: {i['nome']} \nIdade: {i['idade']} \nAltura: {i['altura']}")
            sleep(2)

            
            print("1 - Idade")
            print("2 - Altura")
            escolha = input("Oque deseja editar?: ")

            if escolha == "1":
                try:
                    nova_idade = int(input("Qual seria sua nova idade?: "))
                except ValueError:
                    print("APENAS NUMEROS !!")
                    return
                
                i['idade'] = nova_idade
                salvar()
                print("SUA IDADE FOI ATUALIZADA COM SUCESSO !")
            
            if escolha == "2":
                try:
                    nova_altura = float(input("Qual seria sua nova altura?: "))
                except ValueError:
                    print("APENAS NUMEROS !!")
                    return
                
                i['altura'] = nova_altura
                salvar()
                print("SUA ALTURA FOI ATUALIZADA COM SUCESSO !")


def menu():

    while True:
        print("1 - Cadastrar")
        print("2 - Ver cadastros")
        print("3 - Editar cadastros")
        print("0 - Sair")
        escolha = input("Oque deseja fazer?: ")

        if escolha == "0":
            break



        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            visualizar()
        elif escolha == "3":
            editar()
        else:
            print("Escolha algo valido")
            continue


carregar()
menu()

