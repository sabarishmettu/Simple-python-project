import tkinter as tk
import time
import winsound

class MouseAnimation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 100
        self.y = 100
        self.size = 100
        self.color = 'red'
        self.direction = 'right'

    def draw_circle(self):
        self.canvas.create_oval(self.x-self.size, self.y-self.size, self.x+self.size, self.y+self.size, fill=self.color)

    def animate(self):
        self.canvas.delete('all')
        self.draw_circle()

        if self.direction == 'right':
            self.x += 5
            if self.x >= self.canvas.winfo_width() - self.size:
                self.direction = 'left'
        elif self.direction == 'left':
            self.x -= 5
            if self.x <= self.size:
                self.direction = 'right'

        self.canvas.after(50, self.animate)

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.mouse_animation = MouseAnimation(self.canvas)
        self.mouse_animation.animate()

        self.canvas.bind('<Button-1>', self.play_sound)
        self.canvas.bind('<Button-3>', self.play_sound)

    def play_sound(self, event):
        winsound.PlaySound('click.wav', winsound.SND_FILENAME)

root = tk.Tk()
app = App(root)
root.mainloop()
