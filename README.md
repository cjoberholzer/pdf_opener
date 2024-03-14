# PDF Opener

## Description
This is a simple python script that opens all the PDFs in the `input` directory and saves them to the `output` 
directory after removing their passwords.

## Purpose
- Remove passwords from PDFs

## Setup
1. Create a virtual environment
   - ```bash 
        python3 -m venv .venv
     ```
2. Activate the virtual environment
   - ```bash 
        source .venv/bin/activate
     ```
3. Install the requirements
    - ```bash
         pip install -r requirements.txt
      ```
4. Create a `.env` file
    - ```bash
         cp .env-template .env
      ```
5. Set the `PDF_PASSWORD` environmental variable in the newly created `.env` file.

## Usage
1. Copy all the PDFs into the input directory
2. Ensure that the Password for the PDFs has been set in the `PDF_PASSWORD` environmental variable in the created `.env` file.
   - [.env file (example)](.env-template)
3. Run the script
   - ```bash
     python3 main.py
     ```