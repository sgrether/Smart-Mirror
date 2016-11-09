from Tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Map of Seaside")
img = ImageTk.PhotoImage(Image.open("Seaside.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
