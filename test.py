import time
import calendar
try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

time1 = time.localtime(time.time())

class Application(Frame):

    def createTime(self):
        self.Time = Label(self.top_right, fg='white', background='black', font=('helvetica', 15))
        self.Time.pack(side='right')

    def createCal(self):
        self.Cal = Text(self.bottom_left,height=7,width=0,background='black', fg='white')
        self.Cal.insert(INSERT, calendar.month(time1[0], time1[1]))
        self.Cal.pack(side='left',fill='both',expand=True)

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.main_container = Frame(master, background='black')
        self.main_container.pack(side='top',fill='both',expand=True)
        master.minsize(width=1000,height=500)

        self.top_frame = Frame(self.main_container, background='black')
        self.top_frame.pack(side='top',fill='x',expand=False)

        self.bottom_frame = Frame(self.main_container, background='black')
        self.bottom_frame.pack(side='bottom',fill='x',expand=False)

        self.top_left = Frame(self.top_frame, background='black')
        self.top_left.pack(side="left", fill="x", expand=True)

        self.top_right = Frame(self.top_frame, background='black')
        self.top_right.pack(side="right", fill="x", expand=True)

        self.bottom_right = Frame(self.bottom_frame, background='black')
        self.bottom_right.pack(side='right',fill='x',expand=True)

        self.bottom_left = Frame(self.bottom_frame, background='black')
        self.bottom_left.pack(side='left',fill='x',expand=True)

        self.createTime()
        self.createCal()

        self.top_left_label = Label(self.top_left, text="Top Left", fg='white', background='black')
        self.top_left_label.pack(side="left")

        #self.top_right_label = Label(self.top_right, text="Top Right")
        #self.top_right_label.pack(side="right")

        self.bottom_right_label = Label(self.bottom_right,text='Bottom Right', fg='white', background='black')
        self.bottom_right_label.pack(side='right')

        #self.bottom_left_label = Label(self.bottom_left,text='Bottom Left')
        #self.bottom_left_label.pack(side='left')

def tick():
    global time1
    time2 = time.localtime(time.time())
    if time2 != time1:
        time1 = time2
        app.Time.config(text=time.asctime(time1))
    app.Time.after(200, tick)

root = Tk()
root.title('Smart Mirror.py')
app = Application(root)
tick()
root.mainloop()
