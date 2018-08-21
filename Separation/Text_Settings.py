from tkinter import *

class Text_Settings(object):
    def __init__(self,master):
        tx = self.tx = Toplevel(master,bd=15)
        tx.title("Text Settings")
        pad_x = 5
        pad_y = 5

        self.size_m = Message(tx,text = 'Input Text Size:',aspect = 500, justify = LEFT).pack(anchor = CENTER)
        self.size_e = Entry(tx)
        self.size_e.pack(anchor=CENTER)

        self.okay_button = Button(tx,text = "OKAY", command = self.cleanup)
        self.okay_button.pack(anchor=S,side = BOTTOM,pady=pad_y)

    def cleanup(self):
        text_size = self.size_e.get()
        self.settings = [text_size]
        self.tx.destroy()
