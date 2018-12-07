import numpy as np
from numpy.linalg import inv

dataFile = open("data.txt", "r")

data = [word for line in dataFile for word in line.split()]
numberOfPairs = int(len(data)/3)

x_1 = np.array([data[i * 3] for i in range(0, numberOfPairs)], dtype=int)
x_2 = np.array([data[i * 3 + 1] for i in range(0, numberOfPairs)], dtype=int)
c = np.array([data[i * 3 + 2] for i in range(0, numberOfPairs)], dtype=int)

print("Task1")

print("a)")
print("i)")
result1 = (c == 0).sum()
print("p(c=0) = {}".format(result1))

print("ii)")
result2 = (x_1 + x_2 == 0).sum()
print("p(c=0) = {}".format(result2))

print("iii)")
temp3 = (x_1 + x_2 + c == 0).sum()
print("p(c=0) = {}/{}".format(temp3, result1))

print("iv)")
print("p(c=0) = {}/{}".format(temp3, result2))

print("c)")
error1 = 0
error2 = 0
error3 = 0
error4 = 0


#needed methods

def countCX1X2(c_hat, x1, x2):
    result = 0
    for i in range(0, numberOfPairs):
        if (c[i] == c_hat) & (x_1[i] == x1) & (x_2[i] == x2):
            result += 1
    return result


pCX1X2table = np.array([countCX1X2(cc, xx1, xx2)
                 for cc in range(0, 5)
                 for xx1 in range(0, 10)
                 for xx2 in range(0, 10)]).reshape(5, 10, 10)

pCX1X2table = pCX1X2table * np.divide(1, numberOfPairs)



def pX1(x1):
    result = 0
    for c_hat in range(0, 5):
        for x2 in range(0, 10):
            result += pCX1X2table[c_hat, x1, x2]
    return result

def pX2(x2):
    result = 0
    for c_hat in range(0, 5):
        for x1 in range(0, 10):
            result += pCX1X2table[c_hat, x1, x2]
    return result


def pX1X2(x1, x2):
    result = 0
    for c_hat in range(0, 5):
        result += pCX1X2table[c_hat, x1, x2]
    return result


def pC(c_hat):
    result = 0
    for x2 in range(0, 10):
        for x1 in range(0, 10):
            result += pCX1X2table[c_hat, x1, x2]
    return result


def pCX1(c_hat, x1):
    result = 0
    for x2 in range(0, 10):
            result += pCX1X2table[c_hat, x1, x2]
    return result

def pCX2(c_hat, x2):
    result = 0
    for x1 in range(0, 10):
            result += pCX1X2table[c_hat, x1, x2]
    return result

'''
def pX1(x1):
    pX1 = (x_1 == x1).sum()
    pX1 = pX1/numberOfPairs
    return pX1

def pX2(x2):
    pX2 = (x_2 == x2).sum()
    pX2 = pX2/numberOfPairs
    return pX2

def pC(cTemp):
    pC = (c == cTemp).sum()
    pC = pC/numberOfPairs
    return pC
'''

pX1table = np.array([pX1(i) for i in range(0, 10)])
pX2table = np.array([pX2(i) for i in range(0, 10)])
pCtable = np.array([pC(i) for i in range(0, 5)])
pCX1table = np.array([pCX1(i, j) for i in range(0, 5) for j in range(0, 10)]).reshape(5, 10)
pCX2table = np.array([pCX2(i, j) for i in range(0, 5) for j in range(0, 10)]).reshape(5, 10)
pX1X2table = np.array([pX1X2(i, j) for i in range(0, 10) for j in range(0, 10)]).reshape(10, 10)



print("i)")
for n in range(0, numberOfPairs):
    decisionProb = np.zeros(5)
    for iterC in range(0, 5):
        if pX1table[x_1[n]] == 0:
             decisionProb[iterC] = pCtable[iterC]
        else:
            decisionProb[iterC] = (pCX1table[iterC, x_1[n]] / pX1table[x_1[n]])
    maxC = np.max(decisionProb)
    # maxC is the choosen class from decicion rule
    # now we add the error
    for iterC in range(0, 5):
        if iterC == c[n]:
            error1 += (decisionProb[iterC] - 1) ** 2
        else:
            error1 += (decisionProb[iterC]) ** 2
error1 = np.divide(error1, numberOfPairs)
print("E(g1) = {}".format(error1))

print("ii)")
for n in range(0, numberOfPairs):
    decisionProb = np.zeros(5)
    for iterC in range(0, 5):
        if pX2table[x_1[n]] == 0:
             decisionProb[iterC] = pCtable[iterC]
        else:
            decisionProb[iterC] = (pCX2table[iterC, x_2[n]] / pX2table[x_2[n]])
    maxC = np.max(decisionProb)
    # maxC is the choosen class from decicion rule
    # now we add the error
    for iterC in range(0, 5):
        if iterC == c[n]:
            error2 += (decisionProb[iterC] - 1) ** 2
        else:
            error2 += (decisionProb[iterC]) ** 2
error2 = np.divide(error2, numberOfPairs)
print("E(g2) = {}".format(error2))

print("iii)")
for n in range(0, numberOfPairs):
    decisionProb = np.zeros(5)
    for iterC in range(0, 5):
        if pX1X2table[x_1[n], x_2[n]] == 0:
             decisionProb[iterC] = pCtable[iterC]
        else:
            decisionProb[iterC] = (pCX1X2table[iterC, x_1[n], x_2[n]] / pX1X2table[x_1[n], x_2[n]])
    maxC = np.max(decisionProb)
    # maxC is the choosen class from decicion rule
    # now we add the error
    for iterC in range(0, 5):
        if iterC == c[n]:
            error3 += (decisionProb[iterC] - 1) ** 2
        else:
            error3 += (decisionProb[iterC]) ** 2
error3 = np.divide(error3, numberOfPairs)
print("E(g3) = {}".format(error3))

print("iv)")
for n in range(0, numberOfPairs):
    decisionProb = np.zeros(5)
    for iterC in range(0, 5):
        if pCtable[iterC] == 0:
             decisionProb[iterC] = pCtable[iterC]
        else:
            decisionProb[iterC] = (pCX1X2table[iterC, x_1[n], x_2[n]] / pCtable[iterC])
    maxC = np.max(decisionProb)
    # maxC is the choosen class from decicion rule
    # now we add the error
    for iterC in range(0, 5):
        if iterC == c[n]:
            error4 += (decisionProb[iterC] - 1) ** 2
        else:
            error4 += (decisionProb[iterC]) ** 2
error4 = np.divide(error4, numberOfPairs)
print("E(g3) = {}".format(error4))







