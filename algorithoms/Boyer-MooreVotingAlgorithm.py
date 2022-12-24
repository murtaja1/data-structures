# Boyer-Moore Voting Algorithm: 
# The Boyer-Moore Voting Algorithm is an efficient algorithm for finding the majority element in an array. 
# A majority element is defined as an element that occurs more than n/2 times in an array of length n.

# The algorithm works by maintaining a count variable that is initially set to 0. 
# It then iterates through the array, incrementing the count variable 
# if it encounters an element that is equal to the current candidate for the majority element, 
# and decrementing the count variable if it encounters an element that is not equal to the current candidate.

# If the count variable becomes negative, the algorithm discards the current candidate 
# and sets a new candidate to the element that caused the count to become negative. It then resets the count variable to 1.

# The algorithm terminates when it has processed the entire array. The final candidate is then returned as the majority element.

# time complexity O(n)
# space complexity O(1)
def majorityElement(array):
    count = 0
    candidate = None
    
    for element in array:
        if count == 0:
            candidate = element
            count = 1
        else:
            if element == candidate:
                count += 1
            else:
                count -= 1
    
    return candidate