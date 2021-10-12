#!/usr/bin/env python
from image import Image
from color import Color


def main():
    WIDTH = 3
    HEIGHT = 2
    img = Image(WIDTH, HEIGHT)
    red = Color(x=1, y=0, z=0)
    green = Color(x=0, y=1, z=0)
    blue = Color(x=0, y=0, z=1)
    
    img.set_pixel(0, 0, red)
    img.set_pixel(1, 0, green)
    img.set_pixel(2, 0, blue)

    img.set_pixel(0, 1, red + green)
    img.set_pixel(1, 1, red + green + blue)
    img.set_pixel(2, 1, red * 0.001)

    with open("test.ppm", "w") as img_file:
        img.write_ppm(img_file)


if __name__ == '__main__':
    main()
