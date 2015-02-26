# Project 1
# Evan Sobkowicz


class Edger:

    # Initialize Object
    def __init__(self, file_path):
        self.file_path = file_path
        self.img_data = list()

        # Run the Program
        self.create_image()


    # HELPER METHODS

    # Image Size Parser
    def img_size(self, data):
        sizes = data.split()
        return int(sizes[0]), int(sizes[1])

    # String Cleaner - Strip new line and white space
    def cleaner(self, s):
        return s.strip('\n').strip(' ')

    # Read in pnm P2 or P3 files from text
    def create_image(self):
        path = "img/" + self.file_path
        f = open(path, "r")
        img_type = self.cleaner(f.readline())
        if img_type == 'P2' or img_type == 'P3':
            width, height = self.img_size(f.readline())
            data = list()
            for i in range(width * height):
                clean_line = self.cleaner(f.readline())
                data.append(clean_line)
        else:
            print 'ERROR: Invalid File Type.'
        f.close()
        self.img_data = data

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
