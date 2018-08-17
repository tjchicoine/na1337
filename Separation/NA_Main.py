from tkinter import *
import time

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
            self.Mode_Selection = Radiobutton(master,text = text,variable = self.mode_str,value = mode,command= self.mode_select ,justify=CENTER).pack(anchor=W,padx=(50,0))

        #-------------------------Option Menu For Direction--------------------#
        self.direction_msg = Message(master,text = 'Select Direction of Input:',aspect=200,justify= CENTER)
        self.direction_msg.pack(anchor = CENTER,pady=(15,0))
        DIRECTION = ['DOWN','UP']
        direction_mode = self.direction = StringVar()
        self.direction.set(DIRECTION[0])
        self.direction_menu = OptionMenu(master,direction_mode,*DIRECTION)
        self.direction_menu.pack()

        #----------------OPEN POPUP TO SET COORDINATES-------------------------#
        self.coordinate_button = Button(master,text = 'Initial Coordinates',command = popup)
        self.coordinate_button.pack(anchor = CENTER,padx=padding_x,pady=padding_y)

        #--------------------------Select Text File----------------------------#
        self.filechooserbutton = Button(master,text = "Text File",command = get_filename)
        self.filechooserbutton.pack(anchor = CENTER,padx=padding_x,pady=padding_y)
        self.filechooserbutton.config(state='disabled')

        self.display_path_string = StringVar()
        self.display_path_string.set('Please choose a text file')
        self.display_path_Label = Label(master,textvariable = display_path_string,bg = '#fff').pack(anchor = CENTER,padx=padding_x)

        #--------------------------TEXT TO REPEAT VALUE ENTRY------------------#
        self.line = Message(master,text = '============',aspect = 500, justify = CENTER).pack()
        self.row1text_message = Message(master,text = 'First Row Same Text (use as prefix)',aspect=300,justify = CENTER).pack()
        self.row1text = Entry(master)
        self.row1text.pack()
        self.row1text.config(state='disabled')
        self.row2text_message = Message(master,text = 'Second Row Same Text',aspect=200,justify = CENTER).pack()
        self.row2text = Entry(master)
        self.row2text.pack()
        self.row2text.config(state='disabled')

        #---------------------Sequential Number VALUE ENTRY--------------------#
        self.sequence1a_message = Message(master,text = 'Sequential: Enter Lowest # -> Highest #',aspect=900).pack(pady=padding_y)
        self.sequence1a = Entry(master)
        self.sequence1a.pack()
        self.sequence1b = Entry(master)
        self.sequence1b.pack()
        self.sequence2_message = Message(master,text = 'Row 1: Enter Lowest # -> Highest #',aspect=800).pack(pady=padding_y)
        self.sequence2a = Entry(master)
        self.sequence2a.pack(padx=padding_x+20)
        self.sequence2a.config(state='disabled')
        self.sequence2b = Entry(master)
        self.sequence2b.pack(padx=padding_x+20)
        self.sequence2b.config(state='disabled')

        self.start_button = Button(master,text = "Start",command = start_button_onclick).pack(side = BOTTOM,pady=(30,5), padx=padding_x, fill = X)
        self.exit_button = Button(master,text = "Quit", command = master.destroy).pack(anchor=S,side = BOTTOM,pady=(5,30),padx = padding_x,fill = X)

        #---------------------Mode Selection----------------------#

    def mode_select(self):
        if var.get() == '1': #SEQUENTIAL
            sequence1a.config(state='normal')
            sequence1b.config(state='normal')
            row_one_text.config(state='disabled')
            row_two_text.config(state='disabled')
            sequence2a.config(state='disabled')
            sequence2b.config(state='disabled')
            sequence3a.config(state='disabled')
            sequence3b.config(state='disabled')
        if var.get() == '2': #TAGNAMES
            filechooserbutton.config(state='normal')
            disable_all()
        else: filechooserbutton.config(state='disabled')
        if var.get() == '3': #SAMETEXT1
            row_one_text.config(state='normal')
            sequence2a.config(state='normal')
            sequence2b.config(state='normal')
            row_two_text.config(state='disabled')
            sequence1a.config(state='disabled')
            sequence1b.config(state='disabled')
            sequence3a.config(state='disabled')
            sequence3b.config(state='disabled')
        if var.get() == '4': #SAMETEXT2
            row_one_text.config(state='normal')
            row_two_text.config(state='normal')
            sequence2a.config(state='normal')
            sequence2b.config(state='normal')
            sequence3a.config(state='normal')
            sequence3b.config(state='normal')
            sequence1a.config(state='disabled')
            sequence1b.config(state='disabled')

        if var.get() == '5': #For sametext + a Suffix
            disable_all()
            row_one_text.config(state='normal')
            sequence1a.config(state='normal')
            sequence1b.config(state='normal')

    def disable_all(self):
            row_one_text.config(state='disabled')
            row_two_text.config(state='disabled')
            sequence1a.config(state='disabled')
            sequence1b.config(state='disabled')
            sequence2a.config(state='disabled')
            sequence2b.config(state='disabled')
            sequence3a.config(state='disabled')
            sequence3b.config(state='disabled')

    def get_filename(self):
        #from tkinter import filedialog
        import os
        path = filedialog.askopenfilename(initialdir = "C:/Users/tyler/Desktop/Scripts",title = "Select File", filetypes = (("text files","*.txt"),("all files","*.*")))
        path_string = os.path.join(path)
        display_path_string.set(path_string)
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
        if var.get() == '1': #SEQUENTIAL
            row_1_start = sequence1a.get()
            row_1_end = sequence1b.get()
            if len(row_1_end)==0 or not row_1_end.isdigit():
                print('We have a problem')
            else:
                row_1_start = int(row_1_start)
                row_1_end = int(row_1_end)
                f.start()
                f.sequential(row_1_start,row_1_end)

        if var.get() == '2': #TAG NAMES
            f.start()
            f.different_names()

        if var.get() == '3': #SINGLE ROW SAMETEXT
            row_1_start = int(sequence2a.get())
            row_1_end = int(sequence2b.get())
            f.start()
            f.by_row(row_1_start,row_1_end)

        if var.get() == '4': #SECOND ROW SAMETEXT
            row_1_start = int(sequence2a.get())
            row_1_end = int(sequence2b.get())
            row_2_start = int(sequence3a.get())
            row_2_end = int(sequence3b.get())
            f.start()
            f.by_row(row_1_start,row_1_end)
            f.by_rowx2(row_2_start,row_2_end)

        if var.get() == '5': #Same text with suffix
            row_1_start = int(sequence1a.get())
            row_1_end = int(sequence1b.get())
            prefix = row_one_text.get()
            f.start()
            f.sequential_suffix(row_1_start,row_1_end,prefix)

    def list_create(self):
        path = display_path_string.get()
        text_file = open(path,"r")
        value_list = text_file.read().split('\n')
        text_file.close()
        return value_list

        settings = [*sequence1a.get(),*sequence1b.get(),*sequence2a.get(),*sequence2b.get(),*w.xc1,*w.yc1,*w.xc2,*w.yc2,*w.offset,*DIRECTION]

if __name__ == '__main__':
    root = Tk()
    mw = Main_Window(root)
    root.mainloop()
