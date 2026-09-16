import os
import shutil
import json
from datetime import datetime
from report import create_report

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def get_category(filename, config):
    ext= os.path.splitext(filename)[1].lower()
    for category, extensions in config.items():
        if ext in extensions:
            return category
    return "Others"


def organise_folder(folder_path):
    config = load_config()
    organised_path = os.path.join(folder_path, "organised_files")
    os.makedirs(organised_path, exist_ok=True)

    log=[]  ## to store what we moved

    print(f"Organising: {folder_path}")

    for filename in os.listdir(folder_path):
        file_path= os.path.join(folder_path, filename)

        ##skip folders and the script itself
        if os.path.isdir(file_path) or filename in ["organiser.py", "report.py", "config.json"]:
            continue

        category = get_category(filename, config)
        category_path = os.path.join(organised_path, category)
        os.makedirs(category_path, exist_ok=True)

        new_path= os.path.join(category_path, filename)

        ## handle duplicate file names
        if os.path.exists(new_path):
            name, ext= os.path.splitext(filename)
            new_filename= f"{name}_{datetime.now().strftime('%H%M%S')}{ext}"
            new_path= os.path.join(category_path, new_filename)

        shutil.move(file_path, new_path)

        log.append({
            "Filename": filename,
            "New Location": new_path,
            "Category": category,
            "Date Moved": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Moved: {filename}  -> {category}")

    if log:
        create_report(log)
        print(f"\nDone!!  {len(log)} files organised.")
        print("Report saved as organisation_report.xlsx")
    else:
        print("No files to organise")


if __name__ == "__main__":
    target_folder = input("Enter the full path of the folder to organise: ").strip()
    if os.path.isdir(target_folder):
        organise_folder(target_folder)
    else:
        print("Folder not found! Try again with a valid path.")
