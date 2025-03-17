INSERT INTO
	 usuarios (nome,email,data_nascimento,plano)
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
	id = 3
    