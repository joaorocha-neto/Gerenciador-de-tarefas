import customtkinter as ct
import tkinter as tk

nova_janela = None

def janela():
    global nova_janela

    if nova_janela and nova_janela.winfo_exists():
        nova_janela.destroy()
        
    nova_janela = ct.CTkToplevel(root)
    nova_janela.title("Adicionar Tarefa")
    nova_janela.geometry("300x200")
    nova_janela.resizable(False,  False)
    texto = ct.CTkLabel(master=nova_janela, text=("Adicione uma tarefa"), font=("Arial", 18, "bold"))
    texto.grid(pady=3, padx=5)
    entrada = ct.CTkEntry(nova_janela, width=250)
    entrada.place(x=5, y=35)
    def botao_adicionar(item, lista2):
        lista2.insert(tk.END, item)
        nova_janela.destroy()

    botao2 = ct.CTkButton(master=nova_janela, text="Adicionar", font=("Arial", 14), corner_radius=10, bg_color="white", text_color="white", command=lambda: botao_adicionar(entrada.get(), lista))
    botao2.place(x=80, y=80)

def concluido(envent):
    index = envent.widget.curselection()
    if index:
        item_selecionado = envent.widget.get(index)
        lista.delete(index)
        lista3.insert("end", item_selecionado)


def botao_remover():
    def remover_item():
        index = lista.curselection()
        index2 = lista3.curselection()
        if index:
            lista.delete(index)
            outro_botão.destroy()
        elif index2:
            lista3.delete(index2)
            outro_botão.destroy()
    outro_botão = ct.CTkButton(root, text="Remover", font=("Arial", 14, "bold"), width=15, command=remover_item, bg_color="#FDB678", fg_color="#FF7314")
    outro_botão.place(y=408, x=300)

root = ct.CTk()
root.title("Gerenciador de tarefas")
root.geometry("390x518")
root.config(bg="#FDB678")

root.resizable(False,  False)

label = ct.CTkLabel(master= root, text= "Olá, bem vindo ao seu", font=("Inter", 20), bg_color="#FDB678")
label.grid(sticky="W", padx=10, pady=40)

label2 = ct.CTkLabel(master= root, text="Gerenciador de tarefas", font=("Inter", 20, "bold"), bg_color="#FDB678")
label2.place(y=63,x=9)

linha2 = ct.CTkFrame(master=root, width=495, height=23, fg_color="#FF7314", bg_color="#FF7314")
linha2.place(y=120)

texto_da_label = ct.CTkLabel(master=root, text="Tarefas", font=("Bree Serif", 16), bg_color="#FF7314", height=0,text_color="White")
texto_da_label.place(y=122, x=5)

texto_da_label2 = ct.CTkLabel(master=root, text="Concluido", font=("Bree Serif", 16), bg_color="#FF7314", height=0,text_color="White")
texto_da_label2.place(y=122, x=300)

linha3 = ct.CTkFrame(master=root, width=2.5, height=250)
linha3.place(y=150, x=200)

linha = ct.CTkFrame(master=root, width=495, height=2.5)
linha.place(y=400)

lista = tk.Listbox(root, width=41, height=20, bg="#FDB678", fg="black")
lista.place(x=0, y=179)
lista.bind("<Double-1>", concluido)

lista3 = tk.Listbox(root, width=39, height=20,bg="#FDB678", fg="black")
lista3.place(x=252, y=179)

botao = ct.CTkButton(master=root, text="Adicionar Tarefa", font=("Arial", 14),corner_radius=10 ,bg_color="#FDB678", fg_color="#FF7314", text_color="White", height=35, command=janela)
botao.place(x=130, y=450)

botao_editar = ct.CTkButton(master=root, text="Editar", font=("Arial", 14, "bold"), width=15, fg_color="#FF7314",bg_color="#FDB678", text_color="white", command=botao_remover)
botao_editar.place(x=3, y=408)

root.mainloop()