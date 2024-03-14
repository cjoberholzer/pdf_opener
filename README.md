# PDF Opener

## Description
This is a simple python script that opens all the PDFs in the `input` directory and saves them to the `output` 
directory after removing their passwords.

## Purpose
- Remove passwords from PDFs

## Usage
1. Copy all the PDFs into the input directory
2. Set the Password for the PDFs in the `PDF_PASSWORD` environmental variable in the [.env file](.env)
3. Run the script
   - ```bash
     python main.py
     ```