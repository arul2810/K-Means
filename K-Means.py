from Precode import *
from matplotlib import pyplot as plt
import numpy
data = np.load('AllSamples.npy')
k1,i_point1,k2,i_point2 = initial_S1('3728')

# Splitting ipoints into x and y and splitting of data points
if 1 :
    i = 0
    ipointx = []
    ipointy = []
    while i < k1 :
        ipointx.append(i_point1[i][0])
        ipointy.append(i_point1[i][1])
        i = i + 1

    # For splitting data into x and y co-ordinates
    if 1:
        data_x = []
        data_y = []
        length = len(data)
        i= 0
    while i < length:
        data_x.append(data[i][0])
        data_y.append(data[i][1])
        i = i + 1

def classification(k,ipointx,ipointy,datax,datay):
    i = 0
    length = len(datax)
    classify = []
    while i < length:
        j = 0
        while j < k:
            tempx = numpy.subtract(datax[i],ipointx[j])
            tempy = numpy.subtract(datay[i],ipointy[j])
            tempx = numpy.square(tempx)
            tempy = numpy.square(tempy)
            dist = numpy.sqrt((tempy+tempx))
            if j == 0 :
                previous = dist
                index = j
            elif previous > dist:
                previous = dist
                index = j
            j = j + 1
        classify.append(index)
        i = i + 1
    return (classify)

def objective_function(k,ipoint_x,ipoint_y,data_x,data_y,classifydata):
    objvalue = 0
    i = 0

    length = len(data)
    while i < k:
        j =0
        while j < length:
            if i == classifydata[j]:
                temp_x = numpy.square(ipoint_x[i]-data_x[j])
                temp_y = numpy.square(ipoint_y[i]-data_y[j])
                temp = temp_x + temp_y
                objvalue = temp + objvalue
            j = j + 1
        i = i + 1
    return(objvalue)


def newpoint (k,ipointx,ipointy,datax,datay,classifydata,data):
    i = 0

    temp_x = []
    temp_y = []
    newpoint = []

    length = len(datax)

    while i < k:
        j = 0
        summ = []
        #summ_y = []
        iterations = 0
        while j < length:

            if i == classifydata[j]:
                summ.append(data[j])
                iterations = iterations + 1
                #summ_y.append(data[j])

            j = j + 1

        temp = numpy.mean(summ,axis = 0)

        temp_x.append(temp[0])
        temp_y.append(temp[1])

        i = i + 1
    newpoint = numpy.append(temp_x,temp_y)
    return (newpoint)


classify = classification(k1,ipointx,ipointy,data_x,data_y)
newpoints = newpoint(k1,ipointx,ipointy,data_x,data_y,classify,data)
i = 0
ipointx = []
ipointy = []
previousx = []
previousy = []
iterations = 0
while i < k1:
    ipointx.append(newpoints[i])
    ipointy.append(newpoints[i+k1])
    i = i + 1
while True:
    classify = classification(k1, ipointx, ipointy, data_x, data_y)
    previousx = ipointx
    previousy = ipointy
    newpoints = newpoint(k1, ipointx, ipointy, data_x, data_y, classify, data)
    i = 0
    ipointx = []
    ipointy = []
    while i < k1:
        ipointx.append(newpoints[i])
        ipointy.append(newpoints[i + k1])
        i = i + 1
    if numpy.array_equal(previousx,ipointx) and numpy.array_equal(previousy,ipointy):
        break
    else:
        iterations = iterations  + 1

i = 0
length = len(data)
print("Iterations",iterations)
print("X Points",ipointx)
print("Y Points",ipointy)
while i < length:

    if classify[i] == 0:
        plt.scatter(data_x[i],data_y[i],color = 'green')
    elif classify[i] == 1:
        plt.scatter(data_x[i],data_y[i],color = 'red')
    else:
        plt.scatter(data_x[i],data_y[i],color = 'blue')
    i = i + 1

plt.show()

# Splitting k2 parts
if 1 :
    i = 0
    ipointx = []
    ipointy = []
    while i < k2 :
        ipointx.append(i_point2[i][0])
        ipointy.append(i_point2[i][1])
        i = i + 1

obj = objective_function(k1,ipointx,ipointy,data_x,data_y,classify)
print("Objective Function:",obj)

#clustering of k2
classify = classification(k2,ipointx,ipointy,data_x,data_y)
newpoints = newpoint(k2,ipointx,ipointy,data_x,data_y,classify,data)
i = 0
ipointx = []
ipointy = []
previousx = []
previousy = []
iterations = 0
while i < k2:
    ipointx.append(newpoints[i])
    ipointy.append(newpoints[i+k1])
    i = i + 1
while True:
    classify = classification(k2, ipointx, ipointy, data_x, data_y)
    previousx = ipointx
    previousy = ipointy
    newpoints = newpoint(k2, ipointx, ipointy, data_x, data_y, classify, data)
    i = 0
    ipointx = []
    ipointy = []
    while i < k2:
        ipointx.append(newpoints[i])
        ipointy.append(newpoints[i + k2])
        i = i + 1
    if numpy.array_equal(previousx,ipointx) and numpy.array_equal(previousy,ipointy):
        break
    else:
        iterations = iterations  + 1

i = 0
length = len(data)
print("Iterations",iterations)
print("X Points",ipointx)
print("Y Points",ipointy)
while i < length:

    if classify[i] == 0:
        plt.scatter(data_x[i],data_y[i],color = 'green')
    elif classify[i] == 1:
        plt.scatter(data_x[i],data_y[i],color = 'red')
    elif classify[i] == 2:
        plt.scatter(data_x[i], data_y[i], color='blue')
    elif classify[i] == 3:
        plt.scatter(data_x[i], data_y[i], color='orange')
    elif classify[i] == 4:
        plt.scatter(data_x[i], data_y[i], color='black')

    i = i +1

plt.show()

obj = objective_function(k2,ipointx,ipointy,data_x,data_y,classify)
print("Objective Function:",obj)
