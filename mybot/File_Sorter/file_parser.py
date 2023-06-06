import sys
from pathlib import Path
import File_Sorter.constants

def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                File_Sorter.constants.FOLDERS.append(item)
                scan(item)
            continue
        else:
            ext = get_extensions(item.name)
            full_name = folder / item.name
            if not ext:
                File_Sorter.constants.MY_OTHER.append(full_name)
            else:
                try:
                    container = File_Sorter.constants.REGISTER_EXTENSION[ext]
                    File_Sorter.constants.EXTENSION.add(ext)
                    container.append(full_name)
                except KeyError:
                    File_Sorter.constants.UNKNOWN.add(ext)
                    File_Sorter.constants.MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    scan(Path(folder_for_scan))