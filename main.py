import os
import sys
import hashlib
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def authenticate():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("client_secrets.json")
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def find_file(drive, filename):
    query = f"title='{filename}' and 'root' in parents and trashed=false"
    files = drive.ListFile({'q': query}).GetList()
    return files[0] if files else None

def sync_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("[Error] Folder does not exist.")
        return

    folder_path = os.path.abspath(folder_path)
    drive = authenticate()

    for root, _, files in os.walk(folder_path):
        for filename in files:
            local_file_path = os.path.join(root, filename)
            local_md5 = calculate_md5(local_file_path)

            existing_file = find_file(drive, filename)

            if existing_file:
                if existing_file.get('md5Checksum') != local_md5:
                    existing_file.SetContentFile(local_file_path)
                    existing_file.Upload()
                    print(f"[Updated] {filename}")
                else:
                    print(f"[Skipped] {filename} (no changes)")
            else:
                new_file = drive.CreateFile({
                    'title': filename,
                    'parents': [{'id': 'root'}]
                })
                new_file.SetContentFile(local_file_path)
                new_file.Upload()
                print(f"[Uploaded] {filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = input("Enter path to folder to sync: ")

    sync_folder(folder_path)
