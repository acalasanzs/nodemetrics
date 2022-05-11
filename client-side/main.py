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
    "gray": '#2d3436',
    "yellow": '#ffeaa7'
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


class Interface():
    def __init__(self, gui = True):
        if gui:
            """ GUI """
            self.root = tk.Tk()
            self.root.title("Nodemetrics Client v0.1.0")
            #Es crea un Tk
            self.frame = tk.Frame(self.root, width=fwidth,height=fheight, bg=colors['bg-light'])
            self.root.geometry(f'{fwidth}x{fheight}+{int(width/2-400)}+{int(height/2-175)}')
            self.frame.grid()
            self.frame.pack_propagate(False)
            self.widgets()
            
            #Prevent resize
            self.root.resizable(width=False, height=False)
            self.root.mainloop()
        else:
            """ CLI """
            pass
    def widgets(self):
        #GRAPHICAL USER INTERFACE
        cpu = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['yellow'],
                text='CPU USAGE',
                font=('Roboto',27))
        cpu.pack(pady=20)

        mem = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['yellow'],
                text='CPU USAGE',
                font=('Roboto',27))
        mem.pack(pady=20)

        disk = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['yellow'],
                text='CPU USAGE',
                font=('Roboto',27))
        disk.pack(pady=20)

        gpu = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['yellow'],
                text='CPU USAGE',
                font=('Roboto',27))
        gpu.pack(pady=20)
    def update_labels(self):
        self.root.after(ms_interval, self.update_labels)
    def destroy(self):
        """ ***STOP SENDING DATA*** """
        self.root.destroy()


the_app = Interface()

