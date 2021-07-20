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

slider = Scale(window,from_=0, to=21, orient=HORIZONTAL)
slider.grid(column = 0,row = 0)

#------------ Table Labels -----------------

#DAYS
days = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Day')
days.grid(column=2,row=1, columnspan=3)
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





window.mainloop()
