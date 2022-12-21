import math

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

    # Bucket Sort: check visualization\sort\bucketSort.png.
        # create buckets and distribute elements into buckets.
        # sort buckets using a sorting algorithm.
        # merge buckets after sorting.
    # usage:
    # when uniformly distributed over range. ex: 1, 2, 3, 4, 5. not correct 1, 43, 53, 2, 77.
    # when space isn't a concern.
    # time complexity is O(N logN)
    # space complexity is O(N)
    def bucketSort(self, cList):
        # find number of buckets: buckets = round(square(number of elements))
        buckets = round(math.sqrt(len(cList)))
        # find max value
        maxV = max(cList)
        arr = []

        for i in range(buckets):
            arr.append([])
        # distribute elements into
        for i in cList:
            # buckets: ceil(value*buckets/maxV)
            bucket_index = math.ceil(i*buckets/maxV)
            arr[bucket_index-1].append(i)
        # sort the buckets
        for i in range(buckets):
            arr[i] = sorted(arr[i])
        # merge buckets.
        k = 0
        for i in range(buckets):
            for j in range(len(arr[i])):
                cList[k] = arr[i][j]
                k += 1
        return cList
    
    # Merge Sort: it's divide and conquer algorithm. check visualization\sort\merge1.png/merge2.png      
        # divide the input array into two halves and we keep halving recursively until they become too small to divided.
        # merge the halves by sorting them.
    # usage:
        # when you need stable sort.
        # better average time complexity.
        # when space is not a concern.
    # time complexity is O(N logN)
    # space complexity is O(N)
    def mergeSort(self, cList, l, r):
        if l < r:
            m = (l+(r-1))//2 # middle of the array.
            self.mergeSort(cList, l, m) # left part of array.
            self.mergeSort(cList, m+1, r) # right part of array.
            self.merge(cList, l, m, r)
        return cList
    def merge(self, cList, l, m, r):
        lPart = m-l+1 # length of the left part.
        rPart = r-m # length of the right part.

        lArr = [0] * (lPart) # left array.
        rArr = [0] * (rPart) # right array.
        # fill the left array.
        for i in range(0, lPart):
            lArr[i] = cList[l+i]
        # fill the right array.
        for j in range(0, rPart):
            rArr[j] = cList[m+1+j]
        
        # sort and merge them.
        left = 0
        right = 0
        k = l # index of the cList.
        while left < lPart and right < rPart:
            if lArr[left] <= rArr[right]:
                cList[k] = lArr[left]
                left += 1
            else:
                cList[k] = rArr[right]
                right += 1
            k += 1
        # add the rest if any remaining. 
        while left < lPart:
            cList[k] = lArr[left]
            left += 1
            k += 1
        while right < rPart:
            cList[k] = rArr[right]
            right += 1
            k += 1

    # Quick Sort: it's a divide and conquer algorithm. check visualization\sort\quicksort.png
    # find pivot number and make sure small numbers are located at the left side of pivot and bigger at the right of pivot.
    # unlike merge sort, extra space is not needed.
    # time complexity is O(N logN)
    # space complexity is O(N)
    def quickSort(self, cList, low, high):
        if low < high:
            pi = self.partition(cList, low, high) # the pi is sorted.
            self.quickSort(cList, low, pi-1)
            self.quickSort(cList, pi+1, high)
        return cList
        
    def partition(self, cList, low, high):
        i = low - 1
        pivot = cList[high]
        for j in range(low, high):
            # if j is less than or equal to pivot, then swap the j with i  
            if cList[j] <= pivot:
                i += 1
                cList[i], cList[j] = cList[j], cList[i]
        cList[i+1], cList[high] = cList[high], cList[i+1]
        return (i+1)
    
    # Heap Sort: uses heap tree.
    # time complexity is O(N logN)
    # space complexity is O(1)
    def heapSort(self, cList):
        n = len(cList)
        for i in range(int(n/2)-1, -1, -1):
            self.heapify(cList, n, i)
        for i in range(n-1, 0, -1):
            cList[i], cList[0] = cList[0], cList[i]
            self.heapify(cList, i, 0)
        return cList

    def heapify(self, cList, n, i):
        smallest = i
        l = 2*i+1
        r = 2*i+2
        if l < n and cList[l] < cList[smallest]:
            smallest = l
        if r < n and cList[r] < cList[smallest]:
            smallest = r
        
        if smallest != i:
            cList[i], cList[smallest] = cList[smallest], cList[i]
            self.heapify(cList, n, smallest)
              
cList = [2, 5, 1, 3, 4, 6, 8, 9, 7]
cSort = CSort()
print(cSort.heapSort(cList))

# Note: if nested loop and each time the number of N reduced by one (not by half or third, mostly half) then it's O(n*2).