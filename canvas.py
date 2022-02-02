import numpy as np
from PIL import Image


class Canvas():

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeroes, than replace zeroes with yellow pxls
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)

        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):

        # Converts the current array into an img file
        img = Image.fromarray(self.data,"RGB")
        img.save(imagepath)