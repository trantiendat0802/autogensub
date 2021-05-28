from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from moviepy.editor import *
from tkinter import *
import tkinter as tk
import youtube_dl
import requests
import hashlib
import os.path
import tkinter
import json
import os


################################################################################################# 

# def opend_jsonFile():
#     with open('D:\\Semeter3\\OSG202\\txt\\data.txt') as json_file:
#         datar = json.load(json_file) 

#     print(datar) 
    
################################################################################################# 

def save_to_folder_path ():
    currdir = os.getcwd()
    file_path = filedialog.asksaveasfilename(parent=app, initialdir=currdir, title='Please select a directory')
    if len(file_path) > 0:
        print ("File Path: %s" % file_path)
    return file_path    

################################################################################################# 

def save_to_folder_path2 ():
    currdir = os.getcwd()
    file_path = filedialog.asksaveasfilename(parent=app, initialdir=currdir, title='Please select a directory')
    if len(file_path) > 0:
        print ("File Path: %s" % file_path)
    return file_path   
#################################################################################################

def vid_to_aud_ori():
    # mp4_info = mp4.get()
    # mp3_info = mp3.get()   

    mp4_file = r'D:\Semeter3\OSG202\Video\news2.mp4'
    mp3_file = r'D:\Semeter3\OSG202\sound convert\news2.mp3'

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()

#################################################################################################

# def open_file():
#     global file_path
#     filename = askopenfilename()
#     file_path = os.path.dirname(filename)
#     return file_path

#################################################################################################

def browsermp4():
    currdir = os.getcwd()
    file_path = filedialog.askopenfilename(parent=app, initialdir=currdir, title='Please select a directory')
    if len(file_path) > 0:
        print ("File Path: %s" % file_path)
    mp4.set(file_path)

#################################################################################################

def browsermp3():
    currdir = os.getcwd()
    file_path = filedialog.askopenfilename(parent=app, initialdir=currdir, title='Please select a directory')
    if len(file_path) > 0:
        print ("File Path: %s" % file_path)
    mp3.set(file_path)

#################################################################################################

def browsertxt():
    currdir = os.getcwd()
    file_path = filedialog.askopenfilename(parent=app, initialdir=currdir, title='Please select a directory')
    if len(file_path) > 0:
        print ("File Path: %s" % file_path)
    subtitle.set(file_path)

#################################################################################################

def search_for_folder_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=app, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("File Path: %s" % tempdir)
    return tempdir

#################################################################################################   

# def read_file():
#     global content
#     global file_path

#     filename = askopenfilename()
#     infile = open(filename, 'r')
#     content = infile.read()
#     file_path = os.path.dirname(filename)
#     return content

#################################################################################################

def downloadvid():
    dlpath = search_for_folder_path()
    ydl_opts = {}
    os.chdir(dlpath)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        URL_info = URL.get()
        ydl.download([URL_info])

#################################################################################################

def vid_to_aud():
    mp4_file = mp4.get()
    mp3_file = save_to_folder_path()
    print(mp4_file)

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()

#################################################################################################

def aud_to_txt():
    mp3_file = mp3.get()
    text_file = save_to_folder_path2()


    url = 'https://api.fpt.ai/hmi/asr/general'
    payload = open(mp3_file, 'rb').read()
    headers = {
        'api-key': '6Q3TAvoFEdPYnVcviCiEZZIM6XTIA3CK'
    }

    response = requests.post(url=url, data=payload, headers=headers)

    print(response.json())

    data = response.json() 
    with open(text_file, 'w') as outfile:
        json.dump(data, outfile) 

#################################################################################################

def open_read_json_file():
    top = Toplevel()
    top.title("subtitle file")
    textArea = Text(top)

    scrollbar = tk.Scrollbar(top, command=textArea.yview)
    scrollbar.grid(row=0, column=1, sticky='nsew')

    textArea['yscrollcommand'] = scrollbar.set
    
    subtitle_info = subtitle.get()
    with open(subtitle_info, "r") as json_file:
        textArea.insert(END,json.load(json_file) )

    textArea.grid(row=0, column=0)
    textArea.config(state=DISABLED)
    
#################################################################################################

app = Tk()

app.geometry("540x300")
app.title("Python add subtitle video")
Label(text="Python convert video to text Forms",fg="black",bg="grey",width="500",height="2",font="10").pack()

Label(text="Enter URL :").place(x=15,y=70)
Label(text="mp4 file :").place(x=15,y=125)
Label(text="mp3 file :").place(x=15,y=180)
Label(text="subtitle file :").place(x=15,y=230)

URL = StringVar()
mp4 = StringVar()
mp3 = StringVar()
subtitle = StringVar()

Entry(textvariable=URL,width="45").place(x=15,y=100)
Entry(textvariable=mp4,width="45").place(x=15,y=150)
Entry(textvariable=mp3,width="45").place(x=15,y=200)
Entry(textvariable=subtitle,width="45").place(x=15,y=250)

#Button(app,text="browser",command=open_file,width="10",bg="grey").place(x=295,y=95)
Button(app,text="Download",command=downloadvid,width="15",height="2",bg="grey").place(x=400,y=90)

Button(app,text="browser",command=browsermp4,width="10",bg="white").place(x=295,y=145)
Button(app,text="convert to mp3",command=vid_to_aud,width="15",height="2",bg="grey").place(x=400,y=140)

Button(app,text="browser",command=browsermp3,width="10",bg="white").place(x=295,y=195)
Button(app,text="convert to text",command=aud_to_txt,width="15",height="2",bg="grey").place(x=400,y=190)

Button(app,text="browser",command=browsertxt,width="10",bg="white").place(x=295,y=245)
Button(app,text="open text file",command=open_read_json_file,width="15",height="2",bg="grey").place(x=400,y=240)

mainloop()

#################################################################################################
    