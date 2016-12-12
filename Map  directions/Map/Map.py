#Abstract: Map.py  uses tkinter to display an image of the Map of Seaside downloaded from
#Open Street Maps.
#Author: Michael Royal
#Date:12/11/16
from Tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Map of Seaside")
img = ImageTk.PhotoImage(Image.open("Seaside.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
