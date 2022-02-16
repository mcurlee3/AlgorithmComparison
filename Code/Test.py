import time
import random
import matplotlib.pyplot as plt
from SortingAlgorithm import *


##This is simply a list of values for testing
##I created the lists in this modular way to make easy changing values and for the purpose of simplified 
#understanding. Each individual list is created based on the range and size indicated by the 
# Alpha-Variables. Naming should help to keep everything organized.
A = 10
B = 100
C = 200
D = 500
AA = 700
BB = 1000
CC = 40000
DD = 50000
EE = 60000
FF = 80000
AAA = 100000

ListA = [random.randint(1,A) for num in range(A)]
ListB = [random.randint(1,B) for num in range(B)]
ListC = [random.randint(1,C) for num in range(C)]
ListD = [random.randint(1,D) for num in range(D)]
ListAA = [random.randint(1,AA) for num in range(AA)]
ListBB = [random.randint(1,BB) for num in range(BB)]
ListCC = [random.randint(1,CC) for num in range(CC)]
ListDD = [random.randint(1,DD) for num in range(DD)]
ListEE = [random.randint(1,EE) for num in range(EE)]
ListFF = [random.randint(1,FF) for num in range(FF)]
ListAAA = [random.randint(1,AAA) for num in range(AAA)]

##Data holds the list of actual arrays while data holds the number of values in each array
Data = [ListA, ListB, ListC, ListD, ListAA, ListBB]
data = [A, B, C, D, AA, BB]

##Because of the way I implemented the testing loop I created a time array for each case and algorithm

##Unsorted Times
isTime = []
msTime = []
hsTime = []
qsTime = []
mqsTime = []

##Sorted Times
isTimeS = []
msTimeS = []
hsTimeS = []
qsTimeS = []
mqsTimeS = []

##Reversed Times
isTimeR = []
msTimeR = []
hsTimeR = []
qsTimeR = []
mqsTimeR = []


i = 0
for d in Data:
    ##Unsorted iterations of each Algorithm
    t=0
    for i in range(5):
        test = d
        start = time.time()
        InsertionSort(test)
        end = time.time()
        t += end - start
    t = t/5
    isTime.append(t)

    t = 0 
    for i in range(5):
        test = d
        start = time.time()
        left = 0
        right = len(test) - 1
        MergeSort(test, left, right)
        end = time.time()
        t += end - start
    t = t/5
    msTime.append(t)

    t=0
    for i in range(5):
        test = d
        start = time.time()
        HeapSortI(test, 0, len(test)-1)
        end = time.time()
        t += end - start
    t = t/5
    hsTime.append(t)

    t=0
    for i in range(5):
        test = d
        start = time.time()
        QuickSortI(test, 0, len(test)-1)
        end = time.time()
        t += end - start
    t = t/5
    qsTime.append(t)

    t=0
    for i in range(5):
        test = d
        start = time.time()
        modQuickSortI(test, 0, len(test)-1)
        end = time.time()
        t += end - start
    t = t/5
    mqsTime.append(t)

    ##Sorted Iterations of each Algorithm
    t=0
    for i in range(5):
        sorted = test
        start = time.perf_counter()
        InsertionSort(sorted)
        end = time.perf_counter()
        t += end - start
    t = t/5
    isTimeS.append(t)

    t=0
    for i in range(5):
        sorted = test
        start = time.time()
        left = 0
        right = len(sorted) - 1
        MergeSort(sorted, left, right)
        end = time.time()
        t += end - start
    t = t/5
    msTimeS.append(t)

    t=0
    for i in range(5):
        sorted = test
        start = time.time()
        HeapSortI(sorted, 0, len(sorted)-1)
        end = time.time()
        t += end - start
    t = t/5
    hsTimeS.append(t)

    t=0
    for i in range(5):
        sorted = test
        start = time.time()
        QuickSortI(sorted, 0, len(sorted)-1)
        end = time.time()
        t += end - start
    t = t/5
    qsTimeS.append(t)

    t=0
    for i in range(5):
        sorted = test
        start = time.time()
        modQuickSortI(sorted, 0, len(sorted)-1)
        end = time.time()
        t += end - start
    t = t/5
    mqsTimeS.append(t)

    ##Reversed Iterations of each Algorithm
    t=0        
    for i in range(5):
        sorted.reverse()
        reversed = sorted
        start = time.time()
        InsertionSort(reversed)
        end = time.time()
        t += end - start
    t = t/5
    isTimeR.append(t)

    t=0
    for i in range(5):
        reversed = sorted
        start = time.time()
        left = 0
        right = len(reversed) - 1
        MergeSort(reversed, left, right)
        end = time.time()
        t += end - start
    t = t/5
    msTimeR.append(t)

    t=0
    for i in range(5):
        reversed = sorted
        start = time.time()
        HeapSort(reversed,  0, len(reversed)-1)
        end = time.time()
        t += end - start
    t = t/5
    hsTimeR.append(t)

    t=0
    for i in range(5):
        reversed = sorted
        start = time.time()
        QuickSortI(reversed, 0, len(reversed)-1)
        end = time.time()
        t += end - start
    t = t/5
    qsTimeR.append(t)

    t=0
    for i in range(5):
        reversed = sorted
        start = time.time()
        modQuickSortI(reversed, 0, len(reversed)-1)
        end = time.time()
        t += end - start
    t = t/5
    mqsTimeR.append(t)
    i += 1

##Visualization Module
plt.plot(data, isTime, "r", label = 'Insertion Sort')
plt.plot(data, msTime, "g", label = 'Merge Sort')
plt.plot(data, hsTime, "b", label = 'Heap Sort')
plt.plot(data, qsTime, "y", label = 'Quick Sort')
plt.plot(data, mqsTime, "m", label = 'Modified Quick Sort')
plt.title("Numbers are randomly generated")
plt.xlabel("Number of elements")
plt.ylabel("Time taken by Algorithms")
plt.legend()
plt.show()

plt.plot(data, isTimeS, "r", label = 'Insertion Sort')
plt.plot(data, msTimeS, "g", label = 'Merge Sort')
plt.plot(data, hsTimeS, "b", label = 'Heap Sort')
plt.plot(data, qsTimeS, "y", label = 'Quick Sort')
plt.plot(data, mqsTimeS, "m", label = 'Modified Quick Sort')
plt.title("Numbers are Sorted")
plt.xlabel("Number of elements")
plt.ylabel("Time taken by Algorithms")
plt.legend()
plt.show()

plt.plot(data, isTimeR, "r", label = 'Insertion Sort')
plt.plot(data, msTimeR, "g", label = 'Merge Sort')
plt.plot(data, hsTimeR, "b", label = 'Heap Sort')
plt.plot(data, qsTimeR, "y", label = 'Quick Sort')
plt.plot(data, mqsTimeR, "m", label = 'Quick Sort')
plt.title("Numbers are Sorted in reverse order")
plt.xlabel("Number of elements")
plt.ylabel("Time taken by Algorithms")
plt.legend()
plt.show()