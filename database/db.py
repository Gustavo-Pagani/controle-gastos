import mysql.connector
from database import config


def conectar_banco():
    conexao = mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE
    )

    return conexao