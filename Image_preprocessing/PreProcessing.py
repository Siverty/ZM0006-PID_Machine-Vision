# Import necessary modules
from blur import blur_images 
from erode import erode_images
from noise import add_noise
from mosaic import mosaic_images
from pdf_to_png_converter import pdf_to_png_converter
from to_png_converter import any_to_png_converter
import os

# Set train and label folder paths
train_folder = './datasets/Labels_PID/images/train'
label_folder = './datasets/Labels_PID/labels/train'
input_folder = 'test\P&ID_input'
output_folder = 'test\Original_PID_PNG'

# Loop through images in train folder
for filename in os.listdir(train_folder):
    # Convert pdf to png
    pdf_to_png_converter(input_folder, output_folder)

    # Convert any image to png
    img = any_to_png_converter(train_folder)

    # Apply blur
    img = blur_images(train_folder, label_folder)

    # Apply erosion
    img = erode_images(train_folder, label_folder)

    # Add noise
    img = add_noise(train_folder, label_folder)

    # Apply mosaic
    img = mosaic_images(train_folder, label_folder)
