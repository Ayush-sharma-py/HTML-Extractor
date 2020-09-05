import os
import numpy as np
import PIL
import PIL.Image

#Directory to where training images are kept
training_directory = "C:\\Users\\Ayush Sharma\\Desktop\\Programs\\HTML-Extractor\\Data"

training_files = os.listdir(training_directory)

#List of training images converted into numpy arrays
training_images = []

#Iterating through to add images in array format to the training_images list
for image_directory in training_files:
    training_images.append(np.array(PIL.Image.open(training_directory + "\\" + image_directory)))

