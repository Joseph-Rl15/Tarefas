import tkinter as tk
import json
cadastros = []


def salvar():
    with open("cadastros.json", "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)


def carregar():
    global cadastros
    try:
        with open("cadastros.json", "r", encoding="utf-8") as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        cadastros = []





janela = tk.Tk()
janela.title("PRINCIPAL")
janela.geometry("400x300")
tk.Label(janela, text="BEM VINDO").pack(pady=10)

janela2 = tk.Frame(janela)
janela2.pack()
menssagem1 = tk.Label(janela2, text="")
menssagem1.pack()


tk.Label(janela2, text="Usuario").pack()
usuario = tk.Entry(janela2)
usuario.pack()


tk.Label(janela2, text="Senha").pack()
senha = tk.Entry(janela2)
senha.pack()





def entrar():
    carregar()
    for i in cadastros:
        usuarios = usuario.get()
        senhas = senha.get()
         
        if usuarios == i['usuario'] and senhas == i['senha']:
            janela2.pack_forget()
            logins.pack()
            usuario.delete(0, tk.END)
            senha.delete(0, tk.END)
            return
    else:
        menssagem1["text"] = "As credencias estão erradas !"
        
    






tk.Button(janela2, text="Entrar", command=entrar).pack(fill="y",pady=10)



def cadastrars():
    janela2.pack_forget()
    pagina_do_cadastro.pack()



tk.Button(janela2, text="Cadastrar", command=cadastrars).pack(fill="x")


pagina_do_cadastro = tk.Frame(janela)



tk.Label(pagina_do_cadastro, text="Diga seu nome para o cadastro !").pack()
cadastro_usuario = tk.Entry(pagina_do_cadastro)
cadastro_usuario.pack()

tk.Label(pagina_do_cadastro, text="Diga uma senha !").pack()
cadastro_senha = tk.Entry(pagina_do_cadastro)
cadastro_senha.pack()

def efetuar_cadastro(): 
    
    usuarios = cadastro_usuario.get()
    senhas = cadastro_senha.get()
    if not usuarios or not senhas:
        menssagem["text"] = "Não pode ficar vazio aqui !"
        return
    else:
        lista = {'usuario': usuarios, 'senha': senhas}
        cadastros.append(lista)
        salvar()
        menssagem['text'] = "Cadastro bem sucedido"
        cadastro_senha.delete(0, tk.END)
        cadastro_usuario.delete(0, tk.END)





tk.Button(pagina_do_cadastro, text="Cadastrar",command=efetuar_cadastro).pack()
menssagem = tk.Label(pagina_do_cadastro, text="")
menssagem.pack()
def voltar_do_cadastro():
    pagina_do_cadastro.pack_forget()
    janela2.pack()
    menssagem['text'] = ""
    menssagem1['text'] = ""

tk.Button(pagina_do_cadastro, text="Voltar", command= voltar_do_cadastro).pack()


logins = tk.Frame(janela)
tk.Label(logins, text="oii").pack()
def voltar_do_login():
    logins.pack_forget()
    janela2.pack()
    menssagem1 ["text"] =""



tk.Button(logins, text="Voltar", command=voltar_do_login).pack()


carregar()
janela.mainloop()