import random




def criarfrase_animal():

    estruturas = [

    "Gere uma imagem  realista de um(a) [substantivo] [verbo] no(a) [substantivo2]",
    'Gere uma imagem cartonizada de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem em aquarela de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem surrealista de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem cubista de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem vetorizada de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem de uma ilustração digital de um(a) [substantivo] [verbo] no(a) [substantivo2]'

]
    estrutura = random.choice(estruturas)

    frase = estrutura.replace("[substantivo]", random.choice(CodigoFrase[0]['categorias']['animal']['substantivos']), 1)

    frase = frase.replace("[verbo]", random.choice(CodigoFrase[0]['categorias']['animal']['verbos']), 1)
    frase = frase.replace("[adjetivo]", random.choice(CodigoFrase[0]['categorias']['animal']['adjetivos']), 1)
    frase = frase.replace("[substantivo2]", random.choice(CodigoFrase[0]['categorias']['animal']['substantivos2']), 1)
    

    return frase

def criarfrase_natureza():

    estruturas = [

    "Gere uma imagem  realista de um(a) [substantivo] [verbo] no(a) [substantivo2]",
    'Gere uma imagem cartonizada de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem em aquarela de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem surrealista de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem cubista de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem vetorizada de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem de uma ilustração digital de um(a) [substantivo] [verbo] no(a) [substantivo2]'

]
    estrutura = random.choice(estruturas)

    frase = estrutura.replace("[substantivo]", random.choice(CodigoFrase[0]['categorias']['natureza']['substantivos']), 1)

    frase = frase.replace("[verbo]", random.choice(CodigoFrase[0]['categorias']['natureza']['verbos']), 1)
    frase = frase.replace("[adjetivo]", random.choice(CodigoFrase[0]['categorias']['natureza']['adjetivos']), 1)
    frase = frase.replace("[substantivo2]", random.choice(CodigoFrase[0]['categorias']['natureza']['substantivos2']), 1)
    

    return frase

def criarfrase_tecnologia():

    estruturas = [

    "Gere uma imagem  realista de um(a) [substantivo] [verbo] no(a) [substantivo2]",
    'Gere uma imagem cartonizada de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem em aquarela de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem surrealista de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem cubista de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem vetorizada de um(a) [substantivo] [verbo] no(a) [substantivo2]',
    'Gere uma imagem de uma ilustração digital de um(a) [substantivo] [verbo] no(a) [substantivo2]'

]
    estrutura = random.choice(estruturas)

    frase = estrutura.replace("[substantivo]", random.choice(CodigoFrase[0]['categorias']['tecnologia']['substantivos']), 1)

    frase = frase.replace("[verbo]", random.choice(CodigoFrase[0]['categorias']['tecnologia']['verbos']), 1)
    frase = frase.replace("[adjetivo]", random.choice(CodigoFrase[0]['categorias']['tecnologia']['adjetivos']), 1)
    frase = frase.replace("[substantivo2]", random.choice(CodigoFrase[0]['categorias']['tecnologia']['substantivos2']), 1)
    

    return frase



# PROGRAMA PRINCIPAL

CodigoFrase = [{'categorias':
                
                # 'substantivo' pode ser um objeto e substantivo 2 uma 'localidade'
                # 'adjetivos' se remete a uma aparência ou sentimento
                
                {
                'animal':{

                'substantivos': ['gato','cachorro','elefante','onça','leão','tigre','Canindé Macaw','girafa','leopardo','zebra','gorila','hipopótamo','rinoceronte',
                                 'Cheetah','Panda','crocodilo','águia','flamingo','pinguin','coelho','golfinho','baleia','peixe'],
                                 
                'substantivos2': ['floresta','pasto','rio','telhado','espaço sideral','marte','saturno','lua','ilha','geladeira','polo norte','deserto',
                                  'praça','escola','costa','bosque','cachoeira','mercado','inverno','outono','estrada de terra','estrada de ferro'],

                'verbos':['correndo','saltando','dirigindo','construindo','chorando','sorrindo','trabalhando','capinando lote','trabalhando no açougue',
                          'estudando','malhando','lutando'],
                'adjetivos':['rápido','selvagem','devagar','roupas rasgadas']},

                'natureza':{

                'substantivos': ['onça','aranha','cobra','beija flor','flor','arvore','planta','dinossauro','passaro','indigena'],
                'substantivos2':['montanha', 'floresta','tribo','acampamento','base militar','praia',' ilha isolada','montanha congelada'],
                'verbos':['aprendendo','flundo','voaando','nadando','florescendo','crescendo','avançando','atacando','nascendo','evoluindo'],
                'adjetivos':['verde','selvagem','tranquilo','ansioso','nervoso','calmo','suave','feliz'] },
                
                'tecnologia': {

                'substantivos': ['computador', 'robô', 'software', 'internet', 'smartphone','carro voador'],
                'substantivos2':['escritorio','interior da nave espacial',' coliseu futuristico',],
                'verbos': ['programar', 'conectar', 'atualizar', 'digitalizar', 'inovar'],
                'adjetivos': ['moderno', 'avançado', 'digital']}, # parei aqui

                'esportes': {

                'substantivos': ['bola', 'campo', 'jogador', 'gol', 'competição'],
                'verbos': ['correr', 'chutar', 'jogar', 'vencer', 'treinar'],
                'adjetivos': ['rápido', 'ágil', 'competitivo']},

                'culinária': {

                'substantivos': ['prato', 'ingrediente', 'receita', 'cozinha', 'chef'],
                'verbos': ['cozinhar', 'assar', 'misturar', 'temperar', 'servir'],
                'adjetivos': ['delicioso', 'saboroso', 'picante']},

                'viagens': {

                'substantivos': ['destino', 'turista', 'mapa', 'hotel', 'cultura'],
                'verbos': ['viajar', 'explorar', 'descobrir', 'visitar', 'reservar'],
                'adjetivos': ['exótico', 'distante', 'cultural']},

                'educação': {
                     
                'substantivos': ['livro', 'escola', 'professor', 'aluno', 'aula'],
                'verbos': ['aprender', 'ensinar', 'estudar', 'ler', 'escrever'],
                'adjetivos': ['educativo', 'instrutivo', 'acadêmico']},

                 'arte': {
                     
                'substantivos': ['pintura', 'escultura', 'galeria', 'artista', 'obra'],
                'verbos': ['pintar', 'esculpir', 'criar', 'exibir', 'inspirar'],
                'adjetivos': ['criativo', 'expressivo', 'visual']},

                'música': {

                'substantivos': ['instrumento', 'concerto', 'melodia', 'banda', 'canção'],
                'verbos': ['tocar', 'cantar', 'compor', 'ouvir', 'ensaiar'],
                'adjetivos': ['harmônico', 'melódico', 'rítmico']},

                'história': {

                'substantivos': ['evento', 'figura', 'monumento', 'era', 'civilização'],
                'verbos': ['acontecer', 'recordar', 'construir', 'descobrir', 'narrar'],
                'adjetivos': ['histórico', 'antigo', 'significativo']},

                'moda': {

                'substantivos': ['roupa', 'acessório', 'tendência', 'desfile', 'estilista'],
                'verbos': ['vestir', 'combinar', 'desenhar', 'modelar', 'criar'],
                'adjetivos': ['elegante', 'moderno', 'estiloso']},


                'saúde': {


                'substantivos': ['exercício', 'dieta', 'bem-estar', 'médico', 'paciente'],
                'verbos': ['exercitar', 'alimentar', 'cuidar', 'tratar', 'prevenir'],
                'adjetivos': ['saudável', 'fit', 'nutritivo']},

                'ciência': {

                'substantivos': ['experimento', 'descoberta', 'laboratório', 'teoria', 'cientista'],
                'verbos': ['pesquisar', 'experimentar', 'descobrir', 'analisar', 'provar'],
                'adjetivos': ['científico', 'experimental', 'teórico']},

                'ficção': {

                'substantivos': ['personagem', 'cenário', 'história', 'fantasia', 'aventura'],
                'verbos': ['imaginar', 'criar', 'narrar', 'explorar', 'sonhar'],
                'adjetivos': ['fictício', 'imaginário', 'fantástico']},

                'arquitetura': {

                'substantivos': ['edifício', 'ponte', 'design', 'estrutura', 'arquiteto'],
                'verbos': ['construir', 'projetar', 'desenhar', 'reformar', 'planejar'],
                'adjetivos': ['arquitetônico', 'estrutural', 'moderno']},

                'transporte': {

                'substantivos': ['carro', 'avião', 'trem', 'bicicleta', 'ônibus'],
                'verbos': ['dirigir', 'voar', 'viajar', 'pedalar', 'transportar'],
                'adjetivos': ['rápido', 'eficiente', 'seguro']}    
                 
                  }}]



frase1 = criarfrase_animal()
frase2 = criarfrase_natureza()
frase3 = criarfrase_tecnologia()



print(frase1)
print(frase2)
print(frase3)







































