from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from light import Light
from material import Material, Chesspattern

WIDTH = 2560
HEIGHT = 1440
RENDERED_IMAGE = "twospheres.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    # Ground Plane
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        Chesspattern(
            color1=Color.from_hex("#420500"),
            color2=Color.from_hex("#e6b87d"),
            ambient=0.9,
            reflection=0.2,
        ),
    ),
    # Blue ball
    Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    # Pink ball
    Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980"))),
]
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
    ]