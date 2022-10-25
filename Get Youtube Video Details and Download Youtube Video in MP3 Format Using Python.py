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