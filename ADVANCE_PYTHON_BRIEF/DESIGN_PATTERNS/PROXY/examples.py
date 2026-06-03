class RealImage:

    def display(self):
        print("Loading Image")


class ProxyImage:

    def __init__(self):
        self.real_image = None

    def display(self):

        if self.real_image is None:
            self.real_image = RealImage()

        self.real_image.display()


image = ProxyImage()

image.display()
