# Sliding Window: It is a technique for reducing the complexity of algorithms. 
                # It is used such that the need for reusing the loops gets reduced and hence the program gets optimized. 
                # In this technique, we reuse the result of the previous step to compute the result of the next step.

# check https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/859612505/

# Fixed Sliding Window: time complexity is O(n)
# ex:
k = 3
arr = [1, 2, 3, 4, 5, 6]
# sum of first three is (6), so we subtract the sum from the first element we get 5. 
# then we add 5 to 4, we get 9 and so on... (1+2+3)=6, (6-1+4)=9, (9-2+5)=12,


# code implementation: 
def fixed_sliding_window(arr, k):
    # sum up the first subArray and add it the result.
    curr_subArray = sum(arr[:k])
    result = [curr_subArray]
    # to get each subSequent subArray, add the next value in the list and remove the first value
    for i in range(1, len(arr)-k+1):
        curr_subArray = curr_subArray - arr[i-1]
        curr_subArray = curr_subArray + arr[i+k-1]
        result.append(curr_subArray)
    return result
# fixed_sliding_window(arr, k)

# Dynamic Sliding Window: time complexity is O(n)
# find the largest or smallest subArray that matches (x) in array.

x = 3
arr = [1, 2, 3, 4, 5, 6]

# first [1] is less than x, then [1,2] which their sum >= x (current min_length is 2),
# then removes first, we get [2] >= than x
# then we add next element [2,3] which their sum >= x (current min_length is 2), 
# then removes first, we get [3] >= than x which its sum >= x (current min_length is 1)...

def dynamic_sliding_window(arr, x):
    # track our min subArray
    min_length = float('inf') # inf used to avoid setting the min value as we do not know what it is, (removes the guesswork).

    # the current range and sum of our sliding window.
    start = 0
    end = 0
    current_sum = 0

    # extend the sliding window until our criteria is met.
    while end < len(arr):
        current_sum = current_sum + arr[end]
        end += 1

        # then contract the sliding window until it is no longer meets our condition
        while start < end and current_sum >= x:
            current_sum = current_sum - arr[start]
            start += 1

            # update the min length if this is shorter than the current min.
            min_length = min(min_length, end-start+1)
    return min_length

# dynamic_sliding_window([1, 2, 3, 4, 5, 6], 3)


