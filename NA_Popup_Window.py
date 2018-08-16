from tkinter import *

class popupWindow(object):
    def __init__(self,master,var):
        top = self.top = Toplevel(master,bd=15)
        self.top.title("Coordinates")
        padding_x = 10
        padding_y = 2
        self.var = var
        self.offset_text = Message(top,text = 'Input Offset:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.offset_entry = Entry(top)
        self.offset_entry.pack(anchor = CENTER)
        self.valuestex_tx1 = Message(top,text= 'Input X Coordinate Row 1:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.xcoordentry_x1 = Entry(top)
        self.xcoordentry_x1.pack(anchor = CENTER)
        self.valuestext_y1 = Message(top,text= 'Input Y Coordinate Row 1:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.ycoordentry_y1 = Entry(top)
        self.ycoordentry_y1.pack(anchor = CENTER)
        self.valuestex_tx2 = Message(top,text= 'Input X Coordinate Row 2:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.xcoordentry_x2 = Entry(top)
        self.xcoordentry_x2.pack(anchor = CENTER)
        self.valuestext_y2 = Message(top,text= 'Input Y Coordinate Row 2:',aspect=500,justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.ycoordentry_y2 = Entry(top)
        self.ycoordentry_y2.pack(anchor = CENTER)
        self.boxx_text = Message(top,text = 'mtext Width:',justify=LEFT).pack(anchor = CENTER,pady=padding_y)
        self.box_x = Entry(top)
        self.box_x.pack(anchor = CENTER)
        self.box_x.config(state = 'disabled')
        self.boxy_text = Message(top,text= 'mtext Height:',justify = LEFT).pack(anchor = CENTER,pady=padding_y)
        self.box_y = Entry(top)
        self.box_y.pack(anchor = CENTER)
        self.box_y.config(state = 'disabled')
        self.exit_button = Button(top,text = "OKAY", command = self.cleanup)
        self.exit_button.pack(anchor=S,side = BOTTOM,pady=padding_y+20)
        self.disable_entry()
        self.top.bind('<Return>', lambda x: self.exit_button.invoke())

    def cleanup(self):
        self.offset = self.offset_entry.get()
        self.xc1 = self.xcoordentry_x1.get()
        self.yc1 = self.ycoordentry_y1.get()
        self.xc2 = self.xcoordentry_x2.get()
        self.yc2 = self.ycoordentry_y2.get()
        self.boxx = self.box_x.get()
        self.boxy = self.box_y.get()
        self.top.destroy()

#sequentiall
#tagnames
#single
#double
#sametext

    def disable_entry(self):
        if(self.var.get() == '2'):
            self.xcoordentry_x2.config(state='disabled')
            self.ycoordentry_y2.config(state='disabled')
            self.box_x.config(state = 'normal')
            self.box_y.config(state = 'normal')
        if((self.var.get() == '3') or (self.var.get() == '1') or (self.var.get() == '5')):
            self.xcoordentry_x2.config(state='disabled')
            self.ycoordentry_y2.config(state='disabled')
