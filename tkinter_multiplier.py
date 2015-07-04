from tkinter import *

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        top_frame = Frame(self)
        self.entry1 = Entry(top_frame)
        self.entry1.pack(side=LEFT)
        self.entry2 = Entry(top_frame)
        self.entry2.pack(side=LEFT)
        top_frame.pack()
        bottom_frame = Frame()
        self.resultlabel = Label(bottom_frame,text='Product:')
        self.resultlabel.pack()
        self.button = Button(bottom_frame,text='Multiply',command=self.handle)
        self.button.pack()
        bottom_frame.pack()
    
    def handle(self):
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        try:
            entry1 = float(entry1)
        except ValueError:
            entry1 = False
        try:
            entry2 = float(entry2)
        except ValueError:
            entry2 = False
        if entry1 and entry2:
            product = entry1 * entry2
        else:
            product = '***ERROR***'
        self.resultlabel.config(text='Product:{0}'.format(product))
    
root = Tk()
app = Application(master=root)
app.mainloop()
