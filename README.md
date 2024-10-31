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
    page.theme_mode = ft.ThemeMode.LIGHT
    
    control = ft.Row(
        controls=[
            ft.ElevatedButton(
                text='Sucess',
                color=ft.colors.BLUE,
                on_click=lambda e: clicked_sucess(e)
            ),
            ft.ElevatedButton(
                text='Warning',
                color=ft.colors.PURPLE,
                on_click=lambda e: clicked_warning(e)
            ),
            ft.ElevatedButton(
                text='Error',
                color=ft.colors.RED,
                on_click=lambda e: clicked_error(e)
            )
        ]
    )

    def clicked_sucess(e):
        flet_toast.sucess(
            page=page,
            message='Deu sucesso',
            position=flet_toast.Position.TOP_RIGHT,
            duration=5
        )
    
    def clicked_warning(e):
        flet_toast.warning(
            page=page,
            message='Deu warning',
            position=flet_toast.Position.BOTTOM_RIGHT,
            duration=5
        )
    
    def clicked_error(e):
        flet_toast.error(
            page=page,
            message='Deu erro',
            position=flet_toast.Position.BOTTOM_LEFT,
            duration=5
        )

    page.add(control)

if __name__ == '__main__':
    ft.app(target=main)
```

## Documentação

### Métodos
**success**:
Exibe uma notificação toast de sucesso.

- `page`: A página Flet onde o toast será exibido.
- `message`: A mensagem a ser exibida no toast.
- `position`: A posição do toast na tela.
- `duration`: A duração da notificação toast

**error**:
Exibe uma notificação toast de erro.

- `page`: A página Flet onde o toast será exibido.
- `message`: A mensagem a ser exibida no toast.
- `position`: A posição do toast na tela.
- `duration`: A duração da notificação toast

**warning**:
Exibe uma notificação toast de aviso.

- `page`: A página Flet onde o toast será exibido.
- `message`: A mensagem a ser exibida no toast.
- `position`: A posição do toast na tela.
- `duration`: A duração da notificação toast

### Propriedas
**position**:
position define as possíveis posições para exibir as notificações toast na tela. As opções incluem:

- `top_left`: Canto superior esquerdo.
- `top_right`: Canto superior direito.
- `bottom_left`: Canto inferior esquerdo.
- `bottom_right`: Canto inferior direito (padrão).

**duration**:
Define o tempo em que a notificação toast estará visivel na tela. Este deve ser um número inteiro

## Novidades 0.5.0
- Agrupamento de toasts visíveis

## Novidades 0.4.2
- Correção do bug quando o toast é iniciado de forma assíncrona.

## Novidades 0.4.0
- Agora os toats são gerados de forma assíncrona de modo a não bloquear a execução normal do programa.

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENCE para mais detalhes.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório do GitHub.