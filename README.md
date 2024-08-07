# Toastfy

A classe `Toastfy` fornece uma interface para criar e exibir diferentes tipos de notificações toast em uma aplicação Flet. Esta classe oferece métodos para toasts de sucesso, erro e aviso, incluindo a possibilidade de personalizar a posição dessas notificações.

## Exemplo de Uso

Aqui está um exemplo de como usar a classe `Toastfy` em uma aplicação Flet:

```python
import flet as ft
from flet_toastfy import Toastfy

def main(page: ft.Page):
    page.title = page.route

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(
                ft.View(
                    route='/',
                    bgcolor=ft.colors.SECONDARY,
                    controls=[
                        ft.SafeArea(
                            content=ft.Stack(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ANIMATION,
                                        icon_size=25,
                                        icon_color=ft.colors.BLUE,
                                        top=40,
                                        on_click=lambda e: Toastfy().success(page, 'Testado bem mesmo', 'top_left')
                                    )
                                ]
                            )
                        ),
                    ]
                )
            )

        page.title = page.route
        page.update()

    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)
```

## Métodos

### success(page: ft.Page, message: str, position: position = position.BOTTOM_RIGHT) -> Toast
Exibe uma notificação toast de sucesso.

**page**: A página Flet onde o toast será exibido.
**message**: A mensagem a ser exibida no toast.
**position**: A posição do toast na tela. O padrão é BOTTOM_RIGHT.

### error(page: ft.Page, message: str, position: position = position.BOTTOM_RIGHT) -> Toast
Exibe uma notificação toast de erro.

**page**: A página Flet onde o toast será exibido.
**message**: A mensagem a ser exibida no toast.
**position**: A posição do toast na tela. O padrão é BOTTOM_RIGHT.

### warning(page: ft.Page, message: str, position: position = position.BOTTOM_RIGHT) -> Toast
Exibe uma notificação toast de aviso.

**page**: A página Flet onde o toast será exibido.
**message**: A mensagem a ser exibida no toast.
**position**: A posição do toast na tela. O padrão é BOTTOM_RIGHT.

### __position_string__(pos: position) -> str
Converte um enum ou string de posição para sua representação em string.

**pos**: O enum ou string de posição.

## Atributos

### position
Enum contendo possíveis posições para notificações toast.
    1. *top_left* - posiciona no canto superior esquerdo da pagina
    2. *top_right* - posiciona no canto superior direito da pagina
    1. *bottom_left* - posiciona no canto inferior esquerdo da pagina
    2. *bottom_right* - posiciona no canto inferior direito da pagina