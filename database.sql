CREATE DATABASE controle_gastos;

USE controle_gastos;

CREATE TABLE transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    valor DECIMAL(10,2),
    tipo VARCHAR(20),
    data DATE
);

