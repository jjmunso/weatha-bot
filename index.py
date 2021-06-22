'''
Neural Network for WeathaBot
Software 3-4
By Jeremie Munso
12/06/2021 @ St Leonards College
'''

import numpy as np
import csv

arrDatesWetha = []

arrRainfall = []
arrTempMax = []
arrTempMin = []

with open('weatha.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for column in csvReader:
		arrDates.append(column[0])
		arrRainfall.append(column[1])
		arrTempMax.append(column[2])
		arrTempMin.append(column[3])

arrDatesUsability = []

arrBasketball = []
arrAgora = []
arrAssembly = []

with open('usability.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for column in csvReader:
		arrDates.append(column[0])
		arrBasketball.append(column[1])
		arrAgora.append(column[2])
		arrAssembly.append(column[3])






def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

#Define the training data using coloums number of variables and rows number of (sample) days
trainingData = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])

#Define the training answers using coloums usability for each facility and rows for number of (sample) days
trainingAnswers = np.array([[0],
			[1],
			[1],
			[0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((3,4)) - 1 #3 coloums, 4 rows?
syn1 = 2*np.random.random((4,1)) - 1 #4 rows 1 colum?

for j in range(60000):

	# Feed forward through layers 0, 1, and 2
    l0 = trainingData
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # how much did we miss the target value?
    l2_error = trainingAnswers - l2

    if (j% 10000) == 0:
        print ("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

l0 = [1,0,1]
l1 = nonlin(np.dot(l0,syn0))
l2 = nonlin(np.dot(l1,syn1))
print (l2)

saveFile = open("latestOutput.txt", 'w+') #w+ for write, and a+ for append
saveFile.write(str(l2))
saveFile.close()
