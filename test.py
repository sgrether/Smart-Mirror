from tkinter import *
import time
import calendar

class Application(Frame):

    def createWidget(self):
        self.Time = Label(self)
        localtime = time.localtime(time.time())
        self.Time['text'] = time.asctime( localtime )
        self.Time.grid(row=0)

        var = StringVar()
        self.Cal = Message(self, textvariable=var, anchor=NE)
        var.set(calendar.month(localtime[0], localtime[1]))
        self.Cal.grid()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidget()

root = Tk()
app = Application(root)
app.master.minsize(640, 480)
#localtime = time.asctime( time.localtime(time.time()) )
#localtime = time.localtime(time.time())
#print(localtime[0])

app.mainloop()
