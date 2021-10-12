from math import sqrt


class Sphere:
    """Sphere har center, radius, and material"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersect(self, ray):
        """Checks if the ray intersects with the sphere,
        returns distance from camera to intersection point
        or None if the ray never hit the sphere"""
        sphere_to_ray = ray.origin - self.center
        #a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c    # * a

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None
