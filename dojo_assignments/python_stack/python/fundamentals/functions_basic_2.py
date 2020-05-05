#1.
def countdown(num):
    newList = []
    for x in range(num,-1,-1):
        newList.append(x)
    return newList


#2.
def printReturn(listed):
    print(listed[0])
    return listed[1]



#3.
def first_and_length(alist):
    return alist[0] + alist[len(alist)-1]


#4.
def values_greater_than_second(alist):
    newList = []
    count = 0  
    for n in range(len(alist)):
        if alist[n] >= alist[2]:
            count += 1
            newList.append(alist[n])
    print(count)
    return newList


#5.
def listAndValues(size,value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList
