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


def print_value(val): #get the value of the slider
    print (val)
    window.update()
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
slider = Scale(window, to=21, orient=HORIZONTAL, length=None,command=print_value) #NOTICE command is the method to get the value of the slider
slider.grid(row=0,column=0,columnspan=8,padx=(10,7),sticky='NESW') #Have the slider span the top of the program

#------------ Table Labels -----------------
while True:
    try:
        TEST_VALUE=print_value()
        print("THE TEST VALUE: ", TEST_VALUE)
        days = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= TEST_VALUE)
        days.grid(column=2,row=1, columnspan=3)
        j = 0
        while j < TEST_VALUE:
            print("IM TRYING")
            one = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text=j)
            one.grid(column=2,row=2)
    except:
        pass

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
    window.mainloop()
