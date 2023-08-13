from pytube import YouTube
from tkinter import filedialog 
url_input=input("enter the linke:")
all_streams = YouTube(url_input).streams.all()
print(all_streams)
v=-1
for i in all_streams:
    v=v+1
    print(str(v)+" : "+str(i))
stm_input=int(input("please chose the stream"))
print("please chose directory to save")
folder_name =filedialog.askdirectory()
choice=all_streams[stm_input].download(folder_name)
print("download completed--------------")
