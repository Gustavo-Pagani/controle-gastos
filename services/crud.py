from database.db import conectar_banco
from datetime import date


def salvar_transacao(descricao, valor, tipo):

    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO transacoes (descricao, valor, tipo, data)
    VALUES (%s, %s, %s, %s)
    """

    dados = (descricao, valor, tipo, date.today())

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

def listar_transacoes():

    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = "SELECT * FROM transacoes"

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados