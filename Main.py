import os
import numpy as np
import PIL
import PIL.Image
import pytesseract
from tensorflow import keras

#Directory to where training images are kept
training_directory = "C:\\Users\\Ayush Sharma\\Desktop\\Programs\\HTML-Extractor\\Data"
#Configuring Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


training_files = os.listdir(training_directory)

#List of training images converted into numpy arrays
training_images = []

#Iterating through to add images in array format to the training_images list
for image_directory in training_files:
    #data pipeline for pytesseract in PIL class
    image = PIL.Image.open(training_directory + "\\" + image_directory)
    #resizing to make it streamlined 
    image = image.resize((28,28))
    training_images.append(image)

#numpy array of images
array_training_images = np.array(training_images)

#Function for extracting text from image 
def extract_text(PIL_open):
    return pytesseract.image_to_string(PIL_open)

def shape_text_data(text:str):
    text = text.split("\n\n")
    text = np.array(text)
    print(text)

shape_text_data(extract_text(training_images[0]))



#starting tensorflow model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28, 3)),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    keras.layers.Dense(512,activation='relu'),
    #keras.layers.Dense(len(shapes)) #shape of output is not defined yet
])