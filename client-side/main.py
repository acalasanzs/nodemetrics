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
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

from screeninfo import get_monitors

first_monitor = get_monitors()[0]

width = first_monitor.width
height = first_monitor.height

class Interface():
    def __init__(self, gui = True):
        if gui:
            self.root = tk.Tk()
            #Es crea un Tk
            self.frame = tk.Frame(self.root, width='800',height='350', background= colors['bg'])
            self.root.geometry(f'800x350+{int(width/2-400)}+{int(height/2-175)}')
            self.root.resizable(width=False, height=False)
            self.frame.grid()
            self.widgets()
            #Prevent resize

            self.root.mainloop()
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
    def destroy(self):
        """ ***STOP SENDING DATA*** """
        self.root.destroy()


the_app = Interface()

