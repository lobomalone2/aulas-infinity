from classes import Painel



def menuprincipal(escolha):
    print('Digite "I"  para Iniciar combate ou "S" para sair do jogo ')
   
    while True:
        entrada = input('Digite a opção desejada:')
        if escolha == 'I':
            print("FOI!")

        elif escolha == 'S':
            break

        else:
            
            print("Num foi.")

            


        
    
        

menuprincipal()