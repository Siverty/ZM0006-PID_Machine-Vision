# # Install pdf2image: pip install pdf2image
# import subprocess
# try:
#     subprocess.check_call(["pip", "install", "pdf2image"])
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")

# General imports 
import fitz  # PyMuPDF
import os
import shutil

check_for_pdf_in_folder = "/test/Original_PID"
copy_folder = "/test/Original_PID_PDF"

def pdf_to_png(pdf_file, output_directory):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Iterate through each page and convert it to PNG
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        image_list = page.get_pixmap()
        image_file = f"{output_directory}/page_{page_number + 1}.png"

        # Save the page as a PNG image
        image_list.save(image_file, "png")

    # Close the PDF file
    pdf_document.close()

def convert_and_move_pdfs(check_for_pdf_in_folder, copy_folder):
    # Ensure the output directory exists
    os.makedirs(copy_folder, exist_ok=True)

    # List all files in the check folder
    files = os.listdir(check_for_pdf_in_folder)

    for file in files:
        if file.endswith(".pdf"):
            pdf_file_path = os.path.join(check_for_pdf_in_folder, file)
            png_output_dir = os.path.join(copy_folder, os.path.splitext(file)[0])

            # Convert the PDF to PNG
            pdf_to_png(pdf_file_path, png_output_dir)

            # Move the PDF file to the copy folder
            shutil.move(pdf_file_path, os.path.join(copy_folder, file))

if __name__ == "__main__":
    check_for_pdf_in_folder = "test/Original_PID"  # Replace with the directory where you want to check for PDFs
    copy_folder = "test/Original_PID_PDF"  # Replace with the directory where you want to move the PDFs

    convert_and_move_pdfs(check_for_pdf_in_folder, copy_folder)
