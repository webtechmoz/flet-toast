import flet as ft
from Toast.Toast import (
    Toast,
    creating_toast,
)
from Types.types import (
    color,
    icons,
    position
)

class Toastfy:

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
            

flet_toast: Toastfy = Toastfy()