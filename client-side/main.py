""" 
Python System Monitor Sender via GUI or CLI

made with love by Albert Calasanz

TODO:
    - MAKE 'DO' FUNCTION FOR THE MAIN LOOP OF TK WINDOW
    - MAKE 'SEND' FUNCTION FOR THE DATA SEND PROCESS
"""
colors = {
    "bg-light": '#a29bfe',
    "bg": '#6c5ce7',
    "gray": '#dfe6e9'
}
from textwrap import fill
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from turtle import bgcolor, color
from monitor import statistics, update, interval

from screeninfo import get_monitors

ms_interval = int(interval*1000)

fwidth, fheight = 800, 350

first_monitor = get_monitors()[0]

width = first_monitor.width
height = first_monitor.height

class CircularProgressbar(object):
    def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=0, full_extent=360):
        self.custom_font = tkFont.Font(family="Arial", size=16, weight='bold')
        self.canvas = canvas
        self.x0, self.y0, self.x1, self.y1 = x0+width, y0+width, x1-width, y1-width
        self.tx, self.ty = (x1-x0) / 2, (y1-y0) / 2
        self.width = width
        self.start_ang, self.full_extent = start_ang, full_extent
        # draw static bar outline
        w2 = width / 2
        self.oval_id1 = self.canvas.create_oval(self.x0-w2, self.y0-w2,
                                                self.x1+w2, self.y1+w2, outline=colors['gray'])
        self.oval_id2 = self.canvas.create_oval(self.x0+w2, self.y0+w2,
                                                self.x1-w2, self.y1-w2, outline=colors['gray'])
        self.running = False

    def start(self, interval=100):
        self.interval = interval
        self.increment = self.full_extent / interval
        self.extent = 60
        self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                             start=self.start_ang, extent=self.extent,
                                             width=self.width, style="arc")
        percent = '0%'
        self.label_id = self.canvas.create_text(self.tx, self.ty, text=percent,
                                                font=self.custom_font, fill= colors['gray'])
        self.running = True
        self.canvas.after(interval, self.step, self.increment)

    def step(self, delta):
        """Increment extent and update arc and label displaying how much completed."""
        if self.running:
            self.cur_extent = (self.cur_extent + delta) % 360
            self.canvas.itemconfigure(self.arc_id, extent=self.cur_extent)
            percent = '{:.0f}%'.format(round(float(self.cur_extent) / self.full_extent * 100))
            self.canvas.itemconfigure(self.label_id, text=percent)

        self.after_id = self.canvas.after(self.interval, self.step, delta)
        update()

    def toggle_pause(self):
        self.running = not self.running

class Interface():
    def __init__(self, gui = True):
        if gui:
            """ GUI """
            self.root = tk.Tk()
            self.root.title("Nodemetrics Client v0.1.0")
            #Es crea un Tk
            self.frame = tk.Frame(self.root, width=fwidth,height=fheight)
            self.root.geometry(f'{fwidth}x{fheight}+{int(width/2-400)}+{int(height/2-175)}')
            self.frame.grid()
            self.canvas = tk.Canvas(self.frame, width=fwidth, height=fheight, bg= colors['bg'])
            self.canvas.grid(row=0, column=0, columnspan=2)
            self.widgets()
            
            #Prevent resize
            self.root.resizable(width=False, height=False)
            self.root.mainloop()
        else:
            """ CLI """
            pass
    def widgets(self):
        #GRAPHICAL USER INTERFACE
            exit = tk.Button(self.root, 
                    bg='#ffffff',
                    fg='#1abc9c',
                    relief='flat',
                    text='Tancar',
                    width=8,
                    font=('Roboto',18),
                    command=self.destroy)
            self.progressbar = CircularProgressbar(self.canvas, 0, 0, 200, 200, 20)
            self.progressbar.start()
    def update_labels(self):
        self.root.after(ms_interval, self.update_labels)
    def destroy(self):
        """ ***STOP SENDING DATA*** """
        self.root.destroy()


the_app = Interface()

