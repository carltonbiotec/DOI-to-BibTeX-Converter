import tkinter as tk
from tkinter import ttk, filedialog
import requests
import os
import re

def get_bibtex_from_doi(doi):
    headers = {
        "Accept": "application/x-bibtex",
    }
    response = requests.get(f"https://doi.org/{doi}", headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def process_doi_list():
    filepath = filedialog.askopenfilename(title="Select DOI List File")
    if not filepath:
        return
    
    save_directory = filedialog.askdirectory(title="Select Folder to Save BibTeX Files")
    if not save_directory:
        return

    error_dois = [] # To log DOIs for which BibTeX was not found

    with open(filepath, 'r') as f:
        dois = f.readlines()

    for doi in dois:
        doi = doi.strip()
        bibtex = get_bibtex_from_doi(doi)
        
        if bibtex:
            # Sanitize the filename
            sanitized_doi = re.sub('[^a-zA-Z0-9]', '_', doi)[:200]  # Using regex to replace all non-alphanumeric characters and limiting length
            output_filename = os.path.join(save_directory, f"{sanitized_doi}.bib")

            with open(output_filename, 'w') as out_file:
                out_file.write(bibtex)
        else:
            error_dois.append(doi)
    
    # Save the DOIs with errors to a log file
    if error_dois:
        with open(os.path.join(save_directory, "error_dois.txt"), 'w') as log_file:
            log_file.write("\n".join(error_dois))

    result_label.config(text=f"Processed {len(dois)} DOIs. Check the selected folder for outputs and errors!")

def main():
    root = tk.Tk()
    root.title('DOI List to BibTeX Files')

    ttk.Button(root, text="Upload DOI List", command=process_doi_list).pack(pady=20)
    
    global result_label
    result_label = ttk.Label(root, text="")
    result_label.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()
