import os
import fitz  # PyMuPDF
from PIL import Image
import shutil

def pdf_to_png_converter(input_folder, output_folder):
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

                # Set the resolution (DPI) for the image
                resolution = 300  # You can adjust this as needed
                pixmap = page.get_pixmap(matrix=fitz.Matrix(resolution/72, resolution/72))

                # Convert the Pixmap to a Pillow Image
                image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

                # Set the quality factor (0-100). A higher value results in better quality and larger file size.
                quality = 95  # You can adjust this as needed

                # Save the image with the specified quality
                png_file = os.path.splitext(filename)[0] + f'_page{page_num + 1}.png'
                png_path = os.path.join(output_folder, png_file)
                image.save(png_path, 'PNG', quality=quality)

            # Close the PDF file
            pdf_document.close()

    # Move every .png file to the output folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            png_file = os.path.join(input_folder, filename)
            shutil.move(png_file, output_folder)
            print(f'{png_file} moved to {output_folder}')

    print("PDF conversion complete.")
