
DROP DATABASE spotifyclone;

CREATE DATABASE  spotifyclone;



USE spotifyclone;

-- ex 2

CREATE TABLE Usuarios (
	id	INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_nascimento DATE,
    plano VARCHAR(10) CHECK (plano IN ('Grátis', 'Premium'))
);

-- ex 2.1

INSERT INTO
	  Usuarios (nome,email,data_nascimento,plano)
VALUES

		('Ana Souza','ana@email.com','1995-04-10','Premium'),
		('Carlos Mendes','carlos@email.com','2000-06-15','Grátis'),
		('Pedro Silva','pedro@email.com','2003-02-02','Grátis'),
		('Lucas Lobo','lucaslobo@email.com','1998-06-16','Premium');

 UPDATE usuarios

 SET email = "carlos@gmail.com"

WHERE id = 2;

DELETE FROM
	usuarios
WHERE
	id = 3;

-- ex 3


CREATE TABLE Artistas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    genero VARCHAR(50)

);


CREATE TABLE Albuns (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    ano_lancamento YEAR
);


-- ex 4


INSERT INTO 
	Artistas(nome, genero)
    
VALUES
	('The Weeknd','R&B'),
    ('Imagine Dragons','Rock'),
    ('Tribo da Periferia','Hip Hop');
    
INSERT INTO 

	Albuns(nome,ano_lancamento)
    
VALUES

	('After Hours',2020),
    ('Evolve',2017),
	('Hibrido',2021);
    
 -- ex 5
CREATE TABLE Musicas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    duracao TIME,
    id_artista INT,
    id_album INT,
    FOREIGN KEY (id_artista) REFERENCES Artistas(id),
    FOREIGN KEY (id_album) REFERENCES Albuns(id)

);

-- ex 6

INSERT INTO

	Musicas(titulo,duracao,id_album)
    
VALUES

	('Blinding Lights','00:03:20',1),
    ('Believer','00:03:24',2),
    ('Tema','00:03:05',3),
    ('Insonia','00:04:43',3);
    

-- ex 7

CREATE TABLE Playlists (
	id	INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    nome VARCHAR(100)
    );

CREATE TABLE Playlist_Musicas(
	id_playlist INT,
    id_musica INT,
    PRIMARY KEY (id_playlist,id_musica),
	FOREIGN KEY (id_playlist) REFERENCES Playlists(id),
    FOREIGN KEY (id_musica)	  REFERENCES musicas(id)
);


INSERT INTO 

	Playlists(nome,id_usuario)
    
VALUES

	('Minhas Favoritas',1),
    ('Treino',2);

INSERT INTO 

	Playlist_Musicas(id_playlist,id_musica)

VALUES
	
    (1,2);

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE Albuns;
TRUNCATE TABLE Artistas;
TRUNCATE TABLE Musicas;
TRUNCATE TABLE Playlist_musicas;
TRUNCATE TABLE playlists;
TRUNCATE TABLE Usuarios;
SET FOREIGN_KEY_CHECKS = 1;




	

    
	



