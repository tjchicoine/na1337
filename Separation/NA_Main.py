from tkinter import *
from tkinter import ttk
import time
from Functions import pypoweredfunctions
from NA_Popup_Window import popupWindow

class Main_Window:
    def __init__(self,master):
        padding_x = 5
        padding_y = 5
        rows = 0
        self.coordinates = [2,25,25,25,25,25,25]
        self.master = master

        while rows < 50:
            master.rowconfigure(rows,weight = 1)
            master.columnconfigure(rows,weight = 1)
            rows +=1

        self.master.title("N.A 1.337")
        self.welcomemessage = Message(master,text = "NANOCAD AUTOFILLER 1.337",aspect=200,justify = CENTER).grid(column=0,columnspan=50)

        self.nb = ttk.Notebook(master)
        self.nb.grid(row =1,column =0,columnspan=50,rowspan=49,sticky='NESW')
        p1 = self.page1 = ttk.Frame(self.nb)
        self.nb.add(self.page1,text='Sequential Text')
        p2 = self.page2 = ttk.Frame(self.nb)
        self.nb.add(self.page2,text='More Complicated Stuff')

        #-------------------------Radiobutton Introduction---------------------#
        self.mode_str = StringVar()
        self.mode_str.set('1')

        MODES = [('Sequential Numbers','1'),
        ('Tag Names','2'),
        ('1 Row With Prefix','3'),
        ('2 Row With Prefix','4')]

        for text,mode in MODES:
            self.Mode_Selection = Radiobutton(p1,text = text,variable = self.mode_str,value = mode,command= self.mode_select).grid(row=int(mode),column = 0,sticky='W',padx = 5)

        #-------------------------Option Menu For Direction--------------------#
        self.s = ttk.Separator(p1,orient='horizontal')
        self.s.grid(columnspan=50,sticky = E+W,padx=10,pady=10)
        self.direction_msg = Message(p1,text = 'Select Direction of Input:',aspect=400,justify= CENTER).grid(row = 6, column = 0,sticky='W')
        DIRECTION = ['DOWN','UP']
        direction_mode = self.direction = StringVar()
        self.direction.set(DIRECTION[0])
        self.direction_menu = OptionMenu(p1,direction_mode,*DIRECTION)
        self.direction_menu.grid(row = 6, column = 1)

        #--------------------------Select Text File----------------------------#
        self.filechoose_m = Message(p1,text = 'If using tags, choose text file:',aspect = 400).grid(row = 7, column = 0,sticky = 'W')
        self.filechooserbutton = Button(p1,text = "Text File",command = self.get_filename)
        self.filechooserbutton.config(state='disabled')
        self.filechooserbutton.grid(row = 7, column = 1,ipadx=12)


        self.display_path_string = StringVar()
        self.display_path_string.set('Selected Path')
        self.display_path_Label = Label(p1,textvariable = self.display_path_string,bg = '#fff')
        self.display_path_Label.grid(row = 7, column = 2,ipadx = 20)
        #--------------------------Prefixes------------------------------------#
        self.s = ttk.Separator(p1,orient='horizontal')
        self.s.grid(columnspan=50,sticky=E+W,padx=10,pady=10)
        self.row1text_message = Message(p1,text = 'Row 1 Prefix',aspect=300,justify = CENTER).grid(row=9,sticky='W')
        self.row1text = Entry(p1)
        self.row1text.grid(row=9,column=1)
        self.row1text.config(state='disabled')
        self.row2text_message = Message(p1,text = 'Row 2 Prefix',aspect=200,justify = CENTER).grid(row=10,sticky='W')
        self.row2text = Entry(p1)
        self.row2text.grid(row=10,column=1)
        self.row2text.config(state='disabled')

        #---------------------Sequential Number -------------------------------#
        self.sequence1a_message = Message(p1,text = 'Row 1: Lowest -> Highest',aspect=900).grid(row=11,sticky='W')
        self.sequence1a = Entry(p1)
        self.sequence1a.grid(row=11,column=1)
        self.sequence1b = Entry(p1)
        self.sequence1b.grid(row=12,column=1)
        self.sequence2_message = Message(p1,text = 'Row 2: Lowest -> Highest',aspect=800).grid(row=13,sticky='W')
        self.sequence2a = Entry(p1)
        self.sequence2a.grid(row=13,column=1)
        self.sequence2a.config(state='disabled')
        self.sequence2b = Entry(p1)
        self.sequence2b.grid(row=14,column=1)
        self.sequence2b.config(state='disabled')

        #----------------OPEN POPUP TO SET COORDINATES-------------------------#
        self.coordinate_button = Button(p1,text = 'Initial Coordinates',command = self.popup)
        self.coordinate_button.grid(row=15,columnspan=50,pady=padding_y)

        self.display_error_string = StringVar()
        self.display_error = Label(master,textvariable=self.display_error_string)
        self.display_error.grid(sticky = 'S')
        self.start_button = Button(p1,text = "Start",command = self.start_button_onclick)
        self.start_button.grid(row = 16,columnspan=50,pady=padding_y,ipadx=36)
        self.exit_button = Button(master,text = "Quit", command = master.destroy)
        self.exit_button.grid(columnspan=50,sticky = S+E+W,padx=padding_x,pady=padding_y)
        #---------------------Mode Selection----------------------#

    def mode_select(self):
        self.disable_all()
        mode = self.mode_str.get()
        if (mode=='1'):
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')
        if (mode=='2'):
            self.filechooserbutton.config(state='normal')
        if (mode=='3'):
            self.row1text.config(state='normal')
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')
        if (mode=='4'):
            self.row1text.config(state='normal')
            self.sequence1a.config(state='normal')
            self.sequence1b.config(state='normal')
            self.row2text.config(state='normal')
            self.sequence2a.config(state='normal')
            self.sequence2b.config(state='normal')
    def disable_all(self):
            self.filechooserbutton.config(state='disabled')
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
        w = popupWindow(self.master,self.mode_str)
        self.coordinate_button['state'] = 'disabled'
        self.master.wait_window(w.top)
        self.coordinate_button['state'] = 'normal'
        self.coordinates = w.coordinates

#---------------Start Button and stuff that happens after click----------------#
    def start_button_onclick(self):
        mode = str(self.mode_str.get())
        direction = str(self.direction.get())
        coordinates = self.coordinates
        row1prefix = self.row1text.get()
        row2prefix = self.row2text.get()
        row1start=0
        row2start=0
        row1end=0
        row2end=0
        if mode != 2:
            try:
                row1start = int(self.sequence1a.get())
                row1end = int(self.sequence1b.get())
                if mode == '4'
                    row2start = int(self.sequence2a.get())
                    row2end = int(self.sequence2b.get())
            except ValueError:
                self.display_error_string.set('Problem with your entries')
                return

        if mode == '2':
            taglist = self.list_create()
        else: taglist = []

        entries = [row1prefix,row2prefix,row1start,row1end,row2start,row2end]

        runner = pypoweredfunctions(coordinates,entries,mode,direction,*taglist)

    def list_create(self):
        path = self.display_path_string.get()
        text_file = open(path,"r")
        value_list = text_file.read().split('\n')
        text_file.close()
        return value_list



if __name__ == '__main__':
    root = Tk()
    mw = Main_Window(root)
    root.mainloop()
