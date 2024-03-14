import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader, PdfWriter
from dotenv.main import StrPath

load_dotenv(dotenv_path='./.env')
PDF_PASSWORD = os.environ.get('PDF_PASSWORD')


def remove_password(input_pdf_path: StrPath, output_pdf_path: StrPath, password: str) -> bool:
    try:
        with open(input_pdf_path, 'rb') as input_file:
            reader = PdfReader(input_file)
            if reader.is_encrypted:
                reader.decrypt(password)

            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def process_pdfs(input_folder: StrPath, output_folder: StrPath, password: str) -> None:
    print("Processing PDFs...\n")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)
        if file_name.endswith('.pdf'):
            if remove_password(input_file_path, output_file_path, password):
                print(f"Successfully removed password from: {file_name}")
            else:
                print(f"Failed to remove password from: {file_name}")
    print("\nAll PDFs in the input folder have been processed.")


if __name__ == '__main__':
    input_folder: StrPath = './input'  # Specify the folder containing password-protected PDFs
    output_folder: StrPath = './output'  # Specify the folder where unprotected PDFs will be saved
    password: StrPath = PDF_PASSWORD  # Set this in the .env file

    process_pdfs(input_folder=input_folder, output_folder=output_folder, password=password)
