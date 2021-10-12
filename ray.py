class Ray:
    """Ray is a vector plus a normalized direction"""
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
