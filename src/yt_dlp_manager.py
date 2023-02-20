import yt_dlp


def get_videos_with_artist_and_track(video_urls):
    urls_with_artist_and_track_info = set()

    for url in video_urls:
        video_info = get_video_info(url)
        if video_info == None:
            continue

        if 'artist' in video_info and 'track' in video_info:
            urls_with_artist_and_track_info.add(url)

    return urls_with_artist_and_track_info


def get_video_info(yt_url):
    try:
        return yt_dlp.YoutubeDL().extract_info(url=yt_url, download=False)
    except Exception as e:
        print(e)
        return None


def download_videos_as_mp3(urls, music_file_format_template):
    YDL_DEFAULT_MUSIC_OPTIONS = {
        'format': "bestaudio/best",
        'keepvideo': False,
    }

    options = YDL_DEFAULT_MUSIC_OPTIONS
    options['outtmpl'] = music_file_format_template
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            ydl.download(urls)
        except Exception as e:
            print(e)
