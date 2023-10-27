import os
import fitz  # PyMuPDF
from PIL import Image

# Specify the input and output folders
input_folder = 'test\Converted_PID_JPEG'
output_folder = 'test\Original_PID'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through the PDF files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        pdf_file = os.path.join(input_folder, filename)

        # Open the PDF file using PyMuPDF
        pdf_document = fitz.open(pdf_file)

        # Iterate through the pages and save each page as a PNG
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            image = page.get_pixmap()
            png_file = os.path.splitext(filename)[0] + f'_page{page_num + 1}.png'
            png_path = os.path.join(output_folder, png_file)
            image.save(png_path)

        # Close the PDF file
        pdf_document.close()

print("Conversion complete.")
