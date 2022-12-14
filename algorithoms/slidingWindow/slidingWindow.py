# Sliding Window: It is a technique for reducing the complexity of algorithms. 
                # It is used such that the need for reusing the loops gets reduced and hence the program gets optimized. 
                # In this technique, we reuse the result of the previous step to compute the result of the next step.
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