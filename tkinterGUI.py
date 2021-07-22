'''
Neural Network GUI for WeathaBot
Software 3-4
By Jeremie Munso
23/06/2021 @ St Leonards College
'''


from tkinter import *

from tkinter import scrolledtext

window = Tk()

window.title("WEATHA BOT")

window.geometry('1000x500')

windowHeight = window.winfo_height()
windowWidth = window.winfo_width()


def print_value(val): #This function is used to get the value of the slider and reference it elsewhere in the program
    print (val)
    return val


#------------ TOP TOOL BAR -------------
'''
#Images
imgSelector = PhotoImage(file = r"img/lc_shadowcursor.png")
#imgSelector = imgSelector.zoom(25)
imgConnector = PhotoImage(file = r"img/sc_arrow.png")
#imgConnector = imgConnector.zoom(25)
imgDeleter = PhotoImage(file = r"img/edit-delete.png")
#imgDeleter = imgDeleter.zoom((1))
'''

'''slider = Scale(window,from_=0, to=21, orient=HORIZONTAL, borderwidth=2,relief="solid")
slider.grid(column = 0,row = 0, columnspan=1)'''
slider = Scale(window, to=21, orient=HORIZONTAL, length=None,command=print_value)
slider.grid(row=0,column=0,columnspan=8,padx=(10,7),sticky='NESW') #Have the slider span the top of the program

#------------ Table Labels -----------------
while True:
    try:
        TEST_VALUE=print_value()
        days = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= TEST_VALUE)
        days.grid(column=2,row=1, columnspan=3)
    except:
        print ("WELP")
    one = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'One')
    one.grid(column=2,row=2)
    two = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Two')
    two.grid(column=3,row=2)
    three = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Three')
    three.grid(column=4,row=2)

    #FACILITIES
    facility = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Faclities')
    facility.grid(column=0,row=2, rowspan=3)
    basketball = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Basketball')
    basketball.grid(column=1,row=3)
    agora = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Agora')
    agora.grid(column=1,row=4)
    assembly = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Assembly')
    assembly.grid(column=1,row=5)
# Instead of window.main(), window.update() allows data to be live, this is neccessary for the slider function to have correlation to the table length
    window.update()
