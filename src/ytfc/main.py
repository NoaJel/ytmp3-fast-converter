import os
from io_manager import MP3_DOWNLOAD_FOLDER_PATH, URLS_FILE_PATH, check_if_app_paths_exist, get_urls_from_text_file
from yt_dlp_manager import download_videos_as_mp3, get_videos_with_artist_and_track


def main():
    check_if_app_paths_exist()

    urls = get_urls_from_text_file(URLS_FILE_PATH)
    urls_with_music_info = get_videos_with_artist_and_track(urls)

    download_videos_as_mp3(
        urls_with_music_info,
        os.path.join(
            MP3_DOWNLOAD_FOLDER_PATH, f"{'%(artist)s'} - {'%(track)s'}.mp3"),
    )

    download_videos_as_mp3(
        urls.difference(*[urls_with_music_info]),
        os.path.join(
            MP3_DOWNLOAD_FOLDER_PATH, f"{'%(title)s'}.mp3"),
    )


if __name__ == "__main__":
    main()
