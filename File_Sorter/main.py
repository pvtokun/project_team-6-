from pathlib import Path
from File_Sorter.normalize import normalize
import File_Sorter.constants
import shutil
import File_Sorter.file_parser as parser


def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_arhive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
        print('архів було створенно')
    except shutil.ReadError:
        print('архів не було створенно')
        folder_for_file.rmdir()
        return None
    filename.unlink()

def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')

def sorter(folder: Path) -> None:
    parser.scan(folder)
    for file in parser.File_Sorter.constants.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.File_Sorter.constants.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.File_Sorter.constants.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.File_Sorter.constants.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser.File_Sorter.constants.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
    for file in parser.File_Sorter.constants.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.File_Sorter.constants.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.File_Sorter.constants.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')

    for file in parser.File_Sorter.constants.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.File_Sorter.constants.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in parser.File_Sorter.constants.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.File_Sorter.constants.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')

    for file in parser.File_Sorter.constants.DOC_DOCS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.File_Sorter.constants.DOCX_DOCS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.File_Sorter.constants.PDF_DOCS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.File_Sorter.constants.TXT_DOCS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.File_Sorter.constants.PPTX_DOCS:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in parser.File_Sorter.constants.XLSX_DOCS:
        handle_media(file, folder / 'documents' / 'XLSX')

    for file in parser.File_Sorter.constants.GZ_ARCHIVES:
        handle_arhive(file, folder / 'archives' / 'GZ')
    for file in parser.File_Sorter.constants.ZIP_ARCHIVES:
        handle_arhive(file, folder / 'archives' / 'ZIP')
    for file in parser.File_Sorter.constants.TAR_ARCHIVES:
        handle_arhive(file, folder / 'archives' / 'TAR')

    for file in parser.File_Sorter.constants.MY_OTHER:
        handle_media(file, folder / 'other')

    for folder in parser.File_Sorter.constants.FOLDERS[::-1]:
        handle_folder(folder)

