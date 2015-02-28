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
        self.height = 0
        self.width = 0
        self.largest_vale = 0
        self.img_data = list()
        self.img = None

        # Run the Program
        self.read_file()
        self.create_image()
        self.display_image()

    # HELPER METHODS
    # Image Size Parser
    def img_size(self, data):
        sizes = data.split()
        return int(sizes[0]), int(sizes[1])

    # String Cleaner - Strip new line and white space
    def cleaner(self, s):
        return s.strip('\n').strip(' ')

    # Read in pnm P2 or P3 files from text
    def read_file(self):
        print 'Loading File...'
        path = "img/" + self.file_path
        f = open(path, "r")
        # TODO: Handle Comments In Header
        img_type = self.cleaner(f.readline())                   # Line 1: Image Type
        self.width, self.height = self.img_size(f.readline())   # Line 2/3: Image Width/Height
        self.largest_vale = self.cleaner(f.readline())          # Line 4: Largest Color Value
        raw_data = f.read().strip(' ').splitlines()
        data = [[0 for x in range(self.height)] for x in range(self.width)]
        if img_type == 'P2':
            # Grayscale Image
            for i in range(self.width * self.height):
                clean_line = self.cleaner(f.readline())
                # data.append(clean_line)
        elif img_type == 'P3':
            # RGB Image
            for i in range(self.width):
                for j in range(self.height):
                    color = [raw_data.pop(0), raw_data.pop(0), raw_data.pop(0)]
                    data[i][j] = color
        else:
            print 'ERROR: Invalid File Type.'
        f.close()
        self.img_data = data
        print self.img_data
        print 'Finished Loading File...'


    # Create Image
    def create_image(self):
        self.img = Image(Point(self.width/2, self.height/2), self.width, self.height)
        for x in range(self.width * self.height):
            # for y in range(self.height):
            color = int(self.img_data[x])
            self.img.setPixel(x, x, color_rgb(color, color, color))

    # Grayscale
    def grayscale(self, pic):
        # GS value = .3*red value + .59*green value + .11 * blue value
        return None


    # Analyze Edges (distance of color value calculations)
    # Use floats, add .5 to numbers to avoid improper rounding
    def analyze_edges(self, pic):
        return None


    # Display edged image
    def display_image(self):
        win = GraphWin('Image', self.width, self.height)
        self.img.draw(win)
        win.getMouse()
        win.close()


    # Save your edge image to a file using the greyscale .pnm format.
    def save_image(self, pic):
        return None



e = Edger('rainbow.pnm')
