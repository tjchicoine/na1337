#===============================================================================
#---------------------Stuff that hAppens after click---------------------------#
#===============================================================================
import pyautogui as py
class pypoweredfunctions(object):
    def __init__(self,coordinates,entries,mode,direction):
        self.offset = coordinates[0]
        self.xc1 = coordinates [1]
        self.xc2 = coordinates[2]
        self.yc1 = coordinates[3]
        self.yc2 = coordinates[4]
        self.width = coordinates[5]
        self.height = coordinates[6]
        self.row1prefix = entries[0]
        self.row2prefix = entries[1]
        self.row1start = entries[2]
        self.row1end = entries[3]
        self.row2start = entries[4]
        self.row2end = entries[5]

        if mode != "2":
            runner.start()

        #SEQUENTIAL
        if mode == '1':
            #self.sequential(row1start,row1end)

        #TAG NAMES
        if mode == '2':
            taglist = self.list_create()
            #self.different_names()

        #SINGLE ROW SAMETEXT
        if mode == '3':
            #self.by_row(row1start,row1end)

        #SECOND ROW SAMETEXT
        if mode == '4':
            #self.by_row(row1start,row1end)
            #self.by_rowx2(row2start,row2end)

        def sequential(row_1_start,row_1_end):
            for x in range(row_1_start,row_1_end + 1):
                if(x==row_1_start):
                    x_val = int(w.xc1)
                    y_val = int(w.yc1)
                text_writer(x,x_val,y_val)
                if(var1.get() == 'DOWN'):
                    y_val = y_val - int(w.offset)
                else:
                    y_val = y_val + int(w.offset)

        #                -------------TAG NAMES FUNCTION-------------
        def different_names():
            tag_list = list_create()
            num_tags = len(tag_list)
            for x in range(num_tags):
                if(x==0):
                    x_val = int(w.xc1)
                    y_val = int(w.yc1)
                    xbox = int(w.boxx)
                    ybox = int(w.boxy)
                passval = "{}".format(tag_list[x])
                tag_writer(passval,x_val,y_val,xbox,ybox)
                if(var1.get() == 'DOWN'):
                    y_val = y_val - int(w.offset)
                else:
                    y_val = y_val + int(w.offset)

        #                -------------SINGLE ROW FUNCTION-------------
        def by_row(row_2_start,row_2_end):
            for x in range(row_2_start,row_2_end + 1):
                if(x==row_2_start):
                    x_val = int(w.xc1)
                    y_val = int(w.yc1)
                passval = (row_one_text.get() + str(x))
                text_writer(passval,x_val,y_val)
                if(var1.get() == 'DOWN'):
                    y_val = y_val - int(w.offset)
                else:
                    y_val = y_val + int(w.offset)

        #               -------------DOUBLE ROW FUNCTION-------------
        def by_rowx2(row_3_start,row_3_end):
            for x in range(row_3_start,row_3_end + 1):
                if(x==row_3_start):
                    x_val = int(w.xc2)
                    y_val = int(w.yc2)
                passval = (row_two_text.get() + str(x))
                text_writer(passval,x_val,y_val)
                if(var1.get() == 'DOWN'):
                    y_val = y_val - int(w.offset)
                else:
                    y_val = y_val + int(w.offset)

        def sequential_suffix(row_1_start,row_1_end,prefix):
            for x in range(row_1_start,row_1_end + 1):
                if(x==row_1_start):
                    x_val = int(w.xc1)
                    y_val = int(w.yc1)
                suffix = x
                passval = '{}{}'.format(prefix,suffix)
                text_writer(passval,x_val,y_val)
                if(var1.get() == 'DOWN'):
                    y_val = y_val - int(w.offset)
                else:
                    y_val = y_val + int(w.offset)

        #                 -------------py STUFF-------------
        def start():
            py.moveTo(1130,16)
            py.click()

        def text_writer(x,x_value,y_value):
            py.typewrite("dtext")
            py.hotkey("enter")
            py.typewrite("{},{}".format(x_value,y_value))
            py.hotkey("enter")
            py.typewrite("3") #Text size
            py.hotkey("enter")
            py.typewrite("0") #Text Rotation
            py.hotkey("enter")
            py.typewrite("{}".format(x))
            py.keyDown('ctrl')
            py.keyDown('enter')
            py.keyUp('enter')
            py.keyUp('ctrl')

        def tag_writer(x,x_value,y_value,box_x,box_y):
            py.PAUSE = 0.25
            py.typewrite("mtext")
            py.hotkey("enter")
            py.typewrite("{},{}".format(x_value,y_value))
            py.hotkey("enter")
            py.typewrite("{},{}".format(x_value+box_x,y_value-box_y))
            py.hotkey("enter")
            py.typewrite("{}".format(x))
            py.keyDown('ctrl')
            py.keyDown('enter')
            py.keyUp('enter')
            py.kseyUp('ctrl')
