#===============================================================================
#---------------------Stuff that hAppens after click---------------------------#
#===============================================================================
import pyautogui as py
class pypoweredfunctions(object):
    def __init__(self,coordinates,entries,mode,direction,*taglist):
        self.offset = coordinates[0]
        self.xc1 = coordinates[1]
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
        self.mode = mode
        self.direction_string = direction

        if mode != '2':
            self.start()

        #Numerical Increment
        if mode == '1':
            self.row(self.row1start,self.row1end,self.xc1,self.yc1,self.mode)

        #List of Tags
        if mode == '2':
            self.start()
            self.Tag_Names(taglist)

        #Single Row
        if mode == '3':
            print(mode)
            self.row(self.row1start,self.row1end,self.xc1,self.yc1,self.mode)

        #Double Row
        if mode == '4':
            self.row(self.row1start,self.row1end,self.xc1,self.yc1,self.mode)
            self.row(self.row2start,self.row2end,self.xc2,self.yc2,self.mode)

    def row(self,rowstart,rowend,xc,yc,mode):
        for x in range(rowstart,rowend + 1):
            if(x==rowstart):
                xval = xc
                yval = yc
            if mode == '1':
                passval = x
            elif mode == '3':
                passval = (self.row1text + str(x))
            self.text_writer(passval,xval,yval)
            yval = self.direction(yval)

    def Tag_Names(self,taglist):
        num_tags = len(taglist)
        for x in range(num_tags):
            if(x==0):
                xval = self.xc1
                yval = self.yc1
                width = self.width
                height = self.height
            passval = "{}".format(taglist[x])
            self.tag_writer(passval,xval,yval,width,height)
            yval = self.direction(yval)

    def direction(self,yval):
        if(self.direction_string == 'DOWN'):
            yval = yval - self.offset
        else: yval = yval + self.offset
        return yval

    #                 -------------py STUFF-------------
    def start(self):
        py.moveTo(1130,16)
        py.click()

    def text_writer(self,x,x_value,y_value):
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

    def tag_writer(self,x,x_value,y_value,width,height):
        py.PAUSE = 0.25
        py.typewrite("mtext")
        py.hotkey("enter")
        py.typewrite("{},{}".format(x_value,y_value))
        py.hotkey("enter")
        py.typewrite("{},{}".format(x_value+width,y_value-height))
        py.hotkey("enter")
        py.typewrite("{}".format(x))
        py.keyDown('ctrl')
        py.keyDown('enter')
        py.keyUp('enter')
        py.keyUp('ctrl')
