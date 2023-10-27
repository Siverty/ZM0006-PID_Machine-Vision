# Import necessary modules
from blur import blur_images
from erode import erode_images
from noise import add_noise
from mosaic import mosaic_images
from pdf_to_png_converter import pdf_to_png_converter
import os

# Set train and label folder paths
train_folder = './datasets/Labels_PID/images/train'
label_folder = './datasets/Labels_PID/labels/train'
input_folder = 'test\Converted_PID_JPEG'
output_folder = 'test\Original_PID'

# Loop through images in train folder
for filename in os.listdir(train_folder):
    # Convert pdf to png
    pdf_to_png_converter(input_folder, output_folder)

    # Apply blur
    img = blur_images(train_folder, label_folder)

    # Apply erosion
    img = erode_images(train_folder, label_folder)

    # Add noise
    img = add_noise(train_folder, label_folder)

    # Apply mosaic
    img = mosaic_images(train_folder, label_folder)
