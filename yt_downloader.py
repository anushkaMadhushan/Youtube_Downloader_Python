from pytube import YouTube

link = input("Video Link : ")
Download_video_link = YouTube(link)
Title = Download_video_link.title
Num_of_Views = Download_video_link.views
Length_of_Video = Download_video_link.length
Author_of_Video = Download_video_link.author

print("Title: ",Title)
print("Num of Views: ",Num_of_Views)
print("Length of Video: ",Length_of_Video)
print("Author of Video: ",Author_of_Video)


Download_video_link.streams.get_highest_resolution().download()
print("Download Completed")