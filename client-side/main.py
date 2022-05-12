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
from ast import arg
from time import sleep, time
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from sys import argv
from monitor import statistics, update, interval, gpu_s

from screeninfo import get_monitors

import requests
fwidth, fheight = 800, 350

server = 'localhost'

first_monitor = get_monitors()[0]

width = first_monitor.width
height = first_monitor.height

ms_interval = int(interval*1000)

f = open("server.txt",'r',encoding = 'utf-8')
ft = f.readline()
f.close()
server = ft if len(ft) > 0 else server
class Interface():
    def __init__(self, gui = True):
        self.connected = None
        self.run = True
        if gui:
            """ GUI """
            self.root = tk.Tk()
            self.root.title("Nodemetrics Client v1.0.0")
            self.root.protocol("WM_DELETE_WINDOW", self.destroy)
            #Es crea un Tk
            self.frame = tk.Frame(self.root, width=fwidth,height=fheight, bg=colors['bg-light'])
            self.root.geometry(f'{fwidth}x{fheight}+{int(width/2-400)}+{int(height/2-175)}')
            self.frame.grid()
            self.frame.pack_propagate(False)
            self.widgets()

            #Prevent resize
            self.root.resizable(width=False, height=False)

            delta = 0
            now = time()
            while self.run:
                delta += time() - now
                if delta >= ms_interval:
                    self.update_labels()
                    now = time()
                self.root.update_idletasks()
                self.root.update()
            
        else:
            """ CLI """
            self.gpu = False
            while self.run:
                self.update_cli()
                sleep(interval)
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
        global ms_interval
        if self.run:
            update()
            self.server.configure(text=f"TRYING ({server})")
            try:
                result = self.send()
                self.server.configure(text=result.content.decode('UTF-8')+ ", " + server)
                ms_interval = int(interval*1000)
            except:
                self.server.configure(text=f"SERVER NOT FOUND ({server})")
                ms_interval = int(interval*1000)*8
            self.cpu.configure(text=f'{statistics["cpu"]["count"]} CPU: {statistics["cpu"]["percent"]}%')
            self.mem.configure(text=f'RAM: {statistics["mem"]["percent"]}%')
            self.disk.configure(text=f"""'{statistics["disk"]["partition"]}': {statistics["disk"]["percent"]}%""")
            if gpu_s > 0:
                self.gpu.configure(text=f'GPU 0: {"{:.1f}".format(statistics["gpu"]["percent"])}')
    def update_cli(self):
        update()
        try:
            result = self.send()
            self.server = text=result.content.decode('UTF-8')+ ", " + server
        except:
            self.server = "(SERVER NOT FOUND) "+ server
        self.cpu = f'{statistics["cpu"]["count"]} CPU: {statistics["cpu"]["percent"]}%'
        self.mem = f'RAM: {statistics["mem"]["percent"]}%'
        self.disk = f"""'{statistics["disk"]["partition"]}': {statistics["disk"]["percent"]}%"""
        if gpu_s > 0:
            self.gpu = f'GPU 0: {"{:.1f}".format(statistics["gpu"]["percent"])}'
        print(f'Server url: {self.server}\n{self.cpu}\n{self.mem}\n{self.disk}\n{self.gpu if self.gpu else "NO GPU"}\n')
    def send(self):
        data = [statistics["cpu"]["percent"], statistics["mem"]["percent"], statistics["disk"]["percent"]]
        if gpu_s > 0:
            data.append("{:.3f}".format(statistics["gpu"]["percent"]))
        data = {'usage': data}

        res = requests.post(f'http://{server}/data', json=data)
        return res
    def destroy(self):
        """ ***STOP SENDING DATA*** """
        self.run = False
        self.root.destroy()
if len(argv) > 1:
    the_app = Interface(False if argv[1] else True)
else:
    the_app = Interface()