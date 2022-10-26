# Get-Youtube-Video-Details-and-Download-Youtube-Video-in-MP3-Format-Using-Python
Get Youtube Video Details and Download Youtube Video in MP3 Format Using Python

## Following are the properties(information about the YouTube video) of the YouTube object which we can access:
1. Title
2. Length
3. Thumbnail_URL
4. Description
5. Views*
6. Rating*
7. Age Restricted
8. Video Id


## Before Run this code install :
```
pip install pytube
```

## Run this code
```
from pytube import YouTube
import os

youTube = YouTube(str(input("Please, Enter Your URL:")))


video = youTube.streams.filter(only_audio=True).first()
print("Enter your Destination for Save the file or (Leave Blank to Save in Parent Folder)")
destination = str(input(">> ")) or '.'

outFile = video.download(output_path=destination)

base, ext = os.path.splitext(outFile)
newFile = base+".mp3"
os.rename(outFile, newFile)

print(youTube.title + "has been downloaded")

print("\n\n")
print("Title: " + youTube.title)
print("Video length: " + str(youTube.length))
print("Thumbnail: " + youTube.thumbnail_url)
print("Description: " + youTube.description)
print("Views: " + str(youTube.views))
print("Rating: " + str(youTube.rating))
print("Age restricted: " + str(youTube.age_restricted))
print("Video id: " + youTube.video_id)
```

## Code. 
![Code](https://github.com/NowshadRuhan/Get-Youtube-Video-Details-and-Download-Youtube-Video-in-MP3-Format-Using-Python/blob/main/photo.png?raw=true) 
