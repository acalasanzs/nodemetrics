""" 
Python System Monitor Sender via GUI or CLI

made with love by Albert Calasanz

TODO:
    - MAKE 'DO' FUNCTION FOR THE MAIN LOOP OF TK WINDOW
    - MAKE 'SEND' FUNCTION FOR THE DATA SEND PROCESS
"""
colors = {
    "bg-light": '#130f40',
    "bg": '#6c5ce7',
    "gray": '#2d3436',
    "yellow": '#dff9fb',
    "green": '#c7ecee',
    "red": '#f6e58d',
    "blue": '#7ed6df'
}
from flask import Flask, request
from time import sleep
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from monitor import statistics, update, interval, gpu_s

from screeninfo import get_monitors

fwidth, fheight = 800, 350

server = 'localhost'

first_monitor = get_monitors()[0]

width = first_monitor.width
height = first_monitor.height

ms_interval = int(interval*1000)
class Interface():
    def __init__(self, gui = True):
        if gui:
            """ GUI """
            self.root = tk.Tk()
            self.root.title("Nodemetrics Client v0.1.0")
            self.root.protocol("WM_DELETE_WINDOW", self.destroy)
            #Es crea un Tk
            self.frame = tk.Frame(self.root, width=fwidth,height=fheight, bg=colors['bg-light'])
            self.root.geometry(f'{fwidth}x{fheight}+{int(width/2-400)}+{int(height/2-175)}')
            self.frame.grid()
            self.frame.pack_propagate(False)
            self.widgets()
            self.update_labels()
            
            #Prevent resize
            self.root.resizable(width=False, height=False)
            self.root.mainloop()
        else:
            """ CLI """
            self.gpu = False
            while True:
                self.update_cli()
                sleep(interval*4)
            pass
    def widgets(self):
        #GRAPHICAL USER INTERFACE
        self.server = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['red'],
                text='server url',
                font=('Roboto',16))
        self.server.pack()
        self.cpu = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['yellow'],
                text='CPU USAGE',
                font=('Roboto',27))
        self.cpu.pack(pady=20)

        self.mem = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['green'],
                text='MEMORY USAGE',
                font=('Roboto',27))
        self.mem.pack(pady=20)

        self.disk = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['red'],
                text='DISK USAGE',
                font=('Roboto',27))
        self.disk.pack(pady=20)

        self.gpu = tk.Label(self.frame,
                bg=colors['bg-light'], 
                fg=colors['blue'],
                text='NO GPU FOUND',
                font=('Roboto',27))
        self.gpu.pack()
    def update_labels(self):
        update()
        self.server.configure(text=server)
        self.cpu.configure(text=f'{statistics["cpu"]["count"]} CPU: {statistics["cpu"]["percent"]}%')
        self.mem.configure(text=f'RAM: {statistics["mem"]["percent"]}%')
        self.disk.configure(text=f"""'{statistics["disk"]["partition"]}': {statistics["disk"]["percent"]}%""")
        if gpu_s > 0:
            self.gpu.configure(text=f'GPU 0: {statistics["gpu"]["percent"]}')
        self.root.after(ms_interval, self.update_labels)
    def update_cli(self):
        update()
        self.server = server
        self.cpu = f'{statistics["cpu"]["count"]} CPU: {statistics["cpu"]["percent"]}%'
        self.mem = f'RAM: {statistics["mem"]["percent"]}%'
        self.disk = f"""'{statistics["disk"]["partition"]}': {statistics["disk"]["percent"]}%"""
        if gpu_s > 0:
            self.gpu = f'GPU 0: {statistics["gpu"]["percent"]}'
        print(f'Server url: {self.server}\n{self.cpu}\n{self.mem}\n{self.disk}\n{self.gpu if self.gpu else "NO GPU"}\n')
    def destroy(self):
        """ ***STOP SENDING DATA*** """
        print("nope")
        self.root.destroy()


f = open("server.txt",'r',encoding = 'utf-8')
f = f.readline()
server = f if len(f) > 0 else server
the_app = Interface()

