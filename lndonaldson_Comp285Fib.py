#Laila Donaldson
#July 31, 2023
#COMP 285 Summer Session
# This program solves the Fibonacci seqence utilizing four different algorithmic approaches in order to test and compare the amount of time it takes each seqence to run

import timeit
import math

#Dictionary to hold fibonacci numbers for dynamic recursive sequence
fibonacciDict = {0:0, 1:1}

#Linear O(N) with an iterative approach
def linearFib(num):
    if (num <= 0):
        return 0
    elif (num == 1):
        return 1
    prevFibNum = 0
    currNum = 1
    i = 1
    while (i < num):
      nextFibNum = prevFibNum + currNum
      prevFibNum = currNum
      currNum = nextFibNum
      i = i + 1
    return currNum

#Dynamic Linear Approach O(1) utilizing Binet's Formula
def dynamicLinearFib(num):
    if (num <= 0):
        return 0
    elif (num == 1):
        return 1
    nextFibNum = (1 + math.sqrt(5))/2    
    prevFibNum = 1 - nextFibNum

    return int((nextFibNum ** num - prevFibNum ** num) / math.sqrt(5))

#Recursive Approach T(N) = T(N-1) + T(N-2), O(2^N)
def recursiveFib(num):
    if (num <= 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return recursiveFib(num - 1) + recursiveFib(num - 2)

#Dynamic Recursive Approach T(N) = T(N-1) + T(N-2) using Memoization, O(N)
def dynamicRecursiveFib(num, fibonacciDict={}):
    if (num <= 0):
        return 0
    elif (num == 1):
        return 1
    if num in fibonacciDict:
        return fibonacciDict[num]
    else:
        fibonacciDict[num] = dynamicRecursiveFib(num - 1) + dynamicRecursiveFib(num - 2)
        return fibonacciDict[num]

#Prints results of each computation
def computeResults(num):
    print("Linear Result:", linearFib(num),"\n  Elapsed Runtime: ", "%.8f" % timeit.timeit(lambda: linearFib(num), setup="pass", number=1), "sec\n")
    print("Dynamic Linear Result:", dynamicLinearFib(num), "\n  Elapsed Runtime: ", "%.8f" % timeit.timeit(lambda: dynamicLinearFib(num), setup="pass", number=1), "sec\n")
    print("Dynamic Recursive Result:", dynamicRecursiveFib(num, fibonacciDict), "\n  Elapsed Runtime: ", "%.8f" % timeit.timeit(lambda: dynamicRecursiveFib(num, fibonacciDict), setup="pass", number=1), "sec\n")
    print("Recursive Result:", recursiveFib(num), "\n  Elapsed Runtime: ", "%.8f" % timeit.timeit(lambda: recursiveFib(num), setup="pass", number=1), "sec\n")
    return

#Choose nth Fibonacci number to compute and display algorithm runtimes
print("*** Fibonacci Sequence ***")
computeResults(35)