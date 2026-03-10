import tkinter as tk


def iniciar_app():
    janela = tk.Tk()
    janela.title("Controle de Gastos")
    janela.geometry("400x300")

    titulo = tk.Label(
        janela,
        text="Sistema de Controle de Gastos",
        font=("Arial", 14)
    )

    titulo.pack(pady=20)

    janela.mainloop()