# Binary Search:
# the array must be sorted so that binary search works.

# time complexity is O(logN)
# space complexity is O(1)
def binarySearch(arr, v):
    start = 0
    end = len(arr)-1
    middle = (start+end)//2

    while arr[middle] != v and start <= end:
        if v > arr[middle]:
            start = middle + 1
        else: 
            end = middle - 1
        middle = (start+end)//2
    if arr[middle] == v:
        return True
    else: 
        return False

arr = [1, 2, 3, 4, 5,6]
print(binarySearch(arr, 2))