from tkinter import *

counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            display=str(counter//60).zfill(2)+":"+str(counter%60).zfill(2)
            label['text']=display
            label.after(1000, count)
            counter += 1
    count()

def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=0
    if running==False:
        reset['state']='disabled'
        label['text']='00:00'

root = Tk()
root.title("Stopwatch")

label = Label(root, text="00:00", fg="black", font="Verdana 30 bold")
label.pack()
f=Frame(root)
start = Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Button(f, text='Reset', width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor="center", pady=50)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")

root.mainloop()
