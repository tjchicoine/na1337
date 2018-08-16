#===============================================================================
#---------------Start Button and stuff that happens after click----------------#
#===============================================================================
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
