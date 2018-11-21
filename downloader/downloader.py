import youtube_dl
import os
import re
def GetOpenloadVideo(path,filename):
    print(path)
    print(filename)
    ydl = youtube_dl.YoutubeDL({'outtmpl': filename})
    with ydl:
        youtube_dlresult = ydl.extract_info(
            path,
            download=True  # !!We just want to extract the info
        )
    if 'entries' in youtube_dlresult:
        # Can be a playlist or a list of videos
        video = youtube_dlresult['entries'][0]
    else:
        # Just a video
        video = youtube_dlresult
    return video

if __name__ == "__main__":
    GetOpenloadVideo('https://openload.co/stream/TOBGE5yJfQs~1542894682~163.44.0.0~j8lgwfdJ?mime=true','ddt-551.mp4')