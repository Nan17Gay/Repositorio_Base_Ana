import flet as ft

def main(page: ft.Page):
    page.theme_mode="dark"

    if "Nana" in log:
        print("✅ Acesso permitido")
    else:
        print("❌ Acesso negado")

    def clique(e):
        print("Sim")
    login = ft.Text("Login", size=30,color="blue")
    log = ft.TextField(label="Usuário",border_color="Purple")
    senha = ft.TextField(label="Senha",password=True,can_reveal_password=True,border_color="Purple")
    botao = ft.ElevatedButton("Clique aqui!",on_click=clique)
    page.add(login,log,senha,botao)

ft.app(target=main)