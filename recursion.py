# def countN(n):
#   if n<1: return 0
#   else:
#     countN(n-1)
#     print(n)

# countN(300)

# factorail
# def factorial(n):
#   assert n >= 0 and int(n) == n, 'Positive ineger numbers only!'
#   if n >= 1:
#       print(n)
#       return factorial(n-1) * n
#   else: 
#     return 1
# print('results:',factorial(2))

# fibonacci
# def fib(n):
#     # assert n >=0 and type(n) == int, 'not allowed'
#     if  n == 0 or n == 1:
#         return n
#     else:
#       return fib(n-1) + fib(n-2)
import imp
from itertools import count


1
# print('results:',fib(8))

# def sum(n):
#   if n > 0 and len(str(n)) != 1:
#     return sum(int((str(n)[1:]))) + int(str(n)[0])
#   else: return n

# print(sum(22))

# def powerOf(n, p):
#   if n > 0 and p > 0:
#     return powerOf(n, p-1) * n
#   else: return 1

# print('results:',powerOf(3,2))

# def GCD(a, b):
#   if a >= 0:
#     c = a%b # the remindar.
#     if c == 0:
#       return b
#     return GCD(b,  a%b )
#   else: return 0

# print('results:',GCD(48,18))

# def deciToBinary(num):
#   if num <= 0:
#     return ''
#   a = num % 2
#   b = num // 2
#   return  f'{deciToBinary(b)}' + f'{a}'

# print('results:',deciToBinary(13))
counter = 0

def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    global counter
    counter=counter+1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib(8)
# allFib(8)
print('final: ', counter)

# input4 = 10 , 9
# input6 = 34, 25
# input8 = 100, 67



# python array 
# O(n)
# from array import array
# arr1 = array('B', [2,2,2,2])
# arr1.insert(1,1)
# arr1.remove(2)
# print(arr1)
# from pprint import pprint
# import numpy as np

# twoDArray = np.array([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]])

# # twoDArray = np.append(twoDArray, np.array([[11,22, 33, 44]]).transpose(), axis=1)
# twoDArray = np.delete(twoDArray, 0, axis=0)
# print(twoDArray[-1][-1])


# array = [1,2,3,4]

# for i in range(len(array)):
#   array[i] = array[i]+2
# print(array)

# array1 = [7, 4, 8 , 2, 5]
# array2 = [1,2,3,4]
# a = array1+array2
# print(a)
# array1[0] = 3232
# array1.sort()
# print( array1)

# array =[]
# while (True):
#   user = input('input number:')
#   if user == 'done': break
#   array.append(int(user))
# print(sum(array)/len(array))

# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2] )
# print(a)

# def f(i, values = []):
#     values.append(i)
#     print (values)
#     # return values
# f(1)
# f(2)
# f(3)

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     print(arr[i-1], arr[i])
#     arr[i - 1] = arr[i]
# print(arr)
# for i in range(0, 6): 
#     print(arr[i], end = " ")

