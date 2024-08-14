import random
import flet as ft

def gerar_senha(tamanho, incluir_numeros, incluir_maiúsculas, incluir_caracteres):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    if incluir_numeros:
        caracteres += "0123456789"
    if incluir_maiúsculas:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if incluir_caracteres:
        caracteres += "!@#$%^&*"
    
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main(page: ft.Page):
    page.title = "Gerador de Senhas"
    page.padding = 20
    page.spacing = 20
    page.horizontal_alignment = "center"

    # Título
    page.add(ft.Text("Gerador de Senhas", size=30, weight="bold", text_align="center"))

    # Input para o tamanho da senha
    tamanho_input = ft.TextField(label="Tamanho da Senha", value="8", width=150, text_align="center")

    # Switches para incluir ou não números, maiúsculas e caracteres especiais
    incluir_numeros_switch = ft.Switch(label="Incluir Números", value=True)
    incluir_maiúsculas_switch = ft.Switch(label="Incluir Maiúsculas", value=True)
    incluir_caracteres_switch = ft.Switch(label="Incluir Caracteres Especiais", value=True)

    # Campo para mostrar a senha gerada
    senha_texto = ft.Text(value="", size=20, selectable=True, weight="bold", text_align="center")

    # Função chamada ao clicar no botão "Gerar Senha"
    def gerar_senha_click(e):
        try:
            tamanho = int(tamanho_input.value)
            if tamanho < 4 or tamanho > 50:
                raise ValueError("Tamanho deve estar entre 4 e 50.")
        except ValueError as ve:
            senha_texto.value = f"Erro: {str(ve)}"
            copiar_button.disabled = True
        else:
            incluir_numeros = incluir_numeros_switch.value
            incluir_maiúsculas = incluir_maiúsculas_switch.value
            incluir_caracteres = incluir_caracteres_switch.value

            senha = gerar_senha(tamanho, incluir_numeros, incluir_maiúsculas, incluir_caracteres)
            senha_texto.value = senha
            copiar_button.disabled = False

        page.update()

    # Função para copiar a senha gerada para a área de transferência
    def copiar_senha_click(e):
        if senha_texto.value:
            page.set_clipboard(senha_texto.value)
            page.snack_bar = ft.SnackBar(ft.Text("Senha copiada!"), open=True)
            page.update()

    # Botão para gerar a senha
    gerar_button = ft.ElevatedButton(text="Gerar Senha", on_click=gerar_senha_click)

    # Botão para copiar a senha
    copiar_button = ft.ElevatedButton(text="Copiar Senha", on_click=copiar_senha_click, disabled=True)

    # Layout da página com organização melhorada
    page.add(
        ft.Column([
            ft.Row([
                tamanho_input,
                gerar_button,
                copiar_button
            ], alignment="center", spacing=10),
            ft.Row([
                incluir_numeros_switch,
                incluir_maiúsculas_switch,
                incluir_caracteres_switch
            ], alignment="center", spacing=20),
            senha_texto
        ], spacing=20)
    )

ft.app(target=main)
