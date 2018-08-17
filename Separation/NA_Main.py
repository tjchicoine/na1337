from tkinter import *
import time
from Functions import pypoweredfunctions as f

class Main_Window:
    def __init__(self,master):
        padding_x = 5
        padding_y = 5
        self.master = master

        self.master.title("N.A 1.337")
        self.welcomemessage = Message(master,text = "NANOCAD AUTOFILLER 1.337",aspect=200,justify = CENTER).pack()

        #-------------------------Radiobutton Introduction---------------------#
        self.mode_str = StringVar()
        self.mode_str.set('1')

        MODES = [('Sequential','1'),
        ('Tag Names','2'),
        ('1 Row Same Text','3'),
        ('2 Row Input Text','4'),
        ('First Value + Suffix','5')]

        for text,mode in MODES:
            self.Mode_Selection = Radiobutton(master,text = text,variable = self.mode_str,value = mode,command= self.mode_select ,justify=LEFT).pack(anchor=W,padx=(5,5))

        #-------------------------Option Menu For Direction--------------------#
        self.direction_msg = Message(master,text = 'Select Direction of Input:',aspect=200,justify= CENTER)
        self.direction_msg.pack(anchor = CENTER,pady=(15,0))
        DIRECTION = ['DOWN','UP']
        direction_mode = self.direction = StringVar()
        self.direction.set(DIRECTION[0])
        self.direction_menu = OptionMenu(master,direction_mode,*DIRECTION)
        self.direction_menu.pack()

        #----------------OPEN POPUP TO SET COORDINATES-------------------------#
        self.coordinate_button = Button(master,text = 'Initial Coordinates',command = self.popup)
        self.coordinate_button.pack(anchor = CENTER,padx=padding_x,pady=padding_y)

        #--------------------------Select Text File----------------------------#
        self.filechooserbutton = Button(master,text = "Text File",command = self.get_filename)
        self.filechooserbutton.pack(anchor = CENTER,padx=padding_x,pady=padding_y)
        self.filechooserbutton.config(state='disabled')

        self.display_path_string = StringVar()
        self.display_path_string.set('Please choose a text file')
        self.display_path_Label = Label(master,textvariable = self.display_path_string,bg = '#fff').pack(anchor = CENTER,padx=padding_x)

        #--------------------------Prefixes------------------------------------#
        self.line = Message(master,text = '============',aspect = 500, justify = CENTER).pack()
        self.row1text_message = Message(master,text = 'Row 1 Prefix',aspect=300,justify = CENTER).pack()
        self.row1text = Entry(master)
        self.row1text.pack()
        self.row1text.config(state='disabled')
        self.row2text_message = Message(master,text = 'Row 2 Prefix',aspect=200,justify = CENTER).pack()
        self.row2text = Entry(master)
        self.row2text.pack()
        self.row2text.config(state='disabled')

        #---------------------Sequential Number -------------------------------#
        self.sequence1a_message = Message(master,text = 'Row 1: Lowest -> Highest',aspect=900).pack(pady=padding_y)
        self.sequence1a = Entry(master)
        self.sequence1a.pack()
        self.sequence1b = Entry(master)
        self.sequence1b.pack()
        self.sequence2_message = Message(master,text = 'Row 2: Lowest -> Highest',aspect=800).pack(pady=padding_y)
        self.sequence2a = Entry(master)
        self.sequence2a.pack(padx=padding_x+20)
        self.sequence2a.config(state='disabled')
        self.sequence2b = Entry(master)
        self.sequence2b.pack(padx=padding_x+20)
        self.sequence2b.config(state='disabled')

        self.display_error_string = StringVar()
        self.display_error = Label(master,textvariable=self.display_error_string).pack(anchor = CENTER,padx = padding_x)

        self.start_button = Button(master,text = "Start",command = self.start_button_onclick).pack(pady=(5,5), padx=padding_x, fill = X)
        self.exit_button = Button(master,text = "Quit", command = master.destroy).pack(side = BOTTOM,pady=(5,5),padx = padding_x,fill = X)

        #---------------------Mode Selection----------------------#

    def mode_select(self):

        #SEQUENTIAL
        if self.mode_str.get() == '1':
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')
            self.row1text.config(state='disabled')
            self.row2text.config(state='disabled')
            self.sequence2a.config(state='disabled')
            self.sequence2b.config(state='disabled')

        #TAGNAMES
        if self.mode_str.get() == '2':
            self.filechooserbutton.config(state='normal')
            self.disable_all()
        else: self.filechooserbutton.config(state='disabled')

        #SAMETEXT1
        if self.mode_str.get() == '3':
            self.row1text.config(state='normal')
            self.row2text.config(state='disabled')
            self.sequence2a.config(state='normal')
            self.sequence2b.config(state='normal')
            self.sequence1a.config(state='disabled')
            self.sequence1b.config(state='disabled')

        #SAMETEXT2
        if self.mode_str.get() == '4':
            self.row1text.config(state='normal')
            self.row1text.config(state='normal')
            self.sequence2a.config(state='normal')
            self.sequence2b.config(state='normal')
            self.sequence1a.config(state='disabled')
            self.sequence1b.config(state='disabled')

        #For sametext + a Suffix
        if self.mode_str.get() == '5':
            self.disable_all()
            self.row1text.config(state='normal')
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')

    def disable_all(self):
            self.row1text.config(state='disabled')
            self.row2text.config(state='disabled')
            self.sequence1a.config(state='disabled')
            self.sequence1b.config(state='disabled')
            self.sequence2a.config(state='disabled')
            self.sequence2b.config(state='disabled')

    def get_filename(self):
        from tkinter import filedialog
        import os
        path = filedialog.askopenfilename(initialdir = "C:/Users/tyler/Desktop/Scripts",title = "Select File", filetypes = (("text files","*.txt"),("all files","*.*")))
        path_string = os.path.join(path)
        if(len(path_string)>0):
            self.display_path_string.set(path_string)
        print(path_string)

    #-------------------------OPEN POPUP WINDOW--------------------------------#
    def popup(self):
        w = popupWindow(master,var)
        coordinate_button['state'] = 'disabled'
        master.wait_window(w.top)
        coordinate_button['state'] = 'normal'


#===============================================================================
#---------------Start Button and stuff that happens after click----------------#
#===============================================================================
    def start_button_onclick(self):
        mode = int(self.mode_str.get())


        if (self.sequence1a.get()).isdigit() and (self.sequence1b.get()).isdigit():
            row1start = int(self.sequence1a.get())
            row1end = int(self.sequence1b.get())
            if row1end==0:
                self.display_error_string.set('Row End Cannot be 0')
        else: self.display_error_string.set('Please Set Values')

        if mode==4:
            if (self.sequence2a.get()).isdigit() and (self.sequence2b.get()).isdigit():
                row2start = int(self.sequence2a.get())
                row2end = int(self.sequence2b.get())
                if row2end==0:
                    self.display_error_string.set('Row End Cannot be 0')
            else: self.display_error_string.set('Please Set Values')

        row1prefix = self.row1text.get()
        row2prefix = self.row2text.get()

        if self.mode_str.get() != "2":
            f.start()

        #SEQUENTIAL
        if self.mode_str.get() == '1':
            f.sequential(row1start,row1end)

        #TAG NAMES
        if self.mode_str.get() == '2':
            taglist = self.list_create()
            f.different_names()

        #SINGLE ROW SAMETEXT
        if self.mode_str.get() == '3':
            f.by_row(row1start,row1end)

        #SECOND ROW SAMETEXT
        if self.mode_str.get() == '4':
            f.by_row(row1start,row1end)
            f.by_rowx2(row2start,row2end)

        #Prefix w/ incrementing numbers
        if self.mode_str.get() == '5':
            f.sequential_suffix(row1start,row1end,prefix)

    def list_create(self):
        path = display_path_string.get()
        text_file = open(path,"r")
        value_list = text_file.read().split('\n')
        text_file.close()
        return value_list



if __name__ == '__main__':
    root = Tk()
    mw = Main_Window(root)
    root.mainloop()
