import fitz  # PyMuPDF
from PIL import Image
import os

def convert_pdf_to_png(pdf_path, output_folder):

    # Open the PDF file
    pdf = fitz.open(pdf_path)

    # Iterate pages
    for page_number in range(len(pdf)):
        # Get page
        page = pdf.load_page(page_number)

        # Render pixmap 
        pix = page.get_pixmap()

        # Save pixmap
        with open(f'{output_folder}/{os.path.splitext(os.path.basename(pdf_path))[0]}_Page_{page_number + 1}.png', 'wb') as img_file:
            img_file.write(pix.tobytes('png'))

    pdf.close()

pdf_file_path = 'path/to/source.pdf'  
output_directory = 'path/to/output_folder'      
convert_pdf_to_png(pdf_file_path, output_directory)
