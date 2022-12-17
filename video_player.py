from tkinter import *
import tkinter.filedialog
import os
import webbrowser
import pygame

#initialize pygame
pygame.init()

#set up window
window=Tk()
window.title("Video player")
window.geometry("500x400")

#create a list of supported file types
video_types=[".mp4",".avi",".wmv",".mkv",".flv"]

#create a function for opening a file
def open_file():
    file=tkinter.filedialog.askopenfilename(filetypes=[("Video files",video_types)])
    if file:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    return

#create a function for searching a file
def file_search():
    file=tkinter.filedialog.askopenfilename(filetypes=[("Video files",video_types)])
    if file:
        webbrowser.open(file)
    return

#create a frame
frame=Frame(window)
frame.pack()

#create a button to open a file
open_button=Button(frame,text="Open",command=open_file)
open_button.pack()

#create a button to search a file
search_button=Button(frame,text="Search",command=file_search)
search_button.pack()

window.mainloop()
