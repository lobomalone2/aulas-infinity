import flet as ft

def main(page: ft.Page):

    page.title = "Formulário de contato"

    nome = ft.TextField(label="Digite seu nome")

    email = ft.TextField(label="Digite o email")

    mensagem = ft.TextField(label="Digite a mensagem")


    def btn_click(e):
        nome_digitado = nome.value
        page.add(ft.Text(f'Olá,{nome_digitado}, formúlário enviado com sucesso!'))
        page.update()


    btn_enviar = ft.OutlinedButton(text="Enviar", on_click=btn_click)

    page.add(
        nome,
        email,
        mensagem,
        btn_enviar
    )


ft.app(target=main)