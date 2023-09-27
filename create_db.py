import os
import sqlite3


def main():
    transcripts_txt_dir = "transcripts/txt/"

    con = sqlite3.connect("wolf.db")
    cur = con.cursor()

    # create table to hold video data
    cur.execute('CREATE TABLE IF NOT EXISTS "videos" ( \
                "id"    TEXT NOT NULL UNIQUE, \
                "title"     TEXT NOT NULL, \
                "upload_date"	TEXT NOT NULL, \
                PRIMARY KEY("id"));')

    cur.execute('CREATE VIRTUAL TABLE IF NOT EXISTS "transcripts" USING fts5('
                'video_id, timestamp, transcript);')

    # add videos to db
    i = 1
    for filename in os.listdir(transcripts_txt_dir):
        video_info = filename.split("#", 2)  # [id, upload_date, title]

        # format date to: yyyy-mm-dd
        upload_date = video_info[1][:4] + "-" + video_info[1][4:6] + "-" + \
               video_info[1][6:]

        # remove ".en.txt" extension from end of title
        title = video_info[2][:-7]

        # add video info to db
        cur.execute('INSERT OR REPLACE INTO videos(id, title, upload_date) '
                    'VALUES(?,?,?)',
                    (video_info[0], title, upload_date))

        # open video transcript file
        with open(transcripts_txt_dir + filename, "r") as f:
            # separate transcript into chunks of text based on timestamp
            file_data = f.read().strip().split("\n\n")

            for blob in file_data:
                # [timestamp, transcript_text]
                blob = blob.split("\n", 1)

                if len(blob) == 1:
                    # no text for current timestamp
                    continue

                transcript_text = blob[1].replace("\n", " ")

                # add video info to db
                cur.execute(
                    'INSERT OR REPLACE INTO transcripts(video_id, timestamp, '
                    'transcript) VALUES(?,?,?)',
                    (video_info[0], blob[0], transcript_text))

        print(i)
        i += 1

    con.commit()


if __name__ == "__main__":
    main()
