class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, img_file_object):
        Image.write_ppm_header(img_file_object, height=self.height, width=self.width)
        self.write_ppm_raw(img_file_object)

    @staticmethod
    def write_ppm_header(image_file_object, height=None, width=None):
        image_file_object.write("P3 {} {}\n255\n".format(width, height))

    def write_ppm_raw(self, img_file):
        def to_byte(num):
            return round(max(min(num * 255, 255), 0))

        img_file
        for row in self.pixels:
            for color in row:
                img_file.write(
                    "{} {} {} ".format(
                        to_byte(color.x), to_byte(color.y), to_byte(color.z)
                    )
                )
            img_file.write("\n")
