import FreeSimpleGUI as sg
from zip_extractor import extract_archive

#row 1
archive_label = sg.Text("Select archive: ")
archive_input = sg.InputText(key='archive')
archive_button = sg.FileBrowse("Archives")

#Row 2
destination_label = sg.Text("Select destination: ")
destination_input = sg.InputText(key='destination')
destination_button = sg.FolderBrowse("Destinations")

#Row 3
extract = sg.Button("Extract")
message = sg.Text("", key="message")


window = sg.Window('Archive Extractor',
                   layout=[[archive_label, archive_input, archive_button],
                           [destination_label, destination_input, destination_button],
                           [extract, message]])

while True:
    event, values = window.read()
    
    filepath = values["archive"]
    dest_dir = values["destination"]

    extract_archive(filepath, dest_dir)
    
    window["message"].update(value="Completed!")

window.close()