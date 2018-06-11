#Kelcy Gooch & Heshan Fernando (HF191) & Clayton Hudspeth
#Class Section 01
#KJG116

import random
import time

#Add sort functions here
def bubbleSort(badList):
    sorted = False
    length = len(badList) - 1

    while not sorted:
        sorted = True
        for element in range(0, length):
            if badList[element] > badList[element + 1]:
                sorted = False
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold

def selectionSort(source):
        for i in range(len(source)):
            mini = min(source[i:])
            min_index = source[i:].index(mini)
            source[i + min_index] = source[i]
            source[i] = mini


def main(length):
    #Create a list of random numbers
    myList = []

    for i in range(length):
        x = random.randint(1, length)
        myList.append(x)


    #Sort using python sort method
    start = time.time()
    myList.sort()
    stop = time.time()
    total_time = stop - start
    #print("Sorted:", myList)

    print("Time needed for python sort to sort %d items: " % length, total_time)

    #Recreate an unordered list
    for i in range(len(myList)):
        myList[i] = random.randint(1, length)

    #Sort using bubble sort method
    start = time.time()
    bubbleSort(myList)
    stop = time.time()
    total_time = stop - start
    #print("Sorted:", myList)

    print("Time needed for bubble sort to sort %d items: " % length, total_time)


    #Recreate an unordered list
    for i in range(len(myList)):
        myList[i] = random.randint(1, length)

    #Sort using selection sort method
    start = time.time()
    selectionSort(myList)
    stop = time.time()
    total_time = stop - start


    #print("Sorted:", myList)

    print("Time needed for selection sort to sort %d items: " % length, total_time)
    print()
    


for i in (25, 100, 1000, 10000):
    main(i)
