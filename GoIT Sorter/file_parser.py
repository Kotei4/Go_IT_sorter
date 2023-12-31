import sys
from pathlib import Path

#Оголошуємо константи
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO= []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
MY_OTHER = []



REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    "OGG": MP3_AUDIO,
    "WAV": WAV_AUDIO,
    "AMR": AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
    "AVI": AVI_VIDEO,
    'MP4': MP4_VIDEO,
    "MOV": MOV_VIDEO,
    "MKV": MKV_VIDEO,
    "DOC": DOC_DOCUMENTS,
    "DOCX": DOCX_DOCUMENTS,
    "TXT": TXT_DOCUMENTS,
    "PDF": PDF_DOCUMENTS,
    "XLSX": XLSX_DOCUMENTS,
    "PPTX": PPTX_DOCUMENTS,

}

FOLDERS = []        #
EXTENSIONS = set()  # Визначаємо Множество розширень файлів
UNKNOWN = set()     # Визначаємо Множество розширень файлів які ми не знаємо

def get_extension(name: str) -> str: #######SHYO MY CYM ROBYMO ->
    return Path(name).suffix[1:].upper() # suffix[1:] ->  .jpg -> JPG

def scan(folder: Path):
    for item in folder.iterdir():
        # РОБОТА З ПАПКОЮ
        if item.is_dir():   # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)    #RECURSION
            continue

        # РОБОТА З ФАЙЛОМ
        extension = get_extension(item.name)    # беремо розширення файлу
        full_name = folder / item.name          # беремо повний шлях до файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio mp3: {OGG_AUDIO}')
    print(f'Audio wav: {WAV_AUDIO}')
    print(f'Audio amr: {AMR_AUDIO}')
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
    print(f'Documents doc: {DOC_DOCUMENTS}')
    print(f'Documents docx: {DOCX_DOCUMENTS}')
    print(f'Documents txt: {TXT_DOCUMENTS}')
    print(f'Documents pdf: {PDF_DOCUMENTS}')
    print(f'Documents xlsx: {XLSX_DOCUMENTS}')
    print(f'Documents pptx: {PPTX_DOCUMENTS}')
    print(f'Archive zip: {ZIP_ARCHIVES}')
    print(f'Archive gz: {GZ_ARCHIVES}')
    print(f'Archive tar: {TAR_ARCHIVES}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
    print(f'FOLDERS: {FOLDERS}')