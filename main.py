#!/usr/bin/env python
from scene import Scene
from engine import Renderer

import argparse
import importlib
import os
from multiprocessing import cpu_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (no .py)")
    parser.add_argument("-p", "--processes", action="store", type=int, dest="processes", default=0, help="Number of threads (all threads is default/0")
    args = parser.parse_args()
    args = parser.parse_args()
    if args.processes == 0:
        process_count = cpu_count()
    else:
        process_count = args.processes

    mod = importlib.import_module(args.scene)
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = Renderer()

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDERED_IMAGE, "w") as img_file_object:
        engine.render_multiprocess(scene, process_count, img_file_object)


if __name__ == '__main__':
    main()
