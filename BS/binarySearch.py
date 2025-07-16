#binary search python program

import numpy as np
import math


#sorted data 
arr = np.array([1,2,4,7,8,12,14,15,17,18,19,24,27,31,41,53,58,62,63,85,93,95])

target = int(input("Enter the number for the target: "))

def binarySearch(arr):
    lowerBound = 0
    upperBound = len(arr)  - 1

    while lowerBound < upperBound:
        middleBound = math.floor((lowerBound + upperBound) / 2)

        if target == arr[middleBound]:

            return f"Target value available at {middleBound + 1}"
        
        elif target < arr[middleBound]:
            upperBound = middleBound - 1

        else:
            lowerBound = middleBound + 1
        
result = binarySearch(arr)
print(f"Result is at {result}")

#It is an example of divide an conquer technique