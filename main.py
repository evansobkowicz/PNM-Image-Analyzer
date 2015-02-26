# Project 1
# Evan Sobkowicz


class Edger:

    # Initialize Object
    def __init__(self, file_path):
        self.file_path = file_path
        self.create_image()

    # Read in pnm P2 or P3 files from text
    def create_image(self):
        path = "img/" + self.file_path
        f = open(path, "r")
        img_type = f.readline()
        img_size = f.readline()
        sizes = img_size.split()
        width = int(sizes[0])
        height = int(sizes[1])
        data = list()
        lines = f.readlines()
        for line in lines:
            clean_line = line.strip('\n').strip(' ')
            data.append(clean_line)
        f.close()
        print 'Type:', img_type
        print 'Size:', sizes
        print 'Length', len(data), ' = ', int(sizes[0])*int(sizes[1])
        print data
        return None

    # Grayscale
    def grayscale(self, pic):
        return None


    # Analyze Edges (distance of color value calculations)
    def analyze_edges(self, pic):
        return None


    # Display edged image
    def display_image(self, pic):
        return None


    # Save your edge image to a file using the greyscale .pnm format.
    def save_image(self, pic):
        return None



e = Edger('rainbow.pnm')
