from tkinter import *

class Text_Settings(object):
    def __init__(self,master):
        tx = self.tx = Toplevel(master,bd=15)
        tx.title("Text Settings")
        pad_x = 10
        pad_y = 10

        self.okay_button = Button(tx,text = "OKAY", command = self.cleanup)
        self.okay_button.pack(anchor=S,side = BOTTOM,pady=pad_y)

    def cleanup(self):
        self.tx.destroy()
