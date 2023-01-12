from tkinter import *
import calendar

def showCalender():
    year = int(year_field.get())
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the year")
    gui.geometry("550x600")
    cal_content = calendar.calendar(year)
    Label(gui, text=cal_content, font="Consolas 10 bold").grid(row=5, column=1, padx=20)
    gui.mainloop()

if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("200x140")
    Label(new, text="Calendar", bg='grey', font=("times", 28, "bold")).grid(row=1, column=1)
    Label(new, text="Enter year", bg='dark grey').grid(row=2, column=1)
    year_field = Entry(new)
    year_field.grid(row=3, column=1)
    Button(new, text='Show Calendar', fg='black', bg='blue', command=showCalender).grid(row=4, column=1)
    new.mainloop()
