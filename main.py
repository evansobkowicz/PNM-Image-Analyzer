# Project 1
# Evan Sobkowicz
# Date: 2/27/15

from graphics import *

# Purpose
# Input/Params
# Output/Return


class Edger:

    # Initialize Object
    def __init__(self, file):
        self.file_path = file
        self.img_type = None
        self.height = 0
        self.width = 0
        self.largest_value = 0
        self.img_data = list()
        self.img = None

        # Run the Program
        self.read_file()
        self.create_image()
        self.grayscale()
        self.display_image()

    # Image Size Parser
    def img_size(self, width, height):
        return int(self.cleaner(width)), int(self.cleaner(height))

    # String Cleaner - Strip new line and white space
    def cleaner(self, s):
        return s.strip('\n').strip(' ')

    # Read in pnm P2 or P3 files from text
    def read_file(self):
        print 'Loading File...'
        path = "img/" + self.file_path
        f = open(path, "r")
        # TODO: Handle Comments In Header
        self.img_type = self.cleaner(f.readline())                            # Line 1: Image Type
        self.width, self.height = self.img_size(f.readline(), f.readline())   # Line 2/3: Image Width/Height
        self.largest_value = self.cleaner(f.readline())                       # Line 4: Largest Color Value
        raw_data = f.read().split(' ')
        data = [[0 for x in range(self.height)] for x in range(self.width)]
        if self.img_type.find('P2') != -1:
            # Grayscale Image
            print 'Processing Grayscale (P2) Image...'
            for y in range(self.height):
                for x in range(self.width):
                    data[x][y] = int(raw_data.pop(0))
        elif self.img_type.find('P3') != -1:
            # RGB Image
            print 'Processing RGB (P3) Image...'
            for y in range(self.height):
                for x in range(self.width):
                    color = [int(raw_data.pop(0)), int(raw_data.pop(0)), int(raw_data.pop(0))]
                    data[x][y] = color
        else:
            print 'ERROR: Invalid File Type.'
        print "Potential Error...", len(raw_data)
        f.close()
        self.img_data = data
        print 'Finished Loading File...'


    # Create Image
    def create_image(self):
        print 'Creating Image...'
        self.img = Image(Point(self.width/2, self.height/2), self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                if self.img_type.find('P2') != -1:
                    raw_color = self.img_data[x][y]
                    color = color_rgb(raw_color, raw_color, raw_color)
                elif self.img_type.find('P3') != -1:
                    rgb = self.img_data[x][y]
                    color = color_rgb(rgb[0], rgb[1], rgb[2])
                self.img.setPixel(x, y, color)

    # Grayscale
    def grayscale(self):
        if self.img_type.find('P3') != -1:
            print 'Grayscaling P3 Image...'
            for x in range(self.width):
                for y in range(self.height):
                    color = self.img.getPixel(x, y)
                    gs = (0.3 * color[0]) + (0.59 * color[1]) + (0.11 * color[2])
                    self.img.setPixel(x, y, color_rgb(gs, gs, gs))


    # Analyze Edges (distance of color value calculations)
    # Use floats, add .5 to numbers to avoid improper rounding
    def analyze_edges(self, pic):
        return None


    # Display edged image
    def display_image(self):
        win = GraphWin('Image', self.width, self.height)
        self.img.draw(win)
        print 'Image Displayed...'
        print '==> Click on the image to close it'
        win.getMouse()
        win.close()


    # Save your edge image to a file using the greyscale .pnm format.
    def save_image(self, pic):
        return None



e = Edger('rainbow.pnm')
