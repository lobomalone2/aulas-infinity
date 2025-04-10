import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"

    tarefas = []

    def adicionar_clicado(e):
        if nova_tarefa.value:
            tarefas.append({"descricao": nova_tarefa.value, "status": "pendente"})
            atualizar_lista()
            nova_tarefa.value = ""
            page.update()

    def atualizar_lista():
        lista_de_tarefas_control.controls.clear()
        for indice, tarefa in enumerate(tarefas):
            lista_de_tarefas_control.controls.append(
                ft.Text(f"[{indice}] {tarefa['descricao']} - {tarefa['status']}")
            )
        page.update()

    nova_tarefa = ft.TextField(label="Nova Tarefa")
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_clicado)
    lista_de_tarefas_control = ft.Column()

    page.add(
        ft.Row(
            [
                nova_tarefa,
                botao_adicionar,
            ]
        ),
        lista_de_tarefas_control,
    )

if __name__ == "__main__":
    ft.app(target=main)