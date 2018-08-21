from tkinter import *

class popupWindow(object):
    def __init__(self,master,mode):
        top = self.top = Toplevel(master,bd=15)
        top.title("Coordinates")
        padding_x = 10
        padding_y = 2
        self.mode = str(mode.get())

        self.offset_m = Message(top,text = 'Input Offset:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.offset_entry = Entry(top)
        self.offset_entry.pack(anchor = CENTER)

        self.x1_m = Message(top,text= 'Input X Coordinate Row 1:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.x1_entry = Entry(top)
        self.x1_entry.pack(anchor = CENTER)

        self.y1_m = Message(top,text= 'Input Y Coordinate Row 1:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.y1_entry = Entry(top)
        self.y1_entry.pack(anchor = CENTER)

        self.x2_m = Message(top,text= 'Input X Coordinate Row 2:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.x2_entry = Entry(top)
        self.x2_entry.pack(anchor = CENTER)
        self.x2_entry.config(state = 'disabled')

        self.y2_m = Message(top,text= 'Input Y Coordinate Row 2:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.y2_entry = Entry(top)
        self.y2_entry.pack(anchor = CENTER)
        self.y2_entry.config(state = 'disabled')

        self.width_m = Message(top,text = 'mtext Width:',justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.width_entry = Entry(top)
        self.width_entry.pack(anchor = CENTER)
        self.width_entry.config(state = 'disabled')

        self.height_m = Message(top,text= 'mtext Height:',justify = LEFT).pack(anchor = CENTER,pady=padding_y)
        self.height_entry = Entry(top)
        self.height_entry.pack(anchor = CENTER)
        self.height_entry.config(state = 'disabled')

        self.okay_button = Button(top,text = "OKAY", command = self.cleanup)
        self.okay_button.pack(anchor=S,side = BOTTOM,pady=padding_y+5)
        self.err = StringVar()
        self.error_bar = Message(top,textvariable = self.err,aspect=800).pack(anchor = S,pady=(15,5))
        self.enable_entry()
        top.bind('<Return>', lambda x: self.okay_button.invoke())

    def cleanup(self):
        try:
            offset = float(self.offset_entry.get())
            xc1 = int(self.x1_entry.get())
            yc1 = int(self.y1_entry.get())
            if self.mode == '4':
                xc2 = int(self.x2_entry.get())
                yc2 = int(self.y2_entry.get())
            else:
                xc2 = 0
                yc2 = 0
            if self.mode == '2':
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
            else:
                width = 0
                height = 0
        except ValueError:
            self.err.set("Must Enter Some Values")
            return

        self.coordinates = [offset,xc1,yc1,xc2,yc2,width,height]
        print(self.coordinates)
        self.top.destroy()

    def enable_entry(self):
        if(self.mode == '2'):
            self.width_entry.config(state = 'normal')
            self.height_entry.config(state = 'normal')
        if(self.mode == '4'):
            self.x2_entry.config(state='normal')
            self.y2_entry.config(state='normal')
