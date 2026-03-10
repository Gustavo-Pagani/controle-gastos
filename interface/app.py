import tkinter as tk
from tkinter import ttk
from services.crud import salvar_transacao


def salvar():
    descricao = entrada_descricao.get()
    valor = entrada_valor.get()
    tipo = tipo_var.get()

    salvar_transacao(descricao, valor, tipo)

    entrada_descricao.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)


def iniciar_app():

    global entrada_descricao
    global entrada_valor
    global tipo_var

    janela = tk.Tk()
    janela.title("Controle de Gastos")
    janela.geometry("400x300")

    titulo = tk.Label(janela, text="Controle de Gastos", font=("Arial", 16))
    titulo.pack(pady=10)

    label_desc = tk.Label(janela, text="Descrição")
    label_desc.pack()

    entrada_descricao = tk.Entry(janela)
    entrada_descricao.pack()

    label_valor = tk.Label(janela, text="Valor")
    label_valor.pack()

    entrada_valor = tk.Entry(janela)
    entrada_valor.pack()

    label_tipo = tk.Label(janela, text="Tipo")
    label_tipo.pack()

    tipo_var = tk.StringVar()

    tipo_menu = ttk.Combobox(janela, textvariable=tipo_var)
    tipo_menu["values"] = ("despesa", "receita")
    tipo_menu.pack()

    botao = tk.Button(janela, text="Salvar", command=salvar)
    botao.pack(pady=10)

    janela.mainloop()