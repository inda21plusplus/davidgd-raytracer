from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from light import Light
from material import Material, Chesspattern

WIDTH = 2560
HEIGHT = 1440

RENDERED_IMAGE = "manyspheres.ppm"
CAMERA = Vector(0, -0.3, -1.5)
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
]

colors = ["#9932cc",
          "#4285f4",
          "#ea4335",
          "#83c165",
          "#4697e1",
          "#81c97f",
          "#1c72e9",
          "#4cb942",
          "#5274fa",
          "#d5232f",
          "#84c188",
          "#0d0e10",
          "#f44336",
          "#84c088",
          "#d37b7a",
          "#8bc34a",
          "#89ac76",
          "#8097bf",
          "#f2a56f",
          "#7f89ce",
          "#80b090",
          "#ce4741",
          "#fd3333",
          "#f08080",
          "#b0e0e6",
          "#97857d",
          "#4ca3dd",
          "#c0d6e4",
          "#b0e0e6",
          "#6897bb",
          "#00ced1",
          "#f5f5dc",
          "#b4eeb4",
          "#caff70",
          "#05eaff",
          "#838b8b",
          "#ffb6c1",
          "#ffd859",
          "#00b3ff",
          "#ff2301",
          "#05eaff",
          "#96abff"]
for i in range(30):
    OBJECTS.append(Sphere(Point(0.002 * i - 2, -0.1, 2.5 * i + 3), 0.6,
                          Material(Color.from_hex(colors[i]))))
    OBJECTS.append(Sphere(Point(0.002 * -i + 2, -0.1, 2.5 * i + 3), 0.6,
                          Material(Color.from_hex(colors[30 - i]))))

LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
]
