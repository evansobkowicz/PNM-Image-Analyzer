# Project 1
# Evan Sobkowicz
# Date: 3/1/15


# Import Libraries for graphics, math, and timestamps
from graphics import *
import math
import time
import datetime


# Edger Class
# Processes a P2 or P3 PNM file, detects edges, displays the image, and saves the file
class Edger:

    # Initialize Object
    # Input: [file] original image file path
    # Return: []
    def __init__(self, file):
        # Initialize Class Variables
        self.file_path = file
        self.img_type = None
        self.height = 0
        self.width = 0
        self.largest_value = 0
        self.img_data = list()
        self.img = None
        self.edged_img = None
        # Run the Programs Steps
        self.read_file()
        self.create_image()
        self.grayscale()
        self.analyze_edges()
        self.save_image()
        self.display_image(self.img)
        self.display_image(self.edged_img)

    # Get Current Timestamp (for file name)
    # Input: []
    # Return: [STRING] current timestamp
    def timestamp(self):
        ts = time.time()
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    # Image Size Parser
    # Input: [INT, INT] the raw width and height read from the image
    # Return: [INT, INT] the clean integers for the image width and height
    def img_size(self, width, height):
        return int(self.cleaner(width)), int(self.cleaner(height))

    # String Cleaner (strip new line and white space)
    # Input: [STRING] raw string
    # Return: [STRING] cleaned string (stripped of new lines and white space)
    def cleaner(self, s):
        return s.strip('\n').strip(' ')

    # Read in pnm P2 or P3 files from text, store all image data in class vars
    # Input: []
    # Return: []
    def read_file(self):
        print '> Loading File...'
        path = "img/" + self.file_path
        f = open(path, "r")
        # Read in image meta information
        self.img_type = self.cleaner(f.readline())                            # Line 1: Image Type
        self.width, self.height = self.img_size(f.readline(), f.readline())   # Line 2/3: Image Width/Height
        self.largest_value = self.cleaner(f.readline())                       # Line 4: Largest Color Value
        raw_data = f.read().split(' ')
        # Create image data matrix to store values
        data = [[0 for x in range(self.height)] for x in range(self.width)]
        if self.img_type.find('P2') != -1:
            # Grayscale Image
            print '>> Processing Grayscale (P2) Image...'
            for y in range(self.height):
                for x in range(self.width):
                    data[x][y] = int(raw_data.pop(0))
        elif self.img_type.find('P3') != -1:
            # RGB Image
            print '>> Processing RGB (P3) Image...'
            for y in range(self.height):
                for x in range(self.width):
                    color = [int(raw_data.pop(0)), int(raw_data.pop(0)), int(raw_data.pop(0))]
                    data[x][y] = color
        else:
            print 'ERROR: Invalid File Type!'
        f.close()
        # Save the data
        self.img_data = data
        print '>> Finished Loading File...'


    # Create Image from data read into self.img_data
    # Input: []
    # Return: []
    def create_image(self):
        print '> Creating Image...'
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

    # Apply Grayscale Filter to the Image (if type is P3)
    # Input: []
    # Return: []
    def grayscale(self):
        if self.img_type.find('P3') != -1:
            print '> Grayscaling P3 Image...'
            for x in range(self.width):
                for y in range(self.height):
                    color = self.img.getPixel(x, y)
                    gs = (0.3 * color[0]) + (0.59 * color[1]) + (0.11 * color[2])
                    self.img.setPixel(x, y, color_rgb(gs, gs, gs))
        else:
            print '> Image Already in P2 Grayscale Format...'

    # Analyze image edges by calculating distance of neighboring pixels
    # Input: []
    # Return: []
    def analyze_edges(self):
        print '> Analyzing Image Edges...'
        self.edged_img = Image(Point(self.width/2, self.height/2), self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    # Skip Edges
                    self.edged_img.setPixel(x, y, color_rgb(0, 0, 0))
                else:
                    left = self.img.getPixel(x - 1, y)
                    right = self.img.getPixel(x + 1, y)
                    top = self.img.getPixel(x, y + 1)
                    bottom = self.img.getPixel(x, y - 1)
                    edge = math.sqrt(math.pow(left[0] - right[0], 2) + math.pow(top[0] - bottom[0], 2))
                    self.edged_img.setPixel(x, y, color_rgb(edge, edge, edge))

    # Display an image to the user
    # Input: [IMAGE] the image to be displayed
    # Return: []
    def display_image(self, pic):
        win = GraphWin('Image', self.width, self.height)
        pic.draw(win)
        print '> Image Displayed...'
        print '==> Click on the image to close it'
        win.getMouse()
        win.close()

    # Save edged image to a file using the greyscale (P2) .pnm format (in the /output directory)
    # Input: []
    # Return: []
    def save_image(self):
        output = 'P2\n'
        output += str(self.width) + '\n'
        output += str(self.height) + '\n'
        output += '255\n'
        for y in range(self.height):
            for x in range(self.width):
                color = self.edged_img.getPixel(x, y)
                output += str(color[0]) + ' '
        path = 'output/' + str(self.timestamp()) + '.pnm'
        f = open(path, 'w')
        f.write(output)
        f.close()


# PROJECT 1 MAIN
def main():
    # Test Images should be located in the /img directory
    # e1 = Edger('rainbow.pnm')         # Test Image 1
    # e2 = Edger('buildingGS.pnm')      # Test Image 2
    e3 = Edger('veggies.pnm')           # Test Image 3



# Run the program!
main()
