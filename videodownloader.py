from __future__ import unicode_literals
import youtube_dl

video = input("Please input full youtube link here\n >>>")

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',       
    'outtmpl': '%(id)s',        
    'noplaylist' : True,        
    'progress_hooks': [my_hook],  
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video])
