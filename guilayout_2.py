"""
Creates a gui that opens and displays the content of a file,
then gives you the option to change the color of the text.
as well as provides to frames that track where the user clicks within them.
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
        self.entry = Entry(frame_3)
        self.entry.grid(row=0,column=0, columnspan=3, sticky=ALL)
        self.text = Text(frame_3)
        self.text.grid(row=1,column=0, columnspan=3, sticky=ALL)
        frame_1.bind("<1>", self.handler1)
        frame_2.bind("<1>", self.handler2)
        btnlst = []
        colors = ['red','blue','green','black','open']
        for _color in colors:
            button = Button(self, width=25, text="{0}".format(_color),
                            command=self.bhandler(color=_color))
            btnlst.append(button)
        for i in btnlst:
            self.columnconfigure(btnlst.index(i), weight=1)
            i.grid(row=3, column=btnlst.index(i), sticky=E+W)
    def bhandler(self, color):
        if color == 'open': #This button doesn't change the text color
            def dothis():
                a = self.entry.get()
                try:
                    f = open(a)
                    r = f.read()
                    f.close()
                    self.text.delete(1.0,9999999999.0)
                    self.text.insert(1.0, r)
                except FileNotFoundError:
                    self.text.delete(1.0,9999999999.0)
                    self.text.insert(1.0, "Sorry, we couldn't find that file")
            return dothis
        def dothat():
            _color = color
            self.text.configure(fg = _color)
        return dothat

    def handler1(self, event):
        print("Frame 1", event.x, event.y)
        return "break"
    
    def handler2(self, event):
        print("Frame 2", event.x, event.y)
        return "break"



root = Tk()
app = Application(master=root)
app.mainloop()
