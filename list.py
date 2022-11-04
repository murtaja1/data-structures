# count = 0
# def findMisingNum(n):
#   global count
#   for i in n:
#     count = 1 + count
#     if i != count:
#        return count

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# print(findMisingNum(mylist))

# def findSum(nums, num):
#   n = []
#   for i in range(len(nums)): # big O(n**2)
#     for j in range(i+1, len(nums)):
#       if nums[i] + nums[j] == num:
#         n.append([nums[i] , nums[j]])
#   print(n)

# findSum([12, 8, 22, 1], 20)
# import numpy as np

# def maxTwoItems(nums):
#   max_product = 0
#   for i in range(len(nums)): # big O(n**2)
#     for j in range(i+1, len(nums)):
#       pro = nums[i]*nums[j]
#       if pro > max_product:
#         max_product = pro
#   print(max_product)

# arr = np.array([1,5,2,3,6,9,8,10])
# maxTwoItems(arr)

# from pprint import  pprint
# from copy import deepcopy
# # def rotate90(imag):
# #   org = deepcopy(imag)
# #   for i in range(len(org)):
# #     for j in range(len(org[i])):
# #       imag[j][i]= org[len(org)-i-1][j]
# #   pprint(imag)

# def rotate90(imag):
#   imagj = len(imag[0])
#   imagi = len(imag)
#   current = 0
#   first = True
#   # after each step done, then set the next step either [RITH, DOWN, LEFT or UP].
#   nextStep = 'right'
#   for i in range(imagi):
#     for j in range(imagj):
#       # ! GO RIGHT.
#       # first time
#       if i == 0 and j == 0:
#         current = imag[i][j] 
#         imag[i][j] = imag[i+1][0]
#         # check for next condition because j is now less then j in the next conditioin.
#         if j + 1 == imagj:
#           nextStep = 'down'
#         print('right, first: ')
#         for img in imag:
#           print(img)

#       elif nextStep == 'right':
#           temp = imag[i][j] 
#           imag[i][j] = current
#           current = temp 
#           if j + 1 == imagj:
#             nextStep = 'down'
#           print('right: ')
#           for img in imag:
#             print(img)

#       # ! GO DOWN.
#       if nextStep == 'down':
#         # imagj - 1 - i for inner loop and taking last.
#         # print(-((imagj - 1) -j))
#         # print("J: ", j, "I: ", -i)
#         temp = imag[-((imagj - 1) -j)][-i]
#         imag[-((imagj - 1) - j)][-i] = current
#         current = temp
#         if j + 2 == imagi:
#           nextStep = 'left'
#         print('down: ')
#         for img in imag:
#             print(img)

#       # ! GO LEFT.
#       if nextStep == 'left':
#         if first:
#           first = False
#           # the corner only which happens one time.
#           temp = imag[-1][-2]
#           imag[-1][-2] = current
#           current = temp
#         else:
#           temp = imag[-(imagi - i)][-(imagi + j)] 
#           imag[-(imagi - i)][-(imagi + j)] = current
#           current = temp
#           if imagi - j == imagj:
#             first = True
#             nextStep = 'up'
#         print('left: ')
#         for img in imag:
#             print(img)        

#       # ! GO UP.
#       if nextStep == 'up':
#         print('j: ', j, "i: ", i, imag[-(imagj-j)][0], current)
#         temp = imag[-(imagj-j)][0] 
#         imag[-(imagj-j)][0] = current
#         current = temp
#         # if i + 2 == imagi and j + 2 == imagj:
#         #   print('endd')
#         #   return 'end'
#         print('up: ')
#         for img in imag:
#             print(img)
#       # ! THE END. dead code.
#       # else:
#       #   print('end')
#       #   return 0     



# mylist = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# matrix = [[1,2],
#           [3,4]]
# rotate90(mylist)
# print(matrix[1][-2])








# print(matrix)
      # if i + 1 != imagi:
      #   current = imag[i][j]
      #   print(current)  
      #   imag[i][j] = imag[i][j-1]
      #   imag[i][0] = imag[imagi-1][j-1]
      # else:
      #   imag[i][0] = imag[i][imagi - 1]
      #   imag[i][imagi - 1] = current



            # else:
        # # if last in row and there is still row below it then move to the next row and replace last item
        # # print(j + 1 == imagj, imagj, j +1, j)
        # if j + 1 == imagj and i + 1 != imagi: 
        #   print('iffffffff')
        #   # save last of next row
        #   h = imag[i + 1][imagj - 1]
        #   # replace last of next row
        #   imag[i + 1][imagj - 1] = current 
        #   current = h
        #   print(imag)
        # else:
        #   print('elllllllse ')
        #   # if end of row then move to left       
        #   if i + 1 == imagi:
        #     h = imag[i][imagj - j]
        #     imag[i][j + 1] = current
        #     current = h
        #   else:
        #   # else move to the next right item in the same row.
        #     h = imag[i][imagj + 1]
        #     imag[i][j + 1] = current
        #     current = h

    # print("image rotating: ",imag[i])

# permutation:

# def buildArray(nums):
#   newNums = [nums[0]]
#   for i in range(1, len(nums)):
#     newNums.append(nums[nums[i]])
#     print(newNums)
#   return newNums

# [1, 2, 0]
# def buildArray(nums):
#   newNums = [nums[0]]
#   for i in range(1, len(nums)):
#     a = nums[i]
#     print(a)
#     nums[i] = nums[nums[i]]
#     nums[a] = a
#     print(nums)
#   print(nums)

# nums = [0,2,1,5,3,4]
# nums = [2, 0, 1]

# buildArray(nums)

myDict = {}
print(all(myDict))
# myDict.pop('0.1')
# print(myDict.items())
