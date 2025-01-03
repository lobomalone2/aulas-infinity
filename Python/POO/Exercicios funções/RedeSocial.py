from datetime import date


class Usuario():

    def __init__(self,username: str,nome: str = '',bio: str = '', amigos: list = None ,posts: list = None):
        self.nome = nome
        self.username = username
        self.bio = bio
        self.post = posts
        self.amigos = amigos

    def adicionar_amigo(self,amigo):

        self.amigos[0][self.username]['amigos'].append(amigo)

        print(f'{amigo} foi adicionado a sua lista de amigos!')


    def remover_amigo(self,amigo):

        # FAZER UM FOR PARA PERCORRER LISTA DE AMIGOS E REMOVER O AMIGO ESCOLHIDO PELO USUARIO


                self.amigos[0][self.username]['amigos'].remove(amigo)

                print(f'{amigo} foi removido da sua lista de amigos!')


            
             #NÃO DA PARA REMOVER ITEM PELO VALOR SEM UM FOR, APENAS A PARTIR DO INDICE

        
        

    def fazer_postagem(self,titulo: str,descricao: str, data: str):

        novo_post = {
                
                'titulo': titulo,
                'descricao': descricao,
                'data': data

            }            
        
        for user in self.post:

            if self.username in user:

                user[self.username]['posts'].append(novo_post)
                print(f'Conteúdo postado: {titulo} {descricao} data: {data}')
                return

        print(f'Usuário {self.username} não encontrado.')

        

        print(f'conteúdo postado:  {titulo} {descricao} data: {data}')

    def listar_postagens(self):

        for user in self.post:

            print(user[self.username]['posts'])
            
            return
        print(f'Usuário {self.username} não encontrado.')
        

class Postagem():

    def __init__(self,conteudo: str,data: str):
        self.conteudo = conteudo
        self.data = data
    
    def info(self):

        conteudos = self.conteudo
        data = self.data

        return conteudos,data
    
class Redesocial():

    def __init__(self,usuarios: list):
        
        self.usuarios = usuarios

    
    def criar_usuario(self,nome: str, username: str, bio: str):

        usuario_novo = {

             username: {
            'nome': nome,
            'bio':bio,
            'posts': [], # CRIA UMA LISTA SEPARADA BURRO
            'amigos': []

            }
        }

        self.usuarios.append(usuario_novo)

        print(f'Dados sobre novo usuario criado! \n {usuario_novo} ')        



    def buscar_usuario(self,username):

        for user in self.usuarios:

            if username in user:

                cruzausuario = user[username]

                print(cruzausuario)

                return

        print(f'Usuário {username} não encontrado.')


    def listar_usuarios(self):

        print(self.usuarios)


#FUNÇÕES DO PROGRAMA PRINCIPAL


def criarusuario():

        usuarionovo = Redesocial(usuarios)

        nome = input('Digite o seu nome: ')

        username = input('Digite o seu usuário: ')

        bio = input('Descrição do perfil: ')

        usuarionovo.criar_usuario(nome,username,bio)

        print(usuarios)

def buscarusuario():

        escolhausuario = input('Digite o Usuário a ser encontrado')

        buscarusuario = Redesocial(usuarios)

        buscarusuario.buscar_usuario(escolhausuario)

def listarusuarios():

        listarusuario = Redesocial(usuarios)

        listarusuario.listar_usuarios()

def listarpostagens():

        username = input('Digite o usuário :')

        listarpostagem = Usuario(username,'','','',usuarios)

        listarpostagem.listar_postagens()

def fazerpostagem():

        data = date.today()

        username = input('Digite o usuario')

        titulo = input('Digite o titulo da postagem')

        descricao = input('Digite a descrição da postagem')

        fazerpostagem = Usuario(username,usuarios,usuarios,usuarios,usuarios)

        fazerpostagem.fazer_postagem(titulo,descricao,data)

def adicionaramigo():


        username = input('Digite o seu nome de usuario')

        username_amigo = input('Digite o username do amigo a ser adicionado')

        adicionaramigo = Usuario(username,'','',usuarios,'')
       
        adicionaramigo.adicionar_amigo(username_amigo)

def removeramigo():

        username = input('Digite o seu nome de usuario')

        username_amigo = input('Digite o username do amigo a ser adicionado')

        removeramigo = Usuario(username,'','',usuarios,'')
       
        removeramigo.remover_amigo(username_amigo)
    


def menu():

    while True:

        print('Comandos: \n 1 - Criar usuario \n 2 - Buscar usuario \n 3 - Listar usuarios \n 4 - Fazer postagem \n 5 - Listar Postagens \n 6 - Adicionar amigos \n 7 - Remover amigo \n 8 - Encerrar programa ' )

        escolha = int(input('Digite a sua escolha de acordo com o menu'))

    #### CRIAR FUNÇÕES PARA EXECUTAR OS PASSOS ABAIXO!

        if escolha == 1:

            criarusuario()

        elif escolha == 2:

            buscarusuario()
    
        elif escolha == 3:

            listarusuarios()
  
    
        elif escolha == 4:

            fazerpostagem()


        elif escolha == 5:

            listarpostagens()

        elif escolha == 6:

            adicionaramigo()

        elif escolha == 7:

            removeramigo()

        elif escolha == 8:
            break
    
       
usuarios = [{

        'lobomalone': {'nome': 'lucas lobo', 'bio': 'Um lobo muito foda','posts':[{
    
        'titulo': 'Cada dia é uma batalha, uma chance de extrair o máximo de mim mesmo. Viver intensamente não é apenas um lema, é a minha essência.',
        'descricao': 'A intensidade com que vivo cada segundo reflete a paixão ardente que tenho pela vida. Não se trata apenas de alcançar metas, mas de viver cada instante com fúria e propósito.',
        'data':'23-12-2024'}],'amigos': ['amigo1','amigo2','amigo3']}
    
    }]


menu()
    









    





        