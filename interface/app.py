import tkinter as tk
from tkinter import ttk
from services.crud import salvar_transacao, listar_transacoes


def atualizar_tabela():

    for item in tabela.get_children():
        tabela.delete(item)

    dados = listar_transacoes()

    for linha in dados:
        tabela.insert("", tk.END, values=linha)


def salvar():

    descricao = entrada_descricao.get()
    valor = entrada_valor.get()
    tipo = tipo_var.get()

    salvar_transacao(descricao, valor, tipo)

    entrada_descricao.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)

    atualizar_tabela()


def iniciar_app():

    global entrada_descricao
    global entrada_valor
    global tipo_var
    global tabela

    # cria a janela principal
    janela = tk.Tk()
    janela.title("Controle de Gastos")
    janela.geometry("600x400")

    # título da aplicação
    titulo = tk.Label(janela, text="Controle de Gastos", font=("Arial", 16))
    titulo.pack(pady=10)

    # frame para organizar os campos do formulário
    frame = tk.Frame(janela)
    frame.pack()

    # -----------------------------
    # Campo descrição
    # -----------------------------
    tk.Label(frame, text="Descrição").grid(row=0, column=0)
    entrada_descricao = tk.Entry(frame)
    entrada_descricao.grid(row=0, column=1)

    # -----------------------------
    # Campo valor
    # -----------------------------
    tk.Label(frame, text="Valor").grid(row=1, column=0)
    entrada_valor = tk.Entry(frame)
    entrada_valor.grid(row=1, column=1)

    # -----------------------------
    # Campo tipo (receita ou despesa)
    # -----------------------------
    tk.Label(frame, text="Tipo").grid(row=2, column=0)

    tipo_var = tk.StringVar()

    tipo_menu = ttk.Combobox(frame, textvariable=tipo_var)
    tipo_menu["values"] = ("despesa", "receita")
    tipo_menu.grid(row=2, column=1)

    # -----------------------------
    # Botão salvar
    # -----------------------------
    botao = tk.Button(frame, text="Salvar", command=salvar)
    botao.grid(row=3, columnspan=2, pady=10)

    # -----------------------------
    # Tabela de transações
    # -----------------------------
    tabela = ttk.Treeview(
        janela,
        columns=("id", "descricao", "valor", "tipo", "data"),
        show="headings"
    )

    # nomes das colunas
    tabela.heading("id", text="ID")
    tabela.heading("descricao", text="Descrição")
    tabela.heading("valor", text="Valor")
    tabela.heading("tipo", text="Tipo")
    tabela.heading("data", text="Data")

    tabela.pack(pady=20)

    # carrega dados iniciais
    atualizar_tabela()

    # inicia loop da interface
    janela.mainloop()