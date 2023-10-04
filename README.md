# DOI-to-BibTeX-Converter

Overview
DOI to BibTeX Converter is a simple and effective GUI-based utility designed to automate the process of fetching BibTeX entries from a list of DOIs (Digital Object Identifiers). The application provides a user-friendly interface, allowing users to upload a file containing a list of DOIs, and automatically fetches the corresponding BibTeX entries, saving them as .bib files in a designated folder.

Features
Upload DOI List: Users can upload a text file containing a list of DOIs.
Fetch BibTeX Entries: Automatically fetches BibTeX entries for each DOI in the list.
Save BibTeX Files: Saves each BibTeX entry as a .bib file named after the DOI it corresponds to.
Error Logging: Logs any DOIs for which BibTeX entries could not be fetched, saving them to a text file for further review.
User-friendly GUI: Utilizes Tkinter for a simple and user-friendly graphical user interface.

Usage
run the script using python
Click on the "Upload DOI List" button to upload a text file containing a list of DOIs (one DOI per line).
Select a folder to save the BibTeX files.
The application will process the DOIs, fetch the corresponding BibTeX entries, and save them as .bib files in the selected folder.
If there were any DOIs for which BibTeX entries could not be fetched, they will be logged to a file named error_dois.txt in the same folder.
Dependencies
Tkinter for the GUI.
Requests library for handling HTTP requests.


Created with :heart: by Dextro_Devil
