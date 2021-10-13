#!/usr/bin/env python
from scene import Scene
from engine import Renderer

import argparse
import importlib
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (no .py)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = Renderer()
    image = engine.render(scene)
    
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDERED_IMAGE, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()
