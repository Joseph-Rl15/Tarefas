import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json


tarefas = []

app = tk.Tk()
app.title("TAREFA")
app.geometry("470x500")

def salvar():
    with open ("tarefa.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar():
    global tarefas
    try:
        with open ("tarefa.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

    except FileNotFoundError:
        tarefas = []


def atualizar():
    tree.delete(*tree.get_children())



    for i in tarefas:
        if i['status'] == "concluido":
            tree.insert("","end", values=(i['id'], i['tarefa']),
                        tags=("concluido",))

        else:
            tree.insert("","end", values=(i['id'], i['tarefa']))





def concluir():
    selecao = tree.selection()
    if selecao:
        item = selecao[0]
        
        indice = tree.index(item)
        tarefas[indice]['status'] = "concluido"
        salvar()
        atualizar()


def add():
    idd = id.get()
    lltarefa = tarefa.get()

    if id.get() == "" or tarefa.get() == "":
        messagebox.showinfo(title="ERRO", message="PREENCHA OS CAMPOS !")
        return
    
    
    listinha = {'id': idd, 'tarefa': lltarefa, 'status': 'incompleto'}
    tarefas.append(listinha)
    
    tree.insert("", "end", values=(id.get(), tarefa.get()))
    
    id.delete(0, tk.END)
    tarefa.delete(0, tk.END)

    salvar()
    atualizar()



def remover():
    selecao = tree.selection()
    if selecao:
        item = selecao[0]
        
        indice = tree.index(item)
        
        tarefas.pop(indice)
        tree.delete(selecao)
        salvar()
        atualizar()







iid = tk.Label(app, text="ID")
id = tk.Entry(app)


ltarefa = tk.Label(app, text="TAREFA")
tarefa = tk.Entry(app)

tree = ttk.Treeview(app, columns=("id","tarefa"), show="headings")
tree.column("id", minwidth=0, width=30)
tree.column("tarefa", minwidth=0, width=100)
tree.heading("id", text="ID")
tree.heading("tarefa", text="TAREFA")

addd = tk.Button(app, text="INSERIR", command=add)
rmv = tk.Button(app, text="REMOVER",command=remover)
cnc = tk.Button(app, text="CONCLUIR", command=concluir)




iid.grid(row=0, column=1, sticky="W")
id.grid(row=1, column=1)

ltarefa.grid(row=0, column=2, sticky="W")
tarefa.grid(row=1, column=2)

tree.tag_configure("concluido", background="lightgreen")
tree.grid(row=3, column=1,columnspan=2, pady=5)

addd.grid(row=4, column=1)
rmv.grid(row=4, column=2)
cnc.grid(row=4, column=3)







atualizar()
carregar()
app.mainloop()
    