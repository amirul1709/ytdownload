from pytube import YouTube
from sys import argv

# Get the link from the command line
ytLink = argv[1]
# Create a YouTube object
yt = YouTube(ytLink)

print("Title: ", yt.title)
print("Number of views: ", yt.views)

#ytDownload = yt.streams.get_lowest_resolution()

#print("Downloading...")

#ytDownload.download("/Users/amirulhossain/Desktop")