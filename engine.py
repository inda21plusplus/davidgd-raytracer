from image import Image
from ray import Ray
from point import Point
from color import Color


class Renderer:
    """Renders our 3d world into 2d images and"""

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = 1.0
        xpixelstep = (x1 - x0) / (width - 1)

        y0 = -1.0 / aspect_ratio
        y1 = 1.0 / aspect_ratio
        ypixelstep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for i in range(height):
            y = y0 + i * ypixelstep
            for j in range(width):
                x = x0 + j * xpixelstep
                ray = Ray(camera, Point(x, y) - camera)
                pixels.set_pixel(j, i, self.ray_trace(ray, scene))
        return pixels

    def ray_trace(self, ray, scene):
        color = Color(0.0, 0.0, 0.0)
        # Get first object hit by the ray
        distance_hit, object_hit = self.find_nearest_object(ray, scene)
        if object_hit is None:
            return color
        hit_position = ray.origin + ray.direction * distance_hit
        color += self.color_at(object_hit, hit_position, scene)
        return color

    def find_nearest_object(self, ray, scene):
        min_distance = None
        object_hit = None
        for object in scene.objects:
            distance = object.intersect(ray)
            if distance is not None and (object_hit is None or distance < min_distance):
                min_distance = distance
                object_hit = object

        return min_distance, object_hit

    def color_at(self, object_hit, hit_position, scene):
        return object_hit.material
