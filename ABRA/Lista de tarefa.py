import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

tarefas = []

app = tk.Tk()
app.title("TAREFAS")
app.geometry("475x400")


def atualizar():
    tree.delete(*tree.get_children())

    for i in tarefas:
        if i["status"] == "concluido":
          tree.insert("", "end",
                       values=(i["id"], i["tarefa"]),
                       tags=("concluido",))
        else:
            tree.insert("", "end",
                        values=(i["id"], i["tarefa"]))




def salvar():
    with open("tarefa.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar():
    global tarefas
    try:   
        
        with open("tarefa.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []


def concluir():
    selecao = tree.selection()
    if selecao:
        item = selecao[0]
        indice = tree.index(item)
        tarefas[indice]["status"] = "concluido"

        salvar()
        atualizar()








#Aqui adicionaremos tarefas a lista Treeview      
def add():
    iid = id.get()
    lbTarefas = tarefa.get()
    
    
    if id.get() == "" or tarefa.get() == "":
        messagebox.showinfo(title="ERRO", message="POR FAVOR PREENCHA OS CAMPOS")
        return
    
    
    tarefinha = {"id": iid, "tarefa": lbTarefas, "status": "pendente"}
    tarefas.append(tarefinha)
    
    
    tree.insert("", "end", values=(id.get(), tarefa.get()))
    id.delete(0, tk.END)
    tarefa.delete(0, tk.END)
    
    
    salvar()    
    atualizar()   
        
        
# Removeremos tarefas da lista Treeview    

def remover():
   
        selecao = tree.selection()
        if selecao:
            
            item = selecao[0]
            indice = tree.index(item)
            
            tarefas.pop(indice)
            tree.delete(selecao)
            salvar()
            atualizar()
        
    
    
  
    


# Criamos variaveis para label e entry tem que estar em variaveis !
Lid = tk.Label(app, text="ID")   
id = tk.Entry(app) 
        
Ltarefa = tk.Label(app, text="TAREFA")   
tarefa = tk.Entry(app)      
        
        


# temos o coração do codigo !
tree = ttk.Treeview(app, columns=("id", "tarefa"),show="headings")
tree.column("id", minwidth=0, width=30)
tree.column("tarefa", minwidth=0, width=100)     
tree.heading("id", text="ID")
tree.heading("tarefa", text="TAREFA")
  


# botões de adicionar e remover
adc = tk.Button(app, text="INSERIR", command=add)
rmvr = tk.Button(app, text="REMOVER", command=remover)
clnc = tk.Button(app, text="CONCLUIR", command=concluir)

# Ai temos as variaveis label e entry e a parte do codigo abaixo
# Coloca as posições para ficar esteticamente melhor
Lid.grid(row=0,column=0, sticky="w")
id.grid(row=1, column=0)
        
Ltarefa.grid(row=0,column=1, sticky="w")  
tarefa.grid(row=1, column=1)
        
        
tree.tag_configure("concluido", background="lightgreen")
# posição do ttk Treeview
tree.grid(row=3, column=0, columnspan=3, pady=5)

# E aqui os botões de adicionar e remover
adc.grid(row=4, column=0)
rmvr.grid(row=4, column=1)
clnc.grid(row=4, column=2)













carregar()
app.mainloop()