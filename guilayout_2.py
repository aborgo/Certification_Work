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
        self.redb = Button(self, width=25, text="{0}".format('red'), command=self.bhandler1)
        self.blueb = Button(self, width=25, text="{0}".format('blue'), command=self.bhandler2)
        self.greenb = Button(self, width=25, text="{0}".format('green'), command=self.bhandler3)
        self.blackb = Button(self, width=25, text="{0}".format('black'), command=self.bhandler4)
        self.openb = Button(self, width=25, text="{0}".format('open'), command=self.bhandler5)
        btnlst = [self.redb, self.blueb, self.greenb, self.blackb, self.openb]
        for i in btnlst:
            self.columnconfigure(btnlst.index(i), weight=1)
            i.grid(row=3, column=btnlst.index(i), sticky=E+W)
            
    def bhandler1(self):
        self.text.configure(fg = "red")
    
    def bhandler2(self):
        self.text.configure(fg = "blue")
    
    def bhandler3(self):
        self.text.configure(fg = "green")
    
    def bhandler4(self):
        self.text.configure(fg = "black")
    
    def bhandler5(self):
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

    def handler1(self, event):
        print("Frame 1", event.x, event.y)
        return "break"
    
    def handler2(self, event):
        print("Frame 2", event.x, event.y)
        return "break"



root = Tk()
app = Application(master=root)
app.mainloop()
