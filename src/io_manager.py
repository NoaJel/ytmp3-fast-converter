import os
from pathlib import Path

from folder_uuid import FolderUuid
from globals import WARNING_ERROR_MESSAGE

from known_paths import get_path_from_folder


DOWNLOADS_FOLDER = get_path_from_folder(FolderUuid.downloads)
YTMP3_FAST_CONVERTER_FOLDER = "YTmp3 Fast Converter"
YTMP3_FAST_CONVERTER_FOLDER_PATH = os.path.join(
    DOWNLOADS_FOLDER, YTMP3_FAST_CONVERTER_FOLDER)

URLS_FILE = "videos_to_download_urls.txt"
MP3_DOWNLOAD_FOLDER = "Downloaded music"

URLS_FILE_PATH = os.path.join(
    YTMP3_FAST_CONVERTER_FOLDER_PATH, URLS_FILE)
MP3_DOWNLOAD_FOLDER_PATH = os.path.join(
    YTMP3_FAST_CONVERTER_FOLDER_PATH, MP3_DOWNLOAD_FOLDER)


URLS_FILE_EMPTY_ERROR_MESSAGE = "Please paste the URLs of the YouTube videos you want to convert and download, before running the program again."


def check_if_app_paths_exist():
    is_needed_path_not_existing = False

    if not os.path.exists(MP3_DOWNLOAD_FOLDER_PATH):
        Path(MP3_DOWNLOAD_FOLDER_PATH).mkdir(exist_ok=True, parents=True)
        is_needed_path_not_existing = True

    if not os.path.exists(URLS_FILE_PATH):
        f = open(URLS_FILE_PATH, 'w')
        f.close()

        print(
            f"{WARNING_ERROR_MESSAGE} No URL file has been found. A new file at '{URLS_FILE_PATH}' has been created. {URLS_FILE_EMPTY_ERROR_MESSAGE}")
        is_needed_path_not_existing = True

    if is_needed_path_not_existing:
        exit()


def get_urls_from_text_file(file_path: str):
    if os.stat(file_path).st_size != 0:
        with open(file_path, 'r+') as url_file:
            lines = url_file.readlines()
            url_list = [line for line in lines if not line.isspace()]
            return frozenset(url_list)
    else:
        print(
            f"{WARNING_ERROR_MESSAGE} Your URLs file is empty, hence not containing anything to convert. {URLS_FILE_EMPTY_ERROR_MESSAGE}",
        )
        exit()
