import time
import calendar
try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

class Application(Frame):

    def createTime(self):
        self.Time = Label(self.top_right, text=time.asctime(self.localtime))
        self.Time.pack(side='right')

    def createCal(self):
        self.Cal = Text(self.bottom_right,height=8,width=0,background='gray')
        self.Cal.insert(INSERT, calendar.month(self.localtime[0], self.localtime[1]))
        self.Cal.pack(side='right',fill='both',expand=True)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.localtime = time.localtime(time.time())

        self.main_container = Frame(master, background='bisque')
        self.main_container.pack(side='top',fill='both',expand=True)
        master.minsize(width=500,height=500)

        self.top_frame = Frame(self.main_container,background='green')
        self.top_frame.pack(side='top',fill='x',expand=False)

        self.bottom_frame = Frame(self.main_container,background='yellow')
        self.bottom_frame.pack(side='bottom',fill='x',expand=False)

        self.top_left = Frame(self.top_frame, background="pink")
        self.top_left.pack(side="left", fill="x", expand=True)

        self.top_right = Frame(self.top_frame, background="blue")
        self.top_right.pack(side="right", fill="x", expand=True)

        self.bottom_right = Frame(self.bottom_frame,background='red')
        self.bottom_right.pack(side='right',fill='x',expand=True)

        self.bottom_left = Frame(self.bottom_frame,background='orange')
        self.bottom_left.pack(side='left',fill='x',expand=True)

        self.createTime()
        self.createCal()

        self.top_left_label = Label(self.top_left, text="Top Left")
        self.top_left_label.pack(side="left")

        #self.top_right_label = Label(self.top_right, text="Top Right")
        #self.top_right_label.pack(side="right")

        #self.bottom_right_label = Label(self.bottom_right,text='Bottom Right')
        #self.bottom_right_label.pack(side='right')

        self.bottom_left_label = Label(self.bottom_left,text='Bottom Left')
        self.bottom_left_label.pack(side='left')

def tick(app):
    time2 = time.localtime(time.time())
    if time2 != app.localtime:
        app.localtime = time2
        app.Time.config(text=time.asctime(app.localtime))
    app.Time.after(200,tick(app))

root = Tk()
root.title('Test.py')
app = Application(root)
#tick(app)

app.mainloop()
