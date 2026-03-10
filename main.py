from database.db import conectar_banco


def testar_conexao():
    try:
        conexao = conectar_banco()
        print("Conectado ao MySQL com sucesso!")
        conexao.close()

    except Exception as erro:
        print("Erro ao conectar:", erro)


if __name__ == "__main__":
    testar_conexao()