# Toastfy - Biblioteca de Notificações Toast para Flet

`Toastfy` é uma biblioteca poderosa e flexível que permite a criação e exibição de notificações do tipo "toast" em aplicações Flet. Com `Toastfy`, você pode facilmente adicionar toasts de sucesso, erro e aviso às suas aplicações, personalizando a posição e o comportamento das notificações.

## Funcionalidades

- **Toasts de Sucesso, Erro e Aviso**: Notificações específicas para diferentes cenários.
- **Posicionamento Personalizável**: Escolha entre várias posições predefinidas na tela.
- **Integração Simples**: Fácil de integrar e usar em qualquer aplicação Flet.

![Diferentes toats gerados](https://raw.githubusercontent.com/webtechmoz/flet-toast/master/assets/float_toast.png)

## Instalação

Para instalar a biblioteca `Toastfy`, execute:

```bash
pip install flet_toast
```
## Exemplo de Uso

Abaixo está um exemplo simples de como utilizar a classe Toastfy em uma aplicação Flet:
```python
import flet as ft
from flet_toast import flet_toast

def main(page: ft.Page):
    page.title = "Exemplo de Toastfy"

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
                                        on_click=lambda e: flet_toast.success(
                                            page, 
                                            'Operação concluída com sucesso!', 
                                            'top_left'
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            )

        page.update()

    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)
```

## Documentação

### Métodos
`success(page: ft.Page, message: str, position: position = position.BOTTOM_RIGHT) -> Toast`
Exibe uma notificação toast de sucesso.

- page: A página Flet onde o toast será exibido.
- message: A mensagem a ser exibida no toast.
- position: A posição do toast na tela. O padrão é BOTTOM_RIGHT.

`error(page: ft.Page, message: str, position: position = position.BOTTOM_RIGHT) -> Toast`
Exibe uma notificação toast de erro.

- page: A página Flet onde o toast será exibido.
- message: A mensagem a ser exibida no toast.
- position: A posição do toast na tela. O padrão é BOTTOM_RIGHT.

`warning(page: ft.Page, message: str, position: position = position.BOTTOM_RIGHT) -> Toast`
Exibe uma notificação toast de aviso.

- page: A página Flet onde o toast será exibido.
- message: A mensagem a ser exibida no toast.
- position: A posição do toast na tela. O padrão é BOTTOM_RIGHT.

Enum `position`
position define as possíveis posições para exibir as notificações toast na tela. As opções incluem:

- `top_left`: Canto superior esquerdo.
- `top_right`: Canto superior direito.
- `bottom_left`: Canto inferior esquerdo.
- `bottom_right`: Canto inferior direito (padrão).

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENCE para mais detalhes.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório do GitHub.