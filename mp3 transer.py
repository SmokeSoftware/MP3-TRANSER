import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import moviepy
import moviepy.editor
import time

MP3_TRANSER = tk.Tk() 
MP3_TRANSER.title("MP3 TRANSER")
MP3_TRANSER.minsize(400,300)
MP3_TRANSER.maxsize(400,300)


def MP4_TO_MP3():
    VİDEO_NAME = filedialog.askopenfilename()
    MUSİC_NAME = VİDEO_NAME+".mp3"
    msg = Tk()
    msg.withdraw()
    messagebox.showinfo("İMFORMATİON","TRANSLATİNG TO MP3")
    video = moviepy.editor.VideoFileClip(VİDEO_NAME)
    audio = video.audio
    audio.write_audiofile(MUSİC_NAME)
    msg = Tk()
    msg.withdraw()
    messagebox.showinfo("İMFORMATİON","THE TRANSLATİNG İS DONE\n"+str(MUSİC_NAME))
    return 0
    

TRANSER_START_İA = tk.Label(MP3_TRANSER,text = "SELECT MP4 FİLE \nTRANSLATE TO MP3",fg = "black",bg = "lime",font = "Arial 25")
TRANSER_START_İA.place(width = 400,height = 150,x = 0,y = 0)


TRANSER_START_BUTTON = tk.Button(MP3_TRANSER,text = "START",fg = "lime",bg = "black",font = "Arial 80",activebackground = "black",activeforeground = "lime",command = MP4_TO_MP3)
TRANSER_START_BUTTON.place(width = 400,height = 150,x = 0,y = 150)

MP3_TRANSER.mainloop()
