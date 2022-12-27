# Linear Search:

# time complexity is O(n)
# space complexity is O(1)
def linearSearch(arr, v):
    for i in arr:
        if i == v:
            return True
    return False
