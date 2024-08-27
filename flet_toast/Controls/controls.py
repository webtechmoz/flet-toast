import flet as ft
import asyncio
from time import sleep
try:
    from Types.types import Position

except:
    from ..Types.types import Position

class Container(ft.Container):
    def __init__(
        self,
        bgcolor: ft.colors,
        color: ft.colors,
        width: float,
        height: float,
        border_radius: float,
        text: str,
        size: float,
        icon: ft.icons,
        icon_size: float
    ):
        if text[1:-1].islower() == True:
            if len(text) <= 32:
                self.text = text
            else:
                self.text = f'{text[:32]}...'
        
        else:
            if len(text) <= 28:
                self.text = text
            else:
                self.text = f'{text[:28]}...'
        
        super().__init__()
        self.bgcolor = bgcolor
        self.border_radius = ft.border_radius.only(
            top_left=border_radius,
            top_right=border_radius,
            bottom_left=0,
            bottom_right=0
        )
        self.width = width
        self.height = height
        self.padding = ft.padding.only(
            left=5,
            right=5
        )
        self.content = ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    size=icon_size,
                    color=color
                ),
                ft.Text(
                    value=self.text,
                    weight='bold',
                    size=size,
                    color=color
                )
            ],
            spacing=5
        )
        self.alignment = ft.alignment.center_left

class Toast(ft.Stack):
    def __init__(
        self,
        page: ft.Page,
        color: ft.colors,
        text: str,
        icon: ft.icons,
        position: Position,
        duration: int,
        icon_size: float = 25,
        size: float = 13,
        border_radius: float = 6,
        bgcolor: ft.colors = ft.colors.with_opacity(0.8, ft.colors.WHITE),
        position_spacing: int = 10
    ):
        try:
            self.position = position.value
        
        except:
            self.position = position
        
        self.Page = page
        self.duration = duration
        
        super().__init__()
        self.width = 280
        self.height = 45
        self.controls = [
            Container(
                bgcolor=bgcolor,
                color=color,
                width=self.width,
                height=self.height,
                border_radius=border_radius,
                text=text,
                size=size,
                icon=icon,
                icon_size=icon_size
            ),
            ft.Container(
                width=self.width,
                height=3,
                border_radius=border_radius,
                bgcolor=color,
                top=self.height - 3
            ),
            ft.Container(
                content=ft.Icon(
                    name=ft.icons.CLOSE,
                    color=color,
                    size=14,
                ),
                width=18,
                height=18,
                border_radius=18,
                alignment=ft.alignment.center,
                border=ft.border.all(
                    width=2,
                    color=ft.colors.with_opacity(0.4, color)
                ),
                top=3,
                right=3,
                on_click=lambda e: self.clicked(e)
            )
        ]

        if self.position == 'top_left':
            self.top = position_spacing
            self.left = position_spacing
        
        elif self.position == 'top_right':
            self.top = position_spacing
            self.right = position_spacing
        
        elif self.position == 'bottom_left':
            self.bottom = position_spacing
            self.left = position_spacing
        
        elif self.position == 'bottom_right':
            self.bottom = position_spacing
            self.right = position_spacing
        
        asyncio.run(self.open_toast())
        
    def clicked(self, e: ft.ControlEvent):
        self.close_toast()
    
    async def open_toast(self):
        self.Page.overlay.append(self)

        width = self.width
        redution = (1/self.width)*self.duration

        while width > 0:
            width -= 1
            self.controls[1].width = width
            self.Page.update()
            sleep(redution)
        
        self.close_toast()
    
    def close_toast(self):
        try:
            self.Page.overlay.remove(self)
            self.Page.update()

        except:
            pass