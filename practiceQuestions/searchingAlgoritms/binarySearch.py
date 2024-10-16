from typing import List
def binarySearch(arr: List[int], target: int) -> int:
    high = len(arr) - 1
    low = 0
    
    while low <= high:
        mid = (low + high) // 2  # Integer division
        
        if arr[mid] == target:
            return mid  # Target found
        elif target > arr[mid]:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half
    
    return -1  # Target not found

# Example usage:
arr = [10, 23, 45, 70, 80, 90]
target = 70

result = binarySearch(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
