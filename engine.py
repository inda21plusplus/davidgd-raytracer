from image import Image
from ray import Ray
from point import Point
from color import Color

import time


class Renderer:
    """Renders our 3d world into 2d images and"""

    MAX_DEPTH = 5
    MIN_DISPLACEMENT = 0.0001

    def render(self, scene):
        start_time = time.time()
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
            print("  8{:22} {:3} %".format(round(float(i) / float(height) * 20) * "=" + ">",
                                      round(float(i) / float(height) * 100)), end="\r")
        print("\n  Render time: {} s\n  Done".format(round(time.time() - start_time, 3)))
        return pixels

    def ray_trace(self, ray, scene, depth=0):
        color = Color(0.0, 0.0, 0.0)
        # Get first object hit by the ray
        distance_hit, object_hit = self.find_nearest_object(ray, scene)
        if object_hit is None:
            return color
        hit_position = ray.origin + ray.direction * distance_hit
        hit_normal = object_hit.normal(hit_position)
        color += self.color_at(object_hit, hit_position, hit_normal, scene)
        if depth < self.MAX_DEPTH:
            new_ray_position = hit_position + hit_normal * self.MIN_DISPLACEMENT
            new_ray_dir = ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            new_ray = Ray(new_ray_position, new_ray_dir)
            # Make new ray have less energy
            color += self.ray_trace(new_ray, scene, depth + 1) * object_hit.material.reflection
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

    def color_at(self, object_hit, hit_position, normal, scene):
        material = object_hit.material
        object_color = material.color_at(hit_position)
        to_camera = scene.camera - hit_position
        specular_k = 50.0
        color = material.ambient * Color.from_hex("#000000")
        for light in scene.lights:
            to_light = Ray(hit_position, light.position - hit_position)
            # Diffuse shading (Lambert)
            color += object_color * material.diffuse * max(normal.dot_product(to_light.direction), 0)

            # Specular shading (Blinn)
            half_vector = (to_light.direction + to_camera).normalize()
            color += light.color * material.specular * max(normal.dot_product(half_vector), 0) ** specular_k
        return color
