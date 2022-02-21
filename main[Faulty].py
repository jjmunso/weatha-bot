'''
Neural Network GUI for WeathaBot
Software 3-4
By Jeremie Munso
23/06/2021 @ St Leonards College
'''

#------------- LIBRARIES --------------------
from tkinter import *
from tkinter import scrolledtext

import numpy as np
import csv


window = Tk() #initalise a Tk() object called window, from which we organise the GUI
window.title("WEATHA BOT")
window.geometry('1000x500')
windowHeight = window.winfo_height()
windowWidth = window.winfo_width()
#------------------Functions-------------
def errorMessage(desc,location): #Standardised error message format
	print(desc + " ("+location+")")

def nonlin(x,deriv=False): #Best described here https://fr.wikipedia.org/wiki/Sigmo%C3%AFde_(math%C3%A9matiques), taken directly from https://iamtrask.github.io/2015/07/12/basic-python-network/
	if(deriv==True):
	    return x*(1-x)
	return 1/(1+np.exp(-x)) #Produces weightings more extreme for values closer to centre of sigmoid (steeper gradient) to correct less presise guesses and maintain more certain guesses

def print_value(val): #get the value of the slider
    return val

def funcUpdateScreen(val):
	print (print_value)
	j = 0
    try: #Attempt the following,
        while j < int(val): #Generate the table in reference to the slider
            one = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text=(j+1))
            one.grid(column=j+2,row=3) #Create colums j + 2, avoid overlap for two existing columns

            #-------------OUTPUT-------------
            BASKETBALL = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text=round(week[j][0])) #Basketball output from main function, day J from the forecasted week, index 0 for basketball
            BASKETBALL.grid(column=j+2,row=4)
            AGORA = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text=round(week[j][1])) #Agora output from main function, day J from the forecasted week, index 1 for Agora
            AGORA.grid(column=j+2,row=5)
            ASSEMBLY = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text=round(week[j][2])) #Assembly output from main function, day J from the forecasted week, index 2 for Assembly
            ASSEMBLY.grid(column=j+2,row=6)
            j = j + 1

    except:
        print("I FAILED") #incase something goes wrong in creation of the table, output to the terminal that something has gone wrong
    print ("val: ",val)
    print ("j: ",j)


# -------------------- WEATHER DATA ------------------------
arrDatesWetha = [] #Create Arrays

arrRainfall = []
arrTempMax = []
arrTempMin = []

with open('data/weatha.csv') as csvDataFile:  #Open and read the main csv with past weather data
	csvReader = csv.reader(csvDataFile)
	for column in csvReader:
		if column[0] != "": #Existence Check for data validation
			arrDatesWetha.append(column[0]) #Put the dates in this array from column 0
		else:
			errorMessage("ERROR: Empty Cells in table data","Weather Dates")
		if column[1] != "":#Existence Check for data validation
			arrRainfall.append(column[1]) #Put the rainfal in this array from column 1
		else:
			errorMessage("ERROR: Empty Cells in table data","Rainfall")
		if column[2] != "":#Existence Check for data validation
			arrTempMax.append(column[2]) #Put the tempMax in this array from column 2
		else:
			errorMessage("ERROR: Empty Cells in table data","Temp Max")
		if column[3] != "":#Existence Check for data validation
			arrTempMin.append(column[3]) #Put the tempMin in this array from column 3
		else:
			errorMessage("ERROR: Empty Cells in table data","Temp Min")
arrDatesWetha.pop(0) #Remove the headings of each column
arrRainfall.pop(0)
arrTempMax.pop(0)
arrTempMin.pop(0)



# -------------------- USABILITY DATA ------------------------
arrDatesUsability = []

arrBasketball = []
arrAgora = []
arrAssembly = []



with open('data/usability.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for column in csvReader:
		if column[0] != "":#Existence Check for data validation
			arrDatesUsability.append(column[0]) #Put the dates in this array from column 0
		else:
			errorMessage("ERROR: Empty Cells in table data","Usability Dates")
		if column[1] != "":#Existence Check for data validation
			arrBasketball.append(column[1]) #Put the rainfal in this array from column 1
		else:
			errorMessage("ERROR: Empty Cells in table data","Basketball")
		if column[2] != "":#Existence Check for data validation
			arrAgora.append(column[2]) #Put the tempMax in this array from column 2
		else:
			errorMessage("ERROR: Empty Cells in table data","Agora")
		if column[3] != "":#Existence Check for data validation
			arrAssembly.append(column[3]) #Put the tempMin in this array from column 3
		else:
			errorMessage("ERROR: Empty Cells in table data","Assembly")
arrDatesUsability.pop(0) #Remove the headings of each column
arrBasketball.pop(0)
arrAgora.pop(0)
arrAssembly.pop(0)


arrInside = []
i = 1
if len(arrRainfall) == len(arrTempMax) and len(arrTempMax) == len(arrTempMin):
	while i < len(arrRainfall):
		day = round(float(arrRainfall[i])),round(float(arrTempMax[i])),round(float(arrTempMin[i]))
		arrInside.append(day)
		i=i+1

trainingData = np.array(arrInside)



#Needs to be simplified to an iteration
#Define the training answers using coloums usability for each facility and rows for number of (sample) days

#CURRENTLY USING Basketball to test the program
arrInside = []
i = 1
while i < len(arrBasketball):
	ans = int(arrBasketball[i]),int(arrAgora[i]),int(arrAssembly[i])
	arrInside.append(ans)
	i=i+1
trainingAnswers = np.array(arrInside)



#MAIN TRAINING PROGRAM

X = np.array(trainingData)

y = np.array(trainingAnswers)

np.random.seed(1)


syn0 = 2*np.random.random((3,(len(trainingData)))) - 1
syn1 = 2*np.random.random(((len(trainingData)),3)) - 1

for j in range(60000):
    n0 = X
    n1 = nonlin(np.dot(n0,syn0))
    n2 = nonlin(np.dot(n1,syn1))
    n2_error = y - n2 #what was the error between answer(y) and guess(passed to n2)
    if (j% 10000) == 0:
        print ("Error:" + str(np.mean(np.abs(n2_error))))
    n2_delta = n2_error*nonlin(n2,deriv=True) #use sigmoid function to make corrections depending on how uncertain (close to 0.5) the program's guess was
    n1_error = n2_delta.dot(syn1.T)
    n1_delta = n1_error * nonlin(n1,deriv=True)
    syn1 += n1.T.dot(n2_delta)
    syn0 += n0.T.dot(n1_delta)


#---------------FORECAST-------------------
week = []
forecastData = [[1.0,11.5,4.4], #Weather data for 22-28 of July as new data to test the system on
                [0.2,11.0,7.3],
                [0,14.3,7.6],
                [1.2,12.0,5.8],
                [0,17.2,7.8],
                [0,17.1,10.2],
                [0,16.3,11.6]]
i = 0
while i < 7:
    n0 = forecastData[i] #Take forecast data for current index
    n1 = nonlin(np.dot(n0,syn0)) #pass through layer 1
    n2 = nonlin(np.dot(n1,syn1)) #Produce a prediction using layer 2
    print (n2) #Output that prediction
    i=i+1
    week.append(n2) #add the prediction (array with 3 elements) to another array called week for later referencing and displayment to end user


saveFile = open("latestOutput.txt", 'w+') #w+ for write, and a+ for append
saveFile.write(str(week)) #save the prediction for the week to latestOutput.txt
saveFile.close()



slider = Scale(window, to=7, orient=HORIZONTAL, length=None,command=print_value) #NOTICE command is the method to get the value of the slider
slider.grid(row=1,column=0,columnspan=3,padx=(10,7),sticky='NESW') #Have the slider span 3 colums at the the top of the program (row 0, column 0)

#------------ Table Labels -----------------
while True:
	days = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= "Days")
	days.grid(column=2,row=2, columnspan=2)
    #FACILITIES
	facility = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Faclities')
	facility.grid(column=0,row=3, rowspan=3)
	basketball = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Basketball')
	basketball.grid(column=1,row=4)
	agora = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Agora')
	agora.grid(column=1,row=5)
	assembly = Label(window,width=windowWidth+10,height=windowHeight,borderwidth=2,relief="solid",text= 'Assembly')
	assembly.grid(column=1,row=6)
	updateButton = Button(window,text= 'Update', command=funcUpdateScreen)
	updateButton.grid(column=1,row=0, columnspan=1)
# Instead of window.mainloop(), window.update() allows data to be live, this is neccessary for the slider function to have correlation to the table length
	window.mainloop() #initalise the window
