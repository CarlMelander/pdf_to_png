import fitz  # PyMuPDF
from PIL import Image

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
        with open(f'{output_folder}/page_{page_number + 1}.png', 'wb') as img_file:
            img_file.write(pix.tobytes('png'))

    pdf.close()

pdf_file_path = 'C:/Users/pant/Desktop/sample.pdf'  
output_directory = 'C:/Users/pant/Desktop/PDFtoPNG'      
convert_pdf_to_png(pdf_file_path, output_directory)
