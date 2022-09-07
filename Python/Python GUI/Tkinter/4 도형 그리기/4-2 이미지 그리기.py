from tkinter import *
from PIL import ImageTk, Image

mainFrame = Tk()
sketchbook = Canvas(mainFrame, width=350, height=500)
sketchbook.pack(side="left")
photo = PhotoImage(file="dog.png")
sketchbook.create_image(10, 10, image=photo, anchor=NW)

sketchbook2 = Canvas(mainFrame, width=860, height=500)
sketchbook2.pack(side="right")
PIL_image = ImageTk.PhotoImage(Image.open("rabbit.png"))
sketchbook2.create_image(10, 10, image=PIL_image, anchor=NW)

mainFrame.mainloop()
