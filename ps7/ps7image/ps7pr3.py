#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

# function 1

def grayscale(pixels):
    """returns a greyscale version of an image in 2d list format"""
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for item in range(len(pixels[0])):
            brightness_val = brightness(pixels[row][item])
            new_row += [[brightness_val, brightness_val, brightness_val]]
        new_pixels += [new_row]
    return new_pixels

def left_right(pixels):
    """returns a horizontally inverted version of an image in a 2-d list format"""
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for item in range(len(pixels[0])-1, -1, -1):
            new_row += [pixels[row][item]]
        new_pixels += [new_row]
    return new_pixels

def reflect(pixels):
    """returns a vertically-centered reflected version of an image in a 2-d list format"""
    middle = len(pixels)//2
    new_pixels = []
    if len(pixels) % 2 == 0:
        range_list = list(range(0, middle)) + list(range(middle - 1, -1, -1))
    else:
        range_list = list(range(0, middle + 1)) + list(range(middle - 1, -1, -1))
    for row in range_list:
        new_row = []
        for item in range(len(pixels[0])):
            new_row += [pixels[row][item]]
        new_pixels += [new_row]
    return new_pixels

def cut(pixels, rmin, rmax, cmin, cmax):
    """returns a cutout version of an image within rmin/max, and cmin/max as a 2-d list"""
    new_pixels = []
    for row in range(rmin, rmax):
        new_row = []
        for col in range(cmin, cmax):
            new_row += [pixels[row][col]]
        new_pixels += [new_row]
    return new_pixels
