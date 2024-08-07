from .toastfy import toast_flet

"""
```
import flet as ft
from Toast.toastfy import toast_flet

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
                            content= ft.Stack(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ANIMATION,
                                        icon_size=25,
                                        icon_color=ft.colors.BLUE,
                                        top=40,
                                        on_click= lambda e: toast_flet.sucess(page, 'Testado bem mesmo e aprovado ldjhibdu dkd', 'top_left')
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
"""