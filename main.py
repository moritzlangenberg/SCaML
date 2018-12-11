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


pX1table = np.array([pX1(i) for i in range(0, 10)])
pX2table = np.array([pX2(i) for i in range(0, 10)])
pCtable = np.array([pC(i) for i in range(0, 5)])
pCX1table = np.array([pCX1(i, j) for i in range(0, 5) for j in range(0, 10)]).reshape(5, 10)
pCX2table = np.array([pCX2(i, j) for i in range(0, 5) for j in range(0, 10)]).reshape(5, 10)
pX1X2table = np.array([pX1X2(i, j) for i in range(0, 10) for j in range(0, 10)]).reshape(10, 10)


'''
print("i)")
for n in range(0, numberOfPairs):
    decisionProb = np.zeros(5)
    for iterC in range(0, 5):
        if pX1table[x_1[n]] == 0:
             decisionProb[iterC] = pCtable[iterC]
        else:
            decisionProb[iterC] = (pCX1table[iterC, x_1[n]] / pX1table[x_1[n]])
    maxC = np.argmax(decisionProb)
    # maxC is the choosen class from decicion rule
    # now we add the error
    for iterC in range(0, 5):
        if iterC == c[n]:
            error1 += (decisionProb[iterC] - 1) ** 2
        else:
            error1 += (decisionProb[iterC]) ** 2
error1 = np.divide(error1, numberOfPairs)
print("E(g1) = {}".format(error1))
print("i) Test")
error1 = 0
for iterX1 in range(0, 10):
    for iterX2 in range(0, 10):
        if pX1X2table[x_1[n], x_2[n]] != 0:
            if pX1table[x_1[n]] != 0:
                error1 += pX1X2table[x_1[n], x_2[n]] \
                            * (1 - ((pCX1table[c[n], x_1[n]])/pX1table[x_1[n]])/ \
                            pX1X2table[x_1[n], x_2[n]])
            else:
                error1 += pX1X2table[x_1[n], x_2[n]] \
                            * (1 - pC[c[n]])
        else:
            error1 += pX1X2table[x_1[n], x_2[n]] \
                      * (1 - pC[c[n]])

print("E(g1) = {}".format(error1))

print("i) Test 2")
error1 = 0
for iterX1 in range(0, 10):
    for iterX2 in range(0, 10):
        for iterC in range(0, 5):
            if pX1table[x_1[n]] == 0:
                decisionProb[iterC] = pCtable[iterC]
            else:
                decisionProb[iterC] = (pCX1table[iterC, x_1[n]] / pX1table[x_1[n]])
        maxC = np.argmax(decisionProb)
        if pX1X2table[iterX1, iterX2] != 0:
            error1 += pX1X2table[iterX1, iterX2] * (1 - pCX1X2table[maxC, iterX1, iterX2]/pX1X2table[iterX1, iterX2])
        else:
            error1 += pX1X2table[iterX1, iterX2] * (1 - pCtable[maxC])


print("E(g1) = {}".format(error1))
'''

print("i")
decisionProb = np.zeros(5)
error1 = 0
for iterX1 in range(0, 10):
        for iterC in range(0, 5):
            if pX1table[iterX1] == 0:
                decisionProb[iterC] = pCtable[iterC]
            else:
                decisionProb[iterC] = (pCX1table[iterC, iterX1] / pX1table[iterX1])
        maxC = np.argmax(decisionProb)
        if pX1table[iterX1] != 0:
            error1 += pX1table[iterX1] * (1 - pCX1table[maxC, iterX1]/pX1table[iterX1])
        else:
            error1 += pX1table[iterX1] * (1 - pCtable[maxC])
print("E(g1) = {}".format(error1))


print("ii)")
decisionProb = np.zeros(5)
error1 = 0
for iterX2 in range(0, 10):
        for iterC in range(0, 5):
            if pX2table[iterX2] == 0:
                decisionProb[iterC] = pCtable[iterC]
            else:
                decisionProb[iterC] = (pCX2table[iterC, iterX2] / pX2table[iterX2])
        maxC = np.argmax(decisionProb)
        if pX2table[iterX2] != 0:
            error1 += pX2table[iterX2] * (1 - pCX2table[maxC, iterX2]/pX2table[iterX2])
        else:
            error1 += pX2table[iterX2] * (1 - pCtable[maxC])
print("E(g2) = {}".format(error1))

print("iii)")
decisionProb = np.zeros(5)
error1 = 0
for iterX1 in range(0, 10):
    for iterX2 in range(0, 10):
            for iterC in range(0, 5):
                if pX1X2table[iterX1, iterX2] == 0:
                    decisionProb[iterC] = pCtable[iterC]
                else:
                    decisionProb[iterC] = (pCX1X2table[iterC, iterX1, iterX2] / pX1X2table[iterX1, iterX2])
            maxC = np.argmax(decisionProb)
            if pX1X2table[iterX1, iterX2] != 0:
                error1 += pX1X2table[iterX1, iterX2] * (1 - pCX1X2table[maxC, iterX1, iterX2]/pX1X2table[iterX1, iterX2])
            else:
                error1 += pX1X2table[iterX1, iterX2] * (1 - pCtable[maxC])
print("E(g2) = {}".format(error1))

print("iv)")
for n in range(0, numberOfPairs):
    decisionProb = np.zeros(5)
    for iterC in range(0, 5):
        if pCtable[iterC] == 0:
             decisionProb[iterC] = pCtable[iterC]
        else:
            decisionProb[iterC] = (pCX1X2table[iterC, x_1[n], x_2[n]] / pCtable[iterC])
    maxC = np.argmax(decisionProb)

decisionProb = np.zeros(5)
error1 = 0
for iterX1 in range(0, 10):
    for iterX2 in range(0, 10):
            for iterC in range(0, 5):
                if pX1X2table[iterX1, iterX2] == 0:
                    decisionProb[iterC] = pCtable[iterC]
                else:
                    decisionProb[iterC] = (pCX1X2table[iterC, iterX1, iterX2] / pCtable[iterC])
            maxC = np.argmax(decisionProb)
            if pX1X2table[iterX1, iterX2] != 0:
                error1 += pX1X2table[iterX1, iterX2] * (1 - pCX1X2table[maxC, iterX1, iterX2]/pX1X2table[iterX1, iterX2])
            else:
                error1 += pX1X2table[iterX1, iterX2] * (1 - pCtable[maxC])
print("E(g2) = {}".format(error1))







