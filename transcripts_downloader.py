#
# downloads auto-generated subtitles from youtube videos
#

import scrapetube
import subprocess


def main():
    # get all videos from channel
    videos = scrapetube.get_channel(
        channel_url="https://www.youtube.com/@SSSniperWolf")

    ytdl_path = "yt-dlp.exe"
    i = 1
    for video in videos:
        arg = "yt-dlp --write-auto-sub --output transcripts/%(id)s#%(upload_date)s#%(title)s --skip-download " \
              "https://www.youtube.com/watch?v=" + video["videoId"]
        subprocess.run(arg, stdout=subprocess.DEVNULL)
        print(i)
        i += 1


if __name__ == "__main__":
    main()
