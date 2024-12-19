import time
import random

class Painel:
    
    def __init__(self, iniciar: str, sair: str ):
        self.iniciar = iniciar
        self.sair = sair


class NPC:

    def __init__(self,nome,dano,defesa, stamina: int, hp: int):
        self.nome = nome
        self.hp = hp
        self.dano = dano
        self.defesa = defesa
        self.stamina = stamina
    
    # Ataques

    def chute(self): #1 ALTERA OS ATRIBUTOS DO PERSONAGEM AO SER EXECUTADA

        self.defesa = -10
        self.dano += 15
        self.stamina = -5
        print(f'Defesa: {self.defesa} \n Dano:  {self.dano} \n Stamina: {self.stamina}')

    
    def soco(self): #1
        self.defesa = -2
        self.dano = + 6
        self.stamina = - 3
        print(f'Defesa: {self.defesa} \n Dano:  {self.dano} \n Stamina: {self.stamina}')

    def cotovelada(self): #1
        self.defesa = -1
        self.dano = + 18
        self.stamina = - 4
        print(f'Defesa: {self.defesa} \n Dano:  {self.dano} \n Stamina: {self.stamina}')
        

    # Defesas

    def bloqueio(self): #1 
        self.defesa =  + 10
        self.dano  = - 3.5
        self.stamina = -1
        print(f'Defesa: {self.defesa} \n Dano:  {self.dano} \n Stamina: {self.stamina}')

    def esquiva(self): #1
        self.stamina = -2
        print(f'Stamina: {self.stamina}')

    # Recuperação de stamina

    def descansar(self): #1

        while self.stamina < 200:
            time.sleep(3)
            self.stamina += 30

    def saude(self): #1
                
        self.hp -= self.dano



#Função HP

def HP(vidapc,vidauser):
    
    if vidauser.hp == 0:

        print('Game Over')

    elif vidapc.hp == 0:

            print('You Win!')


#COMBATE

def combate(comando: int):

    if comando == 1:
        player.chute()
        dano = computador.hp - player.dano
        print(f'Dano infligido{dano}')

    elif comando == 2:
        

    





player = NPC('Valdemorth',30,15,200,100)
computador = NPC('Madara',35,13,240,100)





