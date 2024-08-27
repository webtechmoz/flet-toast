try:
    from Toast.Toast import flet_toast

except:
    from .Toast.Toast import flet_toast

"""
Crie toasts personalizados usando a biblioteca flet do python.
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

Consulte a documentação pelo site: https://pypi.org/project/flet-toast/
"""