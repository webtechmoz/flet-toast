import flet as ft
from flet_toast import flet_toast

def main(page: ft.Page):
    page.title = page.route

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(
                ft.View(
                    route='/',
                    bgcolor=ft.colors.WHITE,
                    controls=[
                        ft.SafeArea(
                            content=ft.Stack(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ANIMATION,
                                        icon_size=25,
                                        icon_color=ft.colors.BLUE,
                                        top=40,
                                        on_click=lambda e: flet_toast.error(page, 'Testado bem mesmo', 'bottom_left')
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
    ft.app(target=main, view=ft.WEB_BROWSER)