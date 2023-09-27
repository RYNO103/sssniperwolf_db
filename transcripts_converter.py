import os
import subprocess

import vtt2text


def main():
    i = 1
    for filename in os.listdir("transcripts"):
        vtt2text.run("transcripts/" + filename)
        print(i)
        i += 1


if __name__ == "__main__":
    main()
