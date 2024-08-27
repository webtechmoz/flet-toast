import flet as ft
from time import sleep

from ..Types.types import position, configs

class Toast(ft.Stack):
    def __init__(
        self,
        page: ft.Page,
        bgcolor: ft.colors,
        width: int,
        height: int,
        border_radius: ft.border_radius,
        padding: int,
        alignment: ft.alignment,
        color: ft.colors,
        icon: ft.icons,
        icon_size: int,
        message: str,
        size: int,
        weight: ft.FontWeight,
        spacing: int,
        position: position
    ) -> None:
        self.position = position
        top, left = self.position_handler(page, width, height)

        super().__init__(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.with_opacity(0.12, bgcolor),
                    width=width,
                    height=height,
                    border_radius=border_radius,
                    padding=padding,
                    alignment=alignment,
                    top=top,
                    left=left,
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                color=color,
                                size=icon_size,
                                name=icon
                            ),
                            ft.Text(
                                value=message if (len(message) < 28) else f'{message[:28]}...',
                                size=size,
                                weight=weight,
                                color=color
                            )
                        ],
                        spacing=spacing
                    )
                ),
                ft.Container(
                    bgcolor=color,
                    width=width,
                    height=2,
                    top=top + height - 2,
                    border_radius=border_radius,
                    left=left,
                )
            ],
            width=page.width,
            height=page.height,
            offset=ft.Offset(x=-1.50 if 'left' in self.position else 1.50, y=0),
            animate_offset=ft.Animation(duration=600, curve=ft.AnimationCurve.DECELERATE)
        )

    def position_handler(self, page: ft.Page, width: int, height: int) -> tuple[float, float]:
        multiplayer = 2.2 if page.platform.value in ['ios', 'android'] else 1.50

        if self.position == position.TOP_LEFT.value:
            return 0, 0
        
        elif self.position == position.BOTTOM_LEFT.value:
            return page.height - height * multiplayer, 0
        
        elif self.position == position.TOP_RIGHT.value:
            return 0, page.width - width * 1.1
        
        return page.height - height * multiplayer, page.width - width * 1.1


class creating_toast:
    
    def toastfy(self, page: ft.Page, message: str, icon: ft.icons, color: ft.colors, position: position) -> Toast:
        
        toast = Toast(
            page= page,
            bgcolor=ft.colors.WHITE if page.views[-1].bgcolor == 'black' else ft.colors.BLACK,
            width= configs.width.value,
            height= configs.height.value,
            border_radius= configs.border_radius.value,
            padding= configs.padding.value,
            alignment=ft.alignment.center_left,
            color= color,
            icon= icon,
            icon_size= configs.icon_size.value,
            message= message,
            size=configs.size.value,
            weight= configs.weight.value,
            spacing= configs.spacing.value,
            position= position
        )

        open_toast().open(page, toast)
        close_toast().close(page, position, toast)

        return toast


class open_toast:

    def open(self, page: ft.Page, toast: Toast):

        for i, control in enumerate(page.views[-1].controls):
            if control._get_control_name().lower() == 'stack':
                control.controls.append(toast)
                page.update()
                break

            if i == len(page.views[-1].controls) - 1:
                for parent in page.views[-1].controls:
                    for children in parent._get_children():
                        if children._get_control_name().lower() == 'stack':
                            children.controls.append(toast)
                            page.update()
                            break


class close_toast:

    def close(self, page: ft.Page, position: position, toast: Toast):
        toast.offset = ft.Offset(x=0, y=0)
        page.update()

        while toast.controls[-1].width > 0:
            toast.controls[-1].width -=1
            sleep(0.01)
            page.update()
        
        toast.offset=ft.Offset(x=-1.50 if 'left' in position else 1.50, y=0)
        page.update()

        for i, control in enumerate(page.views[-1].controls):
            if control._get_control_name().lower() == 'stack':
                control.controls.remove(toast)
                break

            if i == len(page.views[-1].controls) - 1:
                for i, parent in enumerate(page.views[-1].controls):
                    for children in parent._get_children():
                        if children._get_control_name().lower() == 'stack':
                            children.controls.remove(toast)
                            break

        page.update()