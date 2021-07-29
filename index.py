'''
Neural Network for WeathaBot
Software 3-4
By Jeremie Munso
12/06/2021 @ St Leonards College
'''
#------------- LIBRARIES --------------------
import numpy as np
import csv

#------------------Functions-------------
def errorMessage(desc,location): #Standardised error message format
	print(desc + " ("+location+")")

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)
	return 1/(1+np.exp(-x))

# -------------------- WEATHER DATA ------------------------
arrDatesWetha = []

arrRainfall = []
arrTempMax = []
arrTempMin = []

with open('data/weatha.csv') as csvDataFile:  #Open and read the main csv with past weather data
	csvReader = csv.reader(csvDataFile)
	for column in csvReader:
		if column[0] != "":
			arrDatesWetha.append(column[0]) #Put the dates in this array from column 0
		else:
			errorMessage("ERROR: Empty Cells in table data","Weather Dates")
		if column[1] != "":
			arrRainfall.append(column[1]) #Put the rainfal in this array from column 1
		else:
			errorMessage("ERROR: Empty Cells in table data","Rainfall")
		if column[2] != "":
			arrTempMax.append(column[2]) #Put the tempMax in this array from column 2
		else:
			errorMessage("ERROR: Empty Cells in table data","Temp Max")
		if column[3] != "":
			arrTempMin.append(column[3]) #Put the tempMin in this array from column 3
		else:
			errorMessage("ERROR: Empty Cells in table data","Temp Min")
arrDatesWetha.pop(0)
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
		if column[0] != "":
			arrDatesUsability.append(column[0]) #Put the dates in this array from column 0
		else:
			errorMessage("ERROR: Empty Cells in table data","Usability Dates")
		if column[1] != "":
			arrBasketball.append(column[1]) #Put the rainfal in this array from column 1
		else:
			errorMessage("ERROR: Empty Cells in table data","Basketball")
		if column[2] != "":
			arrAgora.append(column[2]) #Put the tempMax in this array from column 2
		else:
			errorMessage("ERROR: Empty Cells in table data","Agora")
		if column[3] != "":
			arrAssembly.append(column[3]) #Put the tempMin in this array from column 3
		else:
			errorMessage("ERROR: Empty Cells in table data","Assembly")
arrDatesUsability.pop(0)
arrBasketball.pop(0)
arrAgora.pop(0)
arrAssembly.pop(0)


#

'''
#Define the training data using coloums number of variables and rows number of (sample) days
day1 = [round(float(arrRainfall[0])),round(float(arrTempMax[0])),round(float(arrTempMin[0]))]
day2 = [round(float(arrRainfall[1])),round(float(arrTempMax[1])),round(float(arrTempMin[1]))]
day3 = [round(float(arrRainfall[2])),round(float(arrTempMax[2])),round(float(arrTempMin[2]))]
day4 = [round(float(arrRainfall[3])),round(float(arrTempMax[3])),round(float(arrTempMin[3]))]

trainingData = np.array([day1,day2,day3,day4])

'''
arrInside = []
i = 1
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
'''
trainingData = np.array(arrInside)
bask1 = int(arrBasketball[0])
bask2 = int(arrBasketball[1])
bask3 = int(arrBasketball[2])
bask4 = int(arrBasketball[3])
trainingAnswers = np.array([[bask1],[bask2],[bask3], [bask4]])
'''


X = np.array(trainingData)

y = np.array(trainingAnswers)

np.random.seed(1)


syn0 = 2*np.random.random((3,(len(trainingData)))) - 1
syn1 = 2*np.random.random(((len(trainingData)),3)) - 1

for j in range(10000):
    n0 = X
    n1 = nonlin(np.dot(n0,syn0))
    n2 = nonlin(np.dot(n1,syn1))
    n2_error = y - n2
    if (j% 100000) == 0:
        print ("Error:" + str(np.mean(np.abs(n2_error))))
    n2_delta = n2_error*nonlin(n2,deriv=True)
    n1_error = n2_delta.dot(syn1.T)
    n1_delta = n1_error * nonlin(n1,deriv=True)
    syn1 += n1.T.dot(n2_delta)
    syn0 += n0.T.dot(n1_delta)

#l0 = [round(float(arrRainfall[i])),round(float(arrTempMax[i])),round(float(arrTempMin[i]))] #prediction test
#n0 = [25,11,0] #DATA FOR 22nd RETURNS 1,1,0 WHICH AGREES WITH SPREADSHEET
#n0 = [0,11,7] #DATA FOR 23rd RETURNS 1,1,0 WHICH DISAGREES WITH SPREADSHEET
n0 = [7,12.8,6.7] # DATA FOR LAST TRAINING DAY
n1 = nonlin(np.dot(n0,syn0))
n2 = nonlin(np.dot(n1,syn1))
print (n2)

saveFile = open("latestOutput.txt", 'w+') #w+ for write, and a+ for append
saveFile.write(str(n2))
saveFile.close()
