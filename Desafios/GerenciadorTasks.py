def adicionar_tarefa(descricao_informada: str):

    tarefa_nova = {

        "descricao": descricao_informada,

        "status": "pendente"

    }

    tarefas.append(tarefa_nova)



def listar_tarefas(lista_de_tarefas: list):

    for indice, tarefa in enumerate(lista_de_tarefas):

        print(f"[{indice}] {tarefa['descricao']} - {tarefa['status']}")




def marcar_concluida(tarefaconcluida: int, listar_tarefas: list):

        tarefas[tarefaconcluida]['status'] = 'concluído'

        for indice, tarefa in enumerate(listar_tarefas, start=1):
             
             print(f'[{indice}] {tarefa['descricao']} - {tarefa['status']}')



def remover_tarefa(codigotarefa: int, listar_tarefas: list):
     
    tarefas.pop(codigotarefa)

    for indice, tarefa in enumerate(listar_tarefas):

        print(f'[{indice}] {tarefa['descricao']} - {tarefa['status']}')


# PROGRAMA PRINCIPAL


tarefas = [

    {"descricao": "estudar python", "status": "pendente"},

    {"descricao": "fazer supermercado", "status": "concluído"},

]

#Adicionar tarefa

descricao = input('Digite a descrição da tarefa')

adicionar_tarefa(descricao)


# listar tarefa
listar_tarefas(tarefas)

#marcar tarefa como concluída

tarefaconcluida = int(input('Digite o numero da tarefa que voce concluiu'))
marcar_concluida(tarefaconcluida,tarefas)

# remover tarefas

remover = int(input('Digite o numero da tarefa a ser removida!'))

remover_tarefa(remover,tarefas)