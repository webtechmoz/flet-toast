from ..Controls.controls import Toast
from ..Controls.controls import ft
from ..Types.types import Position

class FletToast:
    
    """
    Crie toasts personalizados usando a biblioteca flet do python.
    
    ---
    Consulte a documentação pelo site: https://pypi.org/project/flet-toast/
    """

    def sucess(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3
    ) -> Toast:
        
        toast = Toast(
            page=page,
            color=ft.Colors.BLUE,
            text=message,
            icon=ft.Icons.CHECK_CIRCLE_OUTLINED,
            position=position,
            duration=duration
        )

        return toast
    
    def warning(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3
    ) -> Toast:
        
        toast = Toast(
            page=page,
            color=ft.Colors.PURPLE,
            text=message,
            icon=ft.Icons.WARNING_ROUNDED,
            position=position,
            duration=duration
        )

        return toast
    
    def error(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3
    ) -> Toast:
        
        toast = Toast(
            page=page,
            color=ft.Colors.RED,
            text=message,
            icon=ft.Icons.ERROR,
            position=position,
            duration=duration
        )

        return toast

flet_toast = FletToast()