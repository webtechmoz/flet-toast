from ..Controls.controls import Toast
from ..Controls.controls import ft
from ..Types.types import Position


class FletToast:
    """
    Crie toasts personalizados usando a biblioteca flet do python.
    """

    @property
    def Position(self) -> Position:
        return Position

    def sucess(
        self,
        page: ft.Page,
        message: str,
        position: Position,
        duration: int = 3
    ) -> Toast:
        
        toast = Toast(
            page=page,
            color=ft.colors.BLUE,
            text=message,
            icon=ft.icons.CHECK_CIRCLE_OUTLINED,
            position=position,
            duration=duration
        )

        return toast
    
    def warning(
        self,
        page: ft.Page,
        message: str,
        position: Position,
        duration: int = 3
    ) -> Toast:
        
        toast = Toast(
            page=page,
            color=ft.colors.PURPLE,
            text=message,
            icon=ft.icons.WARNING_ROUNDED,
            position=position,
            duration=duration
        )

        return toast
    
    def error(
        self,
        page: ft.Page,
        message: str,
        position: Position,
        duration: int = 3
    ) -> Toast:
        
        toast = Toast(
            page=page,
            color=ft.colors.RED,
            text=message,
            icon=ft.icons.ERROR,
            position=position,
            duration=duration
        )

        return toast

flet_toast = FletToast()