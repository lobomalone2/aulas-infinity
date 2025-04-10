USE spotifyclone;
-- ex 1

SELECT 
	Musicas.titulo AS titulo,
	Artistas.nome AS nome

FROM 
	Musicas
    
INNER JOIN
	Artistas ON Musicas.id_artista = Artistas.id;
    
-- ex 2

SELECT
	Musicas.titulo AS titulo,
    Albuns.nome AS nome
    
FROM Musicas

INNER JOIN 
	Albuns ON Musicas.id_album = Albuns.id;
    
-- ex 3

SELECT
	Musicas.titulo AS titulo,
    Artistas.genero AS genero
    
FROM
	Musicas
    
INNER JOIN 
	Artistas ON Musicas.id_artista = Artistas.id;

-- ex 4

SELECT
    Musicas.titulo AS titulo,
    Playlists.nome AS nome
    
FROM
    Playlists
    
INNER JOIN

    Playlist_musicas ON Playlists.id = Playlist_musicas.id_playlist
    
INNER JOIN

    Musicas ON Playlist_musicas.id_musica = Musicas.id
    
LIMIT 0, 1000;

-- ex 6

SELECT
    Artistas.nome AS nome,
    COUNT(Musicas.id) AS quantidade
    
FROM

    Artistas
    
LEFT JOIN

    Musicas ON Artistas.id = Musicas.id_artista
    
GROUP BY

    Artistas.nome;
    
-- ex 7

SELECT
	COUNT(Musicas.id) AS quantidade
    
FROM 

	Musicas;

-- ex 8
SELECT AVG(Musicas.duracao) AS Duracao_media
    
FROM
	Musicas;
    
-- ex 9

SELECT 

	Albuns.nome AS Album,
    Albuns.ano_lancamento  AS ano_recente

    
FROM 
	Albuns
    
ORDER BY 
	ano_lancamento ASC

LIMIT 1;

SELECT 

	Albuns.nome AS Album,
    Albuns.ano_lancamento  AS ano_antigo

    
FROM 
	Albuns
    
ORDER BY 
	ano_lancamento DESC

LIMIT 1;


SELECT 
	
    COUNT(Usuarios.plano) AS quantidade_gratis

FROM
	
    Usuarios
    
WHERE

	Usuarios.plano = 'Grátis';

SELECT 
	
    COUNT(Usuarios.plano) AS quantidade_premium

FROM
	
    Usuarios
    
WHERE

	Usuarios.plano = 'Premium';



-- ex 10

SELECT
	Albuns.nome AS nome,
	SEC_TO_TIME(SUM(TIME_TO_SEC(duracao))) AS tempo_total
FROM
	Albuns,
	Musicas
WHERE 
	id_album = 3;

-- ex 13

SELECT
    Artistas.nome AS Nome_do_Artista,
    count(Musicas.id) as quantidade_musicas
FROM
    Artistas
INNER JOIN
    Musicas ON Artistas.id = Musicas.id_artista
GROUP BY
    Artistas.nome
ORDER BY
    COUNT(Musicas.id) DESC
    
LIMIT 1;

-- ex 14

SELECT

  u.nome,
  COUNT(p.id) AS quantidade_playlists
  
FROM

  Usuarios u
  
JOIN

  Playlists p ON u.id = p.id_usuario
  
GROUP BY

  u.id
  
ORDER BY

  quantidade_playlists ASC
  
LIMIT 1;

-- ex 15

SELECT

    u.nome AS nome_usuario,
    COUNT(pm.id_musica) AS quantidade_musicas
    
FROM

    Usuarios u
    
LEFT JOIN

    Playlists p ON u.id = p.id_usuario
    
LEFT JOIN

    Playlist_Musicas pm ON p.id = pm.id_playlist
    
GROUP BY

    u.id, u.nome
    
ORDER BY

    quantidade_musicas DESC;
    
-- ex 16

SELECT
    m.titulo AS nome_musica,
    a.nome AS nome_artista,
    al.nome AS nome_album,
    m.duracao AS duracao_musica
FROM
    Musicas m
JOIN
    Artistas a ON m.id_artista = a.id
JOIN
    Albuns al ON m.id_album = al.id;


-- ex 17

SELECT

    a.nome AS nome_artista,
    COUNT(m.id) AS quantidade_musicas,
    SEC_TO_TIME(SUM(TIME_TO_SEC(m.duracao))) AS duracao_total
    
FROM

    Artistas a
    
JOIN

    Musicas m ON a.id = m.id_artista
    
GROUP BY

    a.id, a.nome
    
ORDER BY

    quantidade_musicas DESC;

-- ex 18

SELECT

    p.nome AS nome_playlist,
    u.nome AS nome_usuario,
    COUNT(pm.id_musica) AS quantidade_musicas
    
FROM

    Playlists p
    
JOIN

    Usuarios u ON p.id_usuario = u.id
    
LEFT JOIN

    Playlist_Musicas pm ON p.id = pm.id_playlist
    
GROUP BY

    p.id, p.nome, u.nome
    
ORDER BY

    quantidade_musicas DESC;
    
-- ex 19

SELECT

    al.nome AS nome_album,
    a.nome AS nome_artista,
    COUNT(m.id) AS total_musicas
    
FROM

    Albuns al
    
JOIN

    Musicas m ON al.id = m.id_album
    
JOIN

    Artistas a ON m.id_artista = a.id
    
GROUP BY

    al.id, al.nome, a.id, a.nome
    
ORDER BY

    total_musicas DESC;

-- ex 20
SELECT
    u.nome AS nome_usuario,
    SEC_TO_TIME(SUM(TIME_TO_SEC(m.duracao))) AS duracao_total
    
FROM

    Usuarios u
    
JOIN

    Playlists p ON u.id = p.id_usuario
    
JOIN

    Playlist_Musicas pm ON p.id = pm.id_playlist
    
JOIN
    Musicas m ON pm.id_musica = m.id
    
GROUP BY

    u.id, u.nome
    
ORDER BY

    duracao_total DESC;
		
-- ex 21
SELECT

    a.nome AS nome_artista,
    COUNT(m.id) AS quantidade_musicas
    
FROM

    Artistas a
    
JOIN

    Musicas m ON a.id = m.id_artista
    
GROUP BY

    a.id, a.nome
    
ORDER BY

    quantidade_musicas DESC
    
LIMIT 1;

-- ex 22

SELECT
    u.nome AS nome_usuario
    
FROM

    Usuarios u
    
JOIN

    Playlists p ON u.id = p.id_usuario
    
JOIN

    Playlist_Musicas pm ON p.id = pm.id_playlist
    
GROUP BY

    u.id, u.nome, p.id
    
HAVING
    COUNT(pm.id_musica) > 5;
    
-- ex 23

SELECT
    al.nome AS nome_album,
    COUNT(m.id) AS quantidade_musicas
    
FROM

    Albuns al
    
JOIN

    Musicas m ON al.id = m.id_album
    
GROUP BY

    al.id, al.nome
    
ORDER BY

    quantidade_musicas DESC
    
LIMIT 3;

-- ex 24

SELECT
    AVG(quantidade_musicas) AS media_musicas_por_playlist
    
FROM (

    SELECT
        COUNT(pm.id_musica) AS quantidade_musicas
        
    FROM
        Playlists p
        
    LEFT JOIN
        Playlist_Musicas pm ON p.id = pm.id_playlist
        
    GROUP BY
    
        p.id
        
) AS subconsulta;


-- ex 25

	SELECT

		u.nome AS nome_usuario,
		SEC_TO_TIME(SUM(TIME_TO_SEC(m.duracao))) AS duracao_total
		
	FROM

		Usuarios u
		
	JOIN

		Playlists p ON u.id = p.id_usuario
		
	JOIN

		Playlist_Musicas pm ON p.id = pm.id_playlist
		
	JOIN

		Musicas m ON pm.id_musica = m.id
		
	GROUP BY

		u.id, u.nome
		
	ORDER BY

		duracao_total DESC
		
	LIMIT 1;

    