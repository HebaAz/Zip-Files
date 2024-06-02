import zipfile

def extract_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as archiveFile:
        archiveFile.extractall(dest_dir)