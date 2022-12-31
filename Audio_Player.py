import tkinter
import pygame

#initialize the pygame module
pygame.init()

#create a window using tkinter
window = tkinter.Tk()
window.title("Audio Player")
window.geometry("400x400")

#Create a label to show the audio file
label = tkinter.Label(window, text="Audio Player")
label.pack()

#Create a list of audio files
audio_files = ["Hanuman_Chalisa_Hanuman_Da_Damdaa.mp3","audio2.mp3","audio3.mp3"]

#Create a list of audio files to store the list of audio files
playlist = tkinter.Listbox(window,selectmode=tkinter.SINGLE)
for audio_file in audio_files:
    playlist.insert(tkinter.END, audio_file)
playlist.pack()

#Create a button to play the audio
play_btn = tkinter.Button(window, text="Play", command=lambda: play_audio())
play_btn.pack()

#Create a button to stop the audio
stop_btn = tkinter.Button(window, text="Stop", command=lambda: stop_audio())
stop_btn.pack()

#Create a function to play the audio
def play_audio():
    selected_audio = playlist.get(playlist.curselection())
    pygame.mixer.music.load(selected_audio)
    pygame.mixer.music.play()
    
#Create a function to stop the audio
def stop_audio():
    pygame.mixer.music.stop()

#run the mainloop
window.mainloop()
