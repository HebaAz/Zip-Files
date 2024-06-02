import FreeSimpleGUI as sg
from zip_creator import make_archive

#Buttons
compress_choose = sg.FilesBrowse("Choose", key = "files")
destination_choose = sg.FolderBrowse("Choose", key = "folder")
submit = sg.Button("Compress")

#Text fields
compress_input = sg.Input()
destination_input = sg.Input()

#Labels
compress_label = sg.Text("Select files to compress: ")
destination_label = sg.Text("Select destination folder: ")
message = sg.Text("", key='message')

main_window = sg.Window('File Zipper', layout = [[compress_label, compress_input, compress_choose], 
                                                 [destination_label, destination_input, destination_choose], 
                                                 [submit, message]])

while True:
    event, values = main_window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]

    make_archive(filepaths, folder)

    main_window["message"].update(value = "Compression was completed!")

main_window.close()
