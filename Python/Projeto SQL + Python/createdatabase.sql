CREATE DATABASE  spotifyclone;

USE spotifyclone;


CREATE TABLE artistas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    genero VARCHAR(50)	

);

CREATE TABLE albuns (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    ano_lancamento YEAR
);

CREATE TABLE musicas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    duracao TIME
    -- faltam criar colunas !!

)
