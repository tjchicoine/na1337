import pyautogui
import time
import sys
import os.path
pyautogui.PAUSE = 0.25
pyautogui.FAILSAFE = True
ran = 1
#--------------------------------SETUP-----------------------------------------#
#Either run increasing numbers or same text multiple times
sequence = 0

#Number of rows for sametext (max two)
num_rows = 0

#Set different_names to one to pull tags from text file into nanocad sequentially
different_names = 1
#Tag names from notepad, directory must be specified - theoretically no max number of tags
#but be aware of actual screen limitations and space on paper
directory = "C:/Users/tyler/Desktop/Scripts"
file_name = "values.txt"

#Plain text to enter in prompt
row_one_text = "COM"
row_two_text = "V+"
#-------------------------------HOW MANY?--------------------------------------#
#Terminal Numbers Row one starts at 0
row_1 = 16
#Row 2 START AND FINISH NUMBER
row_2_start = 16
row_2_end = 33
#Row 3 START AND FINISH NUMBER
row_3_start = 34
row_3_end = 51
#------------------STARTING COORDINATES - SEQUENTIAL AND TAGS------------------#
x_value1 = 50
y_value1 = 119
#------------------STARTING COORDINATES - SAMETEXT REPETITIVE------------------#
x_value2 = 137
y_value2 = 115
x_value3 = 148
y_value3 = 109
offset = 25
#------------------------------------------------------------------------------#
def start():
    pyautogui.moveTo(1130,16)
    pyautogui.click()

#15px vertical difference for every text
def text_writer(x,x_value,y_value):
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

def tag_writer(x,x_value,y_value):
    pyautogui.typewrite("mtext")
    pyautogui.hotkey("enter")
    pyautogui.typewrite("{},{}".format(x_value,y_value))
    pyautogui.hotkey("enter")
    pyautogui.typewrite("{},{}".format(x_value+60,y_value-10))
    pyautogui.hotkey("enter")
    pyautogui.typewrite("{}".format(x))
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

def list_create():
    text_file = open(file_name,"r")
    value_list = text_file.read().split('\n')
    text_file.close()
    return value_list

try:
    if ran:
        start()
        ran = 0

#-----------------------------SINGLE ROW OF TAGS-------------------------------#
    if different_names:
        tag_list = list_create()
        num_tags = len(tag_list)
        for x in range(num_tags):
            if(x==0):
                x_value = x_value1
                y_value = y_value1
            passval = "{}".format(tag_list[x])
            tag_writer(passval,x_value,y_value)
            y_value = y_value + offset

#-----------------------------ZERO ROW-----------------------------------------#
    if sequence:
        for x in range(row_1):
            if(x==0):
                x_value = x_value1
                y_value = y_value1
            text_writer(x,x_value,y_value)
            y_value = y_value + offset

    pyautogui.alert("Pause one")


#----------------------------FIRST ROW-----------------------------------------#
    for x in range(row_2_start,row_2_end + 1):
        if(x==row_2_start):
            x_value = x_value2
            y_value = y_value2
        if sequence:
            passval = x
        elif(num_rows>=1):
            passval = row_one_text
        else:
            break
        text_writer(passval,x_value,y_value)
        y_value = y_value + offset

    pyautogui.alert("Pause two")

#---------------------------SECOND ROW-----------------------------------------#
    for x in range(row_3_start,row_3_end + 1):
        if(x==row_3_start):
            x_value = x_value3
            y_value = y_value3
        if sequence:
            passval = x
        elif(num_rows==2):
            passval = row_two_text
        else:
            break
        text_writer(passval,x_value,y_value)
        y_value = y_value + offset

except KeyboardInterrupt:
    sys.exit()
