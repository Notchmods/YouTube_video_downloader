from pytubefix import YouTube
from pytubefix.cli import on_progress

#Extract first command line argument
yt_link = input("Enter the link of the video that you want to download: ")

#Fetch the video on YouTube

vid_link= YouTube(yt_link,on_progress_callback = on_progress)

print("Title: ",vid_link.title)

print("Views: ",vid_link.views)

#Get the highest resolution for video

Res= vid_link.streams.get_highest_resolution()

Res.download()


