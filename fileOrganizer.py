import os
import json
import shutil


def load_config():
    try:
        with open("config.json", "r") as config:
            return json.load(config)
    except Exception as e:
        print(f"[ERROR] Error loading config file: {e}")


def organize_files():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    dictionary = load_config()

    try:
        for file in files:
            if file in ['config.json', 'fileOrganizer.py']:
                continue

            file_path = os.path.join(current_directory, file)
            moved = False

            for folder_name, formats in dictionary.items():
                if any(file.endswith(format) for format in formats):
                    if not os.path.exists(folder_name):
                        os.mkdir(folder_name)
                    destination_path = os.path.join(current_directory, folder_name, file)
                    shutil.move(file_path, destination_path)
                    print(f"File {file} moved to {destination_path}")
                    moved = True
                    break

            if not moved:
                if not os.path.exists('other'):
                    os.mkdir('other')
                destination_path = os.path.join(current_directory, 'other', file)
                shutil.move(file_path, destination_path)
                print(f"File {file} moved to {destination_path}")

    except Exception as e:
        print(f"[ERROR] Error moving {file}")
        print(e)


if __name__ == "__main__":
    print("Press any key to start")
    input()

    organize_files()

    print("Press any key to close")
    input()

# исключения файлов, многопоточность, tqdm
