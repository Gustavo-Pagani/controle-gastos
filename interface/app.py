import tkinter as tk
from tkinter import ttk, messagebox
from services.crud import salvar_transacao, listar_transacoes, deletar_transacao


def atualizar_tabela():

    for item in tabela.get_children():
        tabela.delete(item)

    dados = listar_transacoes()

    for linha in dados:
        tabela.insert("", tk.END, values=linha)

def mostrar_botao_deletar(event):
    
    selecionado = tabela.selection()

    if selecionado:
        botao_deletar.pack(pady=5)

def deletar():
    
    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showerror("Erro", "Selecione uma transação!.")
        return

    item = tabela.item(selecionado)
    dados = item["values"]

    id_transacao = dados[0]

    confirmar = messagebox.askyesno(
        "confirmar",
        "Deseja deletar esta transação?"
    )

    if confirmar:
        deletar_transacao(id_transacao)
        atualizar_tabela()
        botao_deletar.pack_forget()
        
def salvar():

    descricao = entrada_descricao.get()
    valor = entrada_valor.get()
    tipo = tipo_var.get()

    if not descricao or not valor or not tipo:
        messagebox.showerror("Erro", "Preencha todos os campos!.")
        return
    
    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor númerico válido!.")
        return 

    salvar_transacao(descricao, valor, tipo)

    entrada_descricao.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)

    atualizar_tabela()

    messagebox.showinfo("Sucesso", "Transação salva com sucesso!.")


def iniciar_app():

    global entrada_descricao
    global entrada_valor
    global tipo_var
    global tabela
    global botao_deletar

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

    tipo_menu = ttk.Combobox(frame, textvariable=tipo_var, state="readonly")
    tipo_menu["values"] = ("despesa", "receita")
    tipo_menu.grid(row=2, column=1)

    # -----------------------------
    # Botão salvar
    # -----------------------------
    botao = tk.Button(frame, text="Salvar", command=salvar)
    botao.grid(row=3, columnspan=2, pady=10)

    # -----------------------------
    # Botão deletar
    # -----------------------------
    botao_deletar = tk.Button(janela, text="Deletar", command=deletar,bg="red",fg="white")
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

    tabela.column("id", width=50)
    tabela.column("descricao", width=200)
    tabela.column("valor", width=100)
    tabela.column("tipo", width=100)
    tabela.column("data", width=120)



    tabela.pack(pady=20, fill="x")

    tabela.bind("<<TreeviewSelect>>", mostrar_botao_deletar)

    # carrega dados iniciais
    atualizar_tabela()

    # inicia loop da interface
    janela.mainloop()