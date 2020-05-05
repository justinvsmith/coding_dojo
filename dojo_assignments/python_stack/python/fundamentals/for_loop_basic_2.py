def length(aList):
    count = 0
    for x in aList:
        count += 1
    return count

#1.
def biggieSize(collection):
    for x in range(length(collection)):
        if collection[x] > 0:
            collection[x] = "big"
    return collection

#2.
def countPositives(x):
    count = 0
    for y in range(length(x)):
        if x[y] > 0:
            count += 1
    x[len(x)-1] = count
    return x

#3.
def sumTotal(x):
    total = 0
    for y in x:
        total += y
    return total

#4.
def average(listing):
    total =0
    for x in range(length(listing)):
        total += listing[x]
    return total/length(listing)

#5.
def length1(aList):
    count = 0
    for x in aList:
        count += 1
    return count

#6.
def minimum(aList):
    if aList == []:
        return False
    else:
        mini = aList[0]
        for x in range(length(aList)):
            if aList[x] < mini:
                mini = aList[x]
    return mini

#7
def maximum(aList):
    if aList == []:
        return False
    else:
        big = aList[0]
        for x in range(length(aList)):
            if aList[x] > big:
                big = aList[x]
    return big

#8.
def ultimateAnalysis(aList):
    newDict = {}
    newDict["sumTotal"] = sumTotal(aList)
    newDict["average"] = average(aList)
    newDict["minimum"] = minimum(aList)
    newDict["maximum"]= maximum(aList)
    newDict["length"] = length(aList)
    return newDict

#9.
list3 = [1,2,3,4,5]

def reverseList(aList):
    j = (length(aList)-1)/2
    for w in range(length(aList)):
        x = 0    
        while x < j:
            temp = aList[x]
            aList[x] = aList[length(aList)-1-x]
            aList[length(aList)-1-x] = temp
            x = x+1
    return aList

print(reverseList(list3))