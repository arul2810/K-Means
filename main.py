from Precode2 import *
import numpy
data = np.load('AllSamples.npy')
k1,i_point1,k2,i_point2 = initial_S2('3728')


def classify(k, ipoint, data):
    i = 0
    length = len(data)
    index = []
    while i < length:
        j = 0
        previous = 0

        while j < k:
            distance = numpy.linalg.norm(data[i] - ipoint[j])
            if j == 0:
                previous = distance
                tempindex = j
            elif previous >= distance:
                previous = distance
                tempindex = j
            j = j + 1
        index.append(tempindex)
        i = i + 1
    return (index)


def new_point(k, ipoint, data, classifydata):
    # Calculating new mean
    i = 0
    j = 0
    newpoint = []
    length = len(data)
    while i < k:
        j = 0
        iterations = 0
        summ = []
        temp = []

        while j < length:
            if i == classifydata[j]:
                summ.append(data[j])
                iterations = iterations + 1
            j = j + 1
        print(iterations)
        print(summ)
        temp = numpy.mean(summ, axis=0)
        newpoint.append(temp)
        i = i + 1
    return (newpoint)


def objective_function(k, ipoint, data, classifydata):
    objvalue = 0
    i = 0
    j = 0
    length = len(data)
    while i < k:
        j = 0
        temp = []
        summ = []
        while j < length:
            if i == classifydata[j]:
                temp = numpy.subtract(ipoint[i], data[j])
                temp_summ = numpy.square(numpy.linalg.norm(temp))
                objvalue = temp_summ + objvalue
            j = j + 1
        i = i + 1
    return (objvalue)


def point_classification(k, ipoint, data):
    i = 0
    j = 0
    length = len(data)
    points = [ipoint]
    tempdata = [data]
    while i < k - 1:
        previous = 0
        j = 0



        while j < length:

            distance = numpy.linalg.norm(tempdata[0][j]-points[i])

            if j == 0:
                previous = distance
                tempindex = j
            elif previous < distance:

                previous = distance
                tempindex = j
            j = j + 1


        points.append(data[tempindex])
        #print(points)
        i = i + 1

    return (points)

def testing(data,ipoint):

    print(data[0])
    #print(numpy.linalg.norm(data[0]-ipoint[1]))
    print(ipoint)


classi = point_classification(k1, i_point1, data)

testing(data,classi)
#newpoint = new_point(k1,classi,data,classify_data)

# print(objfunc)
# print(classi)
# classi = classify(k1,newpoint,data)
# newpoint = new_point(k1,newpoint,data,classi)
# objfunc = objective_function(k1,newpoint,data,classi)

#print(k1)
#print(i_point1)
#print(k2)
#print(i_point2)

def point_assingment(k,ipoint,data_x,data_y):

    # iPoint Splitting
    ipoint_x = []
    ipoint_y = []
    ipoint_x.append(ipoint[0])
    ipoint_y.append(ipoint[1])

    i = 0
    length = len(data_x)
    index_check = []
    while i < k-1:
        j = 0

        while j < length:

            temp_x = (data_x[j] - ipoint_x[i])
            temp_y = (data_y[j] - ipoint_y[i])
            temp = numpy.absolute((temp_x*temp_x)-(temp_y*temp_y))
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
