import os
#import tensorflow
#from tensorflow import keras
import numpy
import matplotlib.image as img
import PIL
from PIL import Image,ImageDraw2,ImageOps
from image_slicer import slice


input_training_directory = "C:\\Users\\Ayush Sharma\\Desktop\\Programs\\HTML-Extractor\\Data"
resized_image_training_directory = input_training_directory + "\\" + "Resized"

try:
    os.mkdir(resized_image_training_directory)
except:
    pass

for directory in os.listdir(input_training_directory):
    try:
        n = Image.open(input_training_directory+ "\\" + directory)
        n = ImageOps.grayscale(n)
        n = n.resize((1500,1500))
        n.save(resized_image_training_directory + "\\" + directory)
    except PermissionError:
        continue

images = []
for directory in os.listdir(resized_image_training_directory):
    n = img.imread(resized_image_training_directory + "\\" + directory)
    images.append(n)

training_image_array = numpy.array(images)
print(training_image_array.shape)

def calculate_seperation_coefficient(directory):
    seperation_coefficient = 1
    image = PIL.Image.open(directory)
    width,height = image.size
    seperation_coefficient = round(width/25)
    return seperation_coefficient

slice(input_training_directory + "\\" + "Html1.png",calculate_seperation_coefficient(input_training_directory + "\\" + "Html1.png"))

slice(resized_image_training_directory + "\\Html1.png" , 4)


#output - array[list[tuples(x,y)]]