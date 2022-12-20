class CSort:
    # Bubble Sort: aka Sinking sort.
    # We repeatedly compare each pair of adjacent element and swap them if they are in the wrong order.
    # usage
        # It's simple and useful for smaller sets of elements but is inefficient for larger sets.
    # time complexity is O(n*2)
    # space complexity is O(1)
    def bubbleSort(self, cList):
        for i in range((len(cList)-1)):
            for j in range(len(cList)-i-1): # cos last ones are sorted.
                if cList[j] > cList[j+1]: 
                    cList[j], cList[j+1] = cList[j+1], cList[j]
        return cList

    # Selection Sort: we repeatedly find the min element and move it to the sorted part of array to make the unsorted part sorted.
    # usage:
        # Selection sort can be good at checking if everything is already sorted. 
        # It is also good to use when memory space is limited. 
        # This is because unlike other sorting algorithms, selection sort doesn't go around swapping things until the very end, resulting in less temporary storage space used.
    # time complexity is O(n*2)
    # space complexity is O(1)
    def selectionSort(self, cList):
        for i in range((len(cList))):
            min_index = i
            for j in range(i+1, len(cList)): # cos last ones are sorted. 
                if cList[min_index] > cList[j]:
                    min_index = j 
            cList[i], cList[min_index] = cList[min_index], cList[i]
        return cList

    # Insertion Sort:
        # 1. divide the array into two parts.
        # 2. take the first element from unsorted part and find its correct place in the sorted part.
        # 3. repeat until unsorted is empty.
    # usage:
        # When the array is nearly sorted - since insertion sort is adaptive. When we have memory usage constraints. 
        # When a simple sorting implementation is desired. When the array to be sorted is relatively small.
        # most commonly used sorting algorithms when it comes to the ordering of a deck of cards in everyday life.
    # time complexity is O(n*2)
    # space complexity is O(1)
    def insertionSort(self, cList):
        for i in range(1, len(cList)):
            key = cList[i]
            j = i - 1
            # Compare key with each element on the left of it until an element smaller than it is found
            # For descending order, change key<array[j] to key>array[j].     
            while j >= 0 and key < cList[j]:
                # to move each one one step ahead.
                cList[j+1] = cList[j]
                j -= 1
            print(cList)
            cList[j+1] = key
        return cList


cList = [2, 5, 1, 3, 4, 6, 8, 9, 7]
cSort = CSort()
print(cSort.insertionSort(cList))

# Note: if nested loop and each time the number of N reduced by one (not by half or third mostly half) then it's O(n*2).
