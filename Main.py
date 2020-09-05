import os
import numpy as np
import PIL
import PIL.Image
import pytesseract

#Directory to where training images are kept
training_directory = "C:\\Users\\Ayush Sharma\\Desktop\\Programs\\HTML-Extractor\\Data"
#Configuring Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

training_files = os.listdir(training_directory)

#List of training images converted into numpy arrays
training_images = []

#Iterating through to add images in array format to the training_images list
for image_directory in training_files:
    training_images.append(PIL.Image.open(training_directory + "\\" + image_directory))

#html_tags = ["<p></p>"]

#Function for extracting text from image 
def extract_text(PIL_open):
    return pytesseract.image_to_string(PIL_open)

print(extract_text(training_images[3]).split("\n\n"))

#Creating the html file
def create_html_doc(name,PIL_open):
    main_tags = ["<html>","<head>","<title>","<body>"]
    additional_tag = ["<p>"]

    with open(name + ".html","a+") as f:
        f.write("<html>")




        f.write("</html>")
        f.close()

    