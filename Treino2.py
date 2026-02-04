import tkinter as tk
import json
tarefa = []


app = tk.Tk()
app.title("TESTEEE")
app.geometry("230x300")

def salvar():
    with open("tarefa.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefa, arquivo, ensure_ascii=False, indent=4)

def carregar():
    global tarefa
    try:
        with open("tarefa.json", "r", encoding="utf-8") as arquivo:
            tarefa = json.load(arquivo)
    
    
    
    
    
    except FileNotFoundError:
        tarefa = []

def atualizar():
    lista.delete(0, tk.END)

    for i in tarefa:
        lista.insert(tk.END, i["tarefa"])


def add():
    adicione = adicionar.get()
    if not adicione:
        menssagem['text'] = ""
        return
    listinha = {'tarefa': adicione}
    tarefa.append(listinha)
    salvar()
    atualizar()
    
    
    lista.insert(tk.END, adicionar.get())
    adicionar.delete(0,tk.END)


def concluir():
   selecionar = lista.curselection()
   if selecionar:
        indice = selecionar[0]
        lista.itemconfig(indice, bg="lightgreen", fg="black")
        salvar()
        atualizar()
        
        
menssagem = tk.Label(app, text="")
menssagem.grid(row=1, column=0)
lista = tk.Listbox(app)


lista.grid(row=1, column=0)


adicionar = tk.Entry()
adicionar.grid()

tk.Button(app, text="ADICIONAR", command=add).grid(row=0, column=0)

tk.Button(app, text="TAREFA FEITA", command=concluir).grid(row=5, column=0)







carregar()
atualizar()
app.mainloop()