from enum import Enum

class position(Enum):
    TOP_LEFT = 'top_left'
    TOP_RIGHT = 'top_right'
    BOTTOM_LEFT = 'bottom_left'
    BOTTOM_RIGHT = 'bottom_right'

class icons(Enum):
    SUCESS = 'check_circle'
    ERROR = 'error'
    WARNING = 'warning'

class color(Enum):
    SUCESS = 'green'
    ERROR = 'error'
    WARNING = 'purple'

class configs(Enum):
    width = 250
    height = 40
    border_radius = 3
    padding  = 3
    alignment = 'center_left'
    icon_size = 22
    size = 13
    weight = 'bold'
    spacing = 3

class bgcolor(Enum):
    DARK = 'white'
    LIGHT = 'black'