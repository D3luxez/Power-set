#Program to find power set of a set
import math;
def printPowerSet(set, SetSize):
    #find total elements in the power set
    PowerSetSize = (int)(math.pow(2,SetSize));
    outer  = 0;
    inner = 0;
    for outer in range (0, PowerSetSize):
        for inner in range (0, SetSize):
            #check if inner bit n the outerr  bit is set, if set, print inner element from set
            if((outer & (1<<inner))>0):
                print (set[inner],end="")
        print("")
size = int(input("Enter array size: "))
set = []
for i in range (0, size):
    n = int(input("Enter element: "))
    set.append(n)
printPowerSet(set, len(set))