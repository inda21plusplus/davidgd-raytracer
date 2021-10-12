class Scene:
    """Scene stores everything in our 3d world for the ray tracing engine"""
    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height
