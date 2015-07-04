"""
Creates a test GUI that demonstrates knowledge of TKinter tools.
"""
from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.createwidgets()
        
    def createwidgets(self):
        self.grid(sticky=ALL)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        frame_1 = Frame(self, bg="blue")
        frame_1.grid(row=0,column=0,columnspan=2, sticky=ALL)
        frame_2 = Frame(self, bg="yellow")
        frame_2.grid(row=1,column=0,columnspan=2, sticky=ALL)
        frame_3 = Frame(self, bg="green")
        frame_3.grid(row=0,column=2, rowspan=2, columnspan=3, sticky=ALL)
        flst = [frame_1,frame_2,frame_3]
        for frame in flst:
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0,weight=1)
        Label(frame_1,text="Frame 1", bg="blue").grid(row=0,column=0, columnspan=2, sticky=ALL)
        Label(frame_2,text="Frame 2", bg="yellow").grid(row=0,column=0,columnspan=2, sticky=ALL)
        Label(frame_3,text="Frame 3", bg="green").grid(row=0,column=0, rowspan=2, columnspan=3, sticky=ALL)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=3, column=c, sticky=E+W)



root = Tk()
app = Application(master=root)
app.mainloop()
