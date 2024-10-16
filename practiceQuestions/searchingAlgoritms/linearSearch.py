# linear search implementation

from types import List


# using for loop and compare every number of the array with the target number sequentially
# return the number index if the target value is found or 
# return -1 if non of the element of the given array are not equall to the target number

def linearSearch(arr: List, target: int) -> int:
    for (index, value) in enumerate(arr):
        if (value == arr[index]):
            return input
    return -1



# sample data
arr = [1,2,3,4,5,6,7,8,9]
target = 4


returnValue  = linearSearch(arr, target)

print("the returned value is: ", returnValue)

