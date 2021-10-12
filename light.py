from color import Color


class Light:
    """Light represents a point lightsource with a color in our 3d world"""
    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
