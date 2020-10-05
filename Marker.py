import os
import tensorflow
import numpy
import matplotlib.image as img
import PIL
from PIL import Image,ImageDraw2
from tensorflow import keras

input_training_directory = "C:\\Users\\Ayush Sharma\\Desktop\\Programs\\HTML-Extractor\\Data"
resized_image_training_directory = input_training_directory + "\\" + "Resized"
try:
    os.mkdir(resized_image_training_directory)
except:
    pass

for directory in os.listdir(input_training_directory):
    try:
        n = Image.open(input_training_directory+ "\\" + directory)
        n = n.resize((1500,1500))
        n.save(resized_image_training_directory + "\\" + directory)
    except PermissionError:
        continue

images = []
for directory in os.listdir(resized_image_training_directory):
    n = img.imread(resized_image_training_directory + "\\" + directory)
    images.append(n)

training_image_array = numpy.array(images )
print(training_image_array.shape)





