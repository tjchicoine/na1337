from tkinter import *
import pyautogui
import time
#test 11111
class App:
    def __init__(self,master):
        padding_x = 5
        padding_y = 5
        self.master = master
        #self.master.geometry('400x1000+800+0')

        self.master.title("N.A 1.337")
        self.welcomemessage = Message(master,text = "NANOCAD AUTOFILLER 1.337",aspect=200,justify = CENTER).pack()

        #-------------------------Radiobutton Introduction---------------------#
        var = self.var = StringVar()
        self.var.set('1')
        MODES = [('Sequential','1'),
        ('Tag Names','2'),
        ('1 Row Same Text','3'),
        ('2 Row Input Text','4'),
        ('First Value + Suffix','5')]
        for text,mode in MODES:
            self.R1 = Radiobutton(master,text = text,variable = self.var,value = mode,command=self.mode_select,justify=CENTER).pack(anchor=W,padx=(50,0))

        #-------------------------Option Menu For Direction--------------------#
        self.direction_ex = Message(master,text = 'Select Direction of Input:',aspect=200,justify= CENTER)
        self.direction_ex.pack(anchor = CENTER,pady=(15,0))
        DIRECTION = ['DOWN','UP']
        var1 = self.var1 = StringVar()
        var1.set(DIRECTION[0])
        option = OptionMenu(master,var1,*DIRECTION)
        option.pack()

        #----------------OPEN POPUP TO SET COORDINATES-------------------------#
        self.coordinate_button = Button(master,text = 'Initial Coordinates',command = self.popup)
        self.coordinate_button.pack(anchor = CENTER,padx=padding_x,pady=padding_y)

        #--------------------------Select Text File----------------------------#
        self.filechooserbutton = Button(master,text = "Text File",command = self.get_filename)
        self.filechooserbutton.pack(anchor = CENTER,padx=padding_x,pady=padding_y)
        self.filechooserbutton.config(state='disabled')
        self.display_path_string = StringVar()
        self.display_path_string.set('Please choose a text file')
        self.display_path = Label(master,textvariable = self.display_path_string,bg = '#fff').pack(anchor = CENTER,padx=padding_x)

        #--------------------------TEXT TO REPEAT VALUE ENTRY------------------#
        self.line = Message(master,text = '============',aspect = 500, justify = CENTER).pack()
        self.row1text = Message(master,text = 'First Row Same Text (use as prefix)',aspect=300,justify = CENTER).pack()
        self.row_one_text = Entry(master)
        self.row_one_text.pack()
        self.row_one_text.config(state='disabled')
        self.row2text = Message(master,text = 'Second Row Same Text',aspect=200,justify = CENTER).pack()
        self.row_two_text = Entry(master)
        self.row_two_text.pack()
        self.row_two_text.config(state='disabled')

        #---------------------Sequential Number VALUE ENTRY--------------------#
        self.sequence1aexplaination = Message(master,text = 'Sequential: Enter Lowest # -> Highest #',aspect=900).pack(pady=padding_y)
        self.sequence1a = Entry(master)
        self.sequence1a.pack()
        self.sequence1b = Entry(master)
        self.sequence1b.pack()
        self.sequence2explaination = Message(master,text = 'Row 1: Enter Lowest # -> Highest #',aspect=800).pack(pady=padding_y)
        self.sequence2a = Entry(master)
        self.sequence2a.pack(padx=padding_x+20)
        self.sequence2a.config(state='disabled')
        self.sequence2b = Entry(master)
        self.sequence2b.pack(padx=padding_x+20)
        self.sequence2b.config(state='disabled')
        self.sequence3explaination = Message(master,text = 'Row 2: Enter Lowest # -> Highest #',aspect=700)
        self.sequence3explaination.pack(pady=padding_y)
        self.sequence3a = Entry(master)
        self.sequence3a.pack(padx=padding_x+20)
        self.sequence3a.config(state='disabled')
        self.sequence3b = Entry(master)
        self.sequence3b.pack(padx=padding_x+20)
        self.sequence3b.config(state='disabled')

        self.exit_button = Button(master,text = "Quit", command = master.destroy).pack(anchor=S,side = BOTTOM,pady=(5,30),padx = padding_x,fill = X)

        #---------------------START BUTTON CLICK COMMANDS----------------------#

        self.start_button = Button(master,text = "Start",command = self.start_button_onclick).pack(side = BOTTOM,pady=(30,5), padx=padding_x, fill = X)

    def mode_select(self):
        if self.var.get() == '1': #SEQUENTIAL
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')
            self.row_one_text.config(state='disabled')
            self.row_two_text.config(state='disabled')
            self.sequence2a.config(state='disabled')
            self.sequence2b.config(state='disabled')
            self.sequence3a.config(state='disabled')
            self.sequence3b.config(state='disabled')
        if self.var.get() == '2': #TAGNAMES
            self.filechooserbutton.config(state='normal')
            self.disable_all()
        else: self.filechooserbutton.config(state='disabled')
        if self.var.get() == '3': #SAMETEXT1
            self.row_one_text.config(state='normal')
            self.sequence2a.config(state='normal')
            self.sequence2b.config(state='normal')
            self.row_two_text.config(state='disabled')
            self.sequence1a.config(state='disabled')
            self.sequence1b.config(state='disabled')
            self.sequence3a.config(state='disabled')
            self.sequence3b.config(state='disabled')
        if self.var.get() == '4': #SAMETEXT2
            self.row_one_text.config(state='normal')
            self.row_two_text.config(state='normal')
            self.sequence2a.config(state='normal')
            self.sequence2b.config(state='normal')
            self.sequence3a.config(state='normal')
            self.sequence3b.config(state='normal')
            self.sequence1a.config(state='disabled')
            self.sequence1b.config(state='disabled')

        if self.var.get() == '5': #For sametext + a Suffix
            self.disable_all()
            self.row_one_text.config(state='normal')
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')

    def disable_all(self):
            self.row_one_text.config(state='disabled')
            self.row_two_text.config(state='disabled')
            self.sequence1a.config(state='disabled')
            self.sequence1b.config(state='disabled')
            self.sequence2a.config(state='disabled')
            self.sequence2b.config(state='disabled')
            self.sequence3a.config(state='disabled')
            self.sequence3b.config(state='disabled')

    def get_filename(self):
        from tkinter import filedialog
        import os
        path = filedialog.askopenfilename(initialdir = "C:/Users/tyler/Desktop/Scripts",title = "Select File", filetypes = (("text files","*.txt"),("all files","*.*")))
        path_string = os.path.join(path)
        self.display_path_string.set(path_string)
        print(path_string)

    #-------------------------OPEN POPUP WINDOW--------------------------------#
    def popup(self):
        self.w = popupWindow(self.master,self.var)
        self.coordinate_button['state'] = 'disabled'
        self.master.wait_window(self.w.top)
        self.coordinate_button['state'] = 'normal'


#===============================================================================
#---------------Start Button and stuff that happens after click----------------#
#===============================================================================
    def start_button_onclick(self):
        if self.var.get() == '1': #SEQUENTIAL
            row_1_start = self.sequence1a.get()
            row_1_end = self.sequence1b.get()
            if len(row_1_end)==0 or not row_1_end.isdigit():
                print('We have a problem')
            else:
                row_1_start = int(row_1_start)
                row_1_end = int(row_1_end)
                self.start()
                self.sequential(row_1_start,row_1_end)

        if self.var.get() == '2': #TAG NAMES
            self.start()
            self.different_names()

        if self.var.get() == '3': #SINGLE ROW SAMETEXT
            row_1_start = int(self.sequence2a.get())
            row_1_end = int(self.sequence2b.get())
            self.start()
            self.by_row(row_1_start,row_1_end)

        if self.var.get() == '4': #SECOND ROW SAMETEXT
            row_1_start = int(self.sequence2a.get())
            row_1_end = int(self.sequence2b.get())
            row_2_start = int(self.sequence3a.get())
            row_2_end = int(self.sequence3b.get())
            self.start()
            self.by_row(row_1_start,row_1_end)
            self.by_rowx2(row_2_start,row_2_end)

        if self.var.get() == '5': #Same text with suffix
            row_1_start = int(self.sequence1a.get())
            row_1_end = int(self.sequence1b.get())
            prefix = self.row_one_text.get()
            self.start()
            self.sequential_suffix(row_1_start,row_1_end,prefix)

    def list_create(self):
        path = self.display_path_string.get()
        text_file = open(path,"r")
        value_list = text_file.read().split('\n')
        text_file.close()
        return value_list

#                -------------SEQUENTIAL FUNCTION-------------
    def sequential(self,row_1_start,row_1_end):
        for x in range(row_1_start,row_1_end + 1):
            if(x==row_1_start):
                x_val = int(self.w.xc1)
                y_val = int(self.w.yc1)
            self.text_writer(x,x_val,y_val)
            if(self.var1.get() == 'DOWN'):
                y_val = y_val - int(self.w.offset)
            else:
                y_val = y_val + int(self.w.offset)
#                -------------TAG NAMES FUNCTION-------------
    def different_names(self):
        tag_list = self.list_create()
        num_tags = len(tag_list)
        for x in range(num_tags):
            if(x==0):
                x_val = int(self.w.xc1)
                y_val = int(self.w.yc1)
                xbox = int(self.w.boxx)
                ybox = int(self.w.boxy)
            passval = "{}".format(tag_list[x])
            self.tag_writer(passval,x_val,y_val,xbox,ybox)
            if(self.var1.get() == 'DOWN'):
                y_val = y_val - int(self.w.offset)
            else:
                y_val = y_val + int(self.w.offset)
#                -------------SINGLE ROW FUNCTION-------------
    def by_row(self,row_2_start,row_2_end):
        for x in range(row_2_start,row_2_end + 1):
            if(x==row_2_start):
                x_val = int(self.w.xc1)
                y_val = int(self.w.yc1)
            passval = (self.row_one_text.get() + str(x))
            self.text_writer(passval,x_val,y_val)
            if(self.var1.get() == 'DOWN'):
                y_val = y_val - int(self.w.offset)
            else:
                y_val = y_val + int(self.w.offset)
#               -------------DOUBLE ROW FUNCTION-------------
    def by_rowx2(self,row_3_start,row_3_end):
        for x in range(row_3_start,row_3_end + 1):
            if(x==row_3_start):
                x_val = int(self.w.xc2)
                y_val = int(self.w.yc2)
            passval = (self.row_two_text.get() + str(x))
            self.text_writer(passval,x_val,y_val)
            if(self.var1.get() == 'DOWN'):
                y_val = y_val - int(self.w.offset)
            else:
                y_val = y_val + int(self.w.offset)

    def sequential_suffix(self,row_1_start,row_1_end,prefix):
        for x in range(row_1_start,row_1_end + 1):
            if(x==row_1_start):
                x_val = int(self.w.xc1)
                y_val = int(self.w.yc1)
            suffix = x
            passval = '{}{}'.format(prefix,suffix)
            self.text_writer(passval,x_val,y_val)
            if(self.var1.get() == 'DOWN'):
                y_val = y_val - int(self.w.offset)
            else:
                y_val = y_val + int(self.w.offset)

#                 -------------PYAUTOGUI STUFF-------------
    def start(self):
        pyautogui.moveTo(1130,16)
        pyautogui.click()

    def text_writer(self,x,x_value,y_value):
        pyautogui.typewrite("dtext")
        pyautogui.hotkey("enter")
        pyautogui.typewrite("{},{}".format(x_value,y_value))
        pyautogui.hotkey("enter")
        pyautogui.typewrite("3") #Text size
        pyautogui.hotkey("enter")
        pyautogui.typewrite("0") #Text Rotation
        pyautogui.hotkey("enter")
        pyautogui.typewrite("{}".format(x))
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        pyautogui.keyUp('ctrl')

    def tag_writer(self,x,x_value,y_value,box_x,box_y):
        pyautogui.PAUSE = 0.25
        pyautogui.typewrite("mtext")
        pyautogui.hotkey("enter")
        pyautogui.typewrite("{},{}".format(x_value,y_value))
        pyautogui.hotkey("enter")
        pyautogui.typewrite("{},{}".format(x_value+box_x,y_value-box_y))
        pyautogui.hotkey("enter")
        pyautogui.typewrite("{}".format(x))
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        pyautogui.keyUp('ctrl')

#===============================================================================
#-----------------------PARAMETERS POPUP---------------------------------------#
#===============================================================================
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

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
