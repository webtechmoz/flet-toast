import flet as ft
from .Toast import (
    Toast,
    creating_toast,
)
from .types import (
    color,
    icons,
    position
)

class Toastfy:

    """
        ```python
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

    position = position

    def sucess(
        self,
        page: ft.Page,
        message: str,
        position: position = position.BOTTOM_RIGHT
    ) -> Toast:
        
        toast = creating_toast().toastfy(
            page=page,
            message=message,
            icon=icons.SUCESS.value,
            color=color.SUCESS.value,
            position=self.__position_string__(position)
        )

        return toast
    
    def error(
        self,
        page: ft.Page,
        message: str,
        position: position = position.BOTTOM_RIGHT
    ) -> Toast:
        
        toast = creating_toast().toastfy(
            page=page,
            message=message,
            icon=icons.ERROR.value,
            color=color.ERROR.value,
            position=self.__position_string__(position)
        )

        return toast
    
    def warning(
        self,
        page: ft.Page,
        message: str,
        position: position = position.BOTTOM_RIGHT
    ) -> Toast:
        
        toast = creating_toast().toastfy(
            page=page,
            message=message,
            icon=icons.WARNING.value,
            color=color.WARNING.value,
            position=self.__position_string__(position)
        )

        return toast
    
    def position_list(self) -> list[position]:
        return [k.value for k in position]

    def __position_string__(self, pos: position) -> str:
        if type(pos) == position:
            return pos.value
        
        else:
            if pos in self.position_list():
                return pos
            
            else:
                return self.position_list()[-1]