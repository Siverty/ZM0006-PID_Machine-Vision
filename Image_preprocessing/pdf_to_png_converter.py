import os
import subprocess
import shutil

check_for_pdf_in_folder = "test/Original_PID"
copy_folder = "test/Original_PID_PDF"

def pdf_to_png_converter(check_for_pdf_in_folder, copy_folder):

    pdf_files = [f for f in os.listdir(check_for_pdf_in_folder) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        shutil.move(os.path.join(check_for_pdf_in_folder, pdf_file), copy_folder)

    pdf_files = [f for f in os.listdir(check_for_pdf_in_folder) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        # Use Ghostscript to convert the PDF to PNG
        output_folder = os.path.join(check_for_pdf_in_folder, pdf_file[:-4])
        os.makedirs(output_folder, exist_ok=True)
        cmd = [
            "gs",
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE=png16m",
            "-r300",  # Set the resolution (adjust as needed)
            f"-sOutputFile={output_folder}/%03d.png",  # Output file format
            os.path.join(check_for_pdf_in_folder, pdf_file)
        ]
        subprocess.run(cmd)

pdf_to_png_converter(check_for_pdf_in_folder, copy_folder)
