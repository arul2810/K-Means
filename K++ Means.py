from Precode2 import *
from matplotlib import pyplot as plt
import numpy
data = np.load('AllSamples.npy')
k1,i_point1,k2,i_point2 = initial_S2('3728')


# Splitting ipoints into x and y and splitting of data points
if 1 :
    i = 0
    ipointx = []
    ipointy = []

    ipointx.append(i_point1[0])
    ipointy.append(i_point1[1])
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

def point_assingment(k,ipoint_x,ipoint_y,data_x,data_y):


    i = 0
    length = len(data_x)
    index_check = []
    while i < k-1:
        j = 0

        while j < length:

            temp_x = numpy.square(data_x[j] - ipoint_x[i])
            temp_y = numpy.square(data_y[j] - ipoint_y[i])
            temp = temp_x + temp_y
            e_dist = numpy.sqrt(temp)
            if j == 0:
                previous = e_dist
                index = j
            elif previous < e_dist and not(j in index_check):
                previous = e_dist
                index = j
            j = j + 1

        index_check.append(index)
        ipoint_x.append(data_x[index])
        ipoint_y.append(data_y[index])
        i = i + 1

    point = numpy.append(ipoint_x,ipoint_y)
    return (point)

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

ipointreturn = point_assingment(k1,ipointx,ipointy,data_x,data_y)
i = 0
while i < k1:
    ipointx.append(ipointreturn[i])
    ipointy.append(ipointreturn[i+k1])
    i = i + 1
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
print("Iterations:",iterations)
print("Point X:",ipointx)
print("Point Y:",ipointy)
while i < length:

    if classify[i] == 0:
        plt.scatter(data_x[i],data_y[i],color = 'green')
    elif classify[i] == 1:
        plt.scatter(data_x[i],data_y[i],color = 'red')
    elif classify[i] == 2:
        plt.scatter(data_x[i],data_y[i],color = 'blue')
    elif classify[i] == 3:
        plt.scatter(data_x[i],data_y[i],color = 'orange')


    i = i + 1

plt.show()

obj = objective_function(k1,ipointx,ipointy,data_x,data_y,classify)
print("Objective Function:",obj)

if 1 :
    i = 0
    ipointx = []
    ipointy = []

    ipointx.append(i_point2[0])
    ipointy.append(i_point2[1])

ipointreturn = point_assingment(k2,ipointx,ipointy,data_x,data_y)
i = 0
while i < k2:
    ipointx.append(ipointreturn[i])
    ipointy.append(ipointreturn[i+k2])
    i = i + 1
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
    ipointy.append(newpoints[i+k2])
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
print("K2 Iterations:",iterations)
print("Point X:",ipointx)
print("Point Y:",ipointy)
while i < length:

    if classify[i] == 0:
        plt.scatter(data_x[i],data_y[i],color = 'green')
    elif classify[i] == 1:
        plt.scatter(data_x[i],data_y[i],color = 'red')
    elif classify[i] == 2:
        plt.scatter(data_x[i],data_y[i],color = 'blue')
    elif classify[i] == 3:
        plt.scatter(data_x[i],data_y[i],color = 'orange')
    elif classify[i] == 4:
        plt.scatter(data_x[i],data_y[i],color = 'black')
    elif classify[i] == 5:
        plt.scatter(data_x[i],data_y[i],color = 'pink')
    i = i + 1

plt.show()


obj = objective_function(k2,ipointx,ipointy,data_x,data_y,classify)
print("Objective Function:",obj)
