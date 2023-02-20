# YTmp3 Fast Converter (YTFC)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=NoaJel_ytmp3-fast-converter&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=NoaJel_ytmp3-fast-converter)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=NoaJel_ytmp3-fast-converter&metric=coverage)](https://sonarcloud.io/summary/new_code?id=NoaJel_ytmp3-fast-converter)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=NoaJel_ytmp3-fast-converter&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=NoaJel_ytmp3-fast-converter)

**Quickly** download music from **YouTube** using a URL file and convert all to **MP3** *in one go*!

## How does it work?

:white_check_mark: YTmp3 Fast Converter uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to make get video information and do the downloading under the hood.  
:link: YTFC uses a URL file that stores the URL of every video you want to download.  
:zap: Once the desired video URLs are pasted in, simply run the program and watch your audio getting downloaded!

## Running the program

:arrow_right: Run the program by executing the provided batch file at the project root: `ytmp3-fast-converter.bat`. A simple double-click should do the trick :wink:

## How to use

:file_folder: On the first launch, the `YTmp3 Fast Converter` directory will be created in your `Downloads` folder.  
:spiral_notepad: You will be able to paste your video URLs in the `videos_to_download_urls.txt` file.  
This file needs to contain only one url per line. :bulb:  
:arrow_down: Running the program will download every video in the URL file with an MP3 format, in the `Downloaded music` folder.

## Additional information

:musical_note: This program is primarily meant to download many music from YouTube at once.  
:green_heart: Therefore, the downloaded files are named following the convention `<artist_name> - <track_name>`, i.e. `PSY - Gangnam Style`.  
:blue_heart: If no information about an artist or a track name is available, YTFC names the file according to the video title, i.e. `PSY- Gangnam Style (Official Music Video)`.

:soon: New features, such as changing the download folder location or having a standalone executable, are currently under developement.  
:information_source: This is a small project I am primarily making for myself, so please be patient and be kind if opening an issue. Thank you for using YTFC! :sparkling_heart:
