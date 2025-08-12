import numpy as np

# creating arrays using list or tupple
# 1D Array


# 1D array using list   it look like a list
arr1=np.array([1,2,3,4,5])
# print(arr1)

#1D array using tupple   
arr2=np.array((1,2,3,4,5))
# print(arr2)



# 2D Array   (matrices)  it looks like a table

arr_2D=np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    )
# print(arr_2D)

# 3D array   it look like a sequence of table  repetation of 2d array
# A 3D list is a list of lists of lists — think of it like a cube of numbers,
# or multiple 2D tables stacked on top of each other.

arr_3D=np.array(
    [
        [[1,2,3],[4,5,6]],
        [[7,8,9],[10,11,12]]
        
    ]
    )
# print(arr_3D)



# Accessing Array elements  using indices ---------------indix start with 0 ----------------------------------

# access 1D element
# print(arr1[2])

# access 2D element 

    # [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
    # ]
# print(arr_2D[0][1])  
#     # first index  [0]  identify row and second  index [1] identify col   (access first row second colum)

# print(arr_2D[2][2])  
#     # third row third columns  = 9


# access 3D element 
# [
#         [[1,2,3],[4,5,6]],
#         [[7,8,9],[10,11,12]]
        
# ]
# print(arr_3D[0][0][0])

# 3D array may multipul 2D arrays hote hay  first index [0]  show first 2D array  
# second index [0] show first row in first 2D array  third index [0] show column in firs 2D array
# 1

# print(arr_3D[1][1][2])   
# second 2D second row  third column = 12

# 1D array slicing
print(arr1[:4])    # start say  lesthan 4th index tak
print(arr1[1:4])   # index 1 say  lesthan 4th index tak
print(arr1[:])          #start say end tak
print(arr1[0:])    # 0 index say last tak


# 2D array slicing

#[
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
# ]

print(arr_2D[:,0:1])
# 2d may row and column ki alg alg select kya jata hay , say pehlay ki slicing row kay liyhay and bad ki colom kay liyhay
# all rows first column

# print(arr_2D[:1,0:1])

# first row first column


# 3D row slicing
# [
#         [[1,2,3],[4,5,6]],
#         [[7,8,9],[10,11,12]]
        
# ]

# print(arr_3D[0:1,1:2,:1])


                                # Array attributes------------------------------------
print(arr_3D.ndim) 
        # The number of dimensions of an array is contained in the ndim attribute.
print(arr_3D.shape) 
        # specify the number of elements along each dimension.
print(arr_3D.size)
        # The fixed, total number of elements in array is contained in the size attribute.
print(arr_3D.dtype)
        # Arrays are typically “homogeneous”, meaning that they contain elements 
        # of only one “data type”. The data type is recorded in the dtype attribute.



#         How to create a basic array
# This section covers np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()


print(np.zeros(5))

print(np.ones(5))

print(np.empty(5))

        # You can create an array with a range of elements:
print(np.arange(5))
        # nd even an array that contains a range of evenly spaced intervals. To do this, you will
        # specify the first number, last number, and the step size.
print(np.arange(1,10,2))

        # ou can also use np.linspace() to create an array with values that are spaced linearly in a specified interval:

print(np.linspace(1,10,num=5))


# 1. Adding Elements to a NumPy Array ---------------------------------------------

# append method is used to add at the end of array

print(np.append(arr1,6)) 

print(np.append(arr1,[7,8,9,10]))



# adding new element to 2D array shape must be matcched 
#[
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
# ]
# each row has 3 columns  
print(np.append(arr_2D,[[10,11,12]],axis=0))   

# adding column to shoure each column has 3 rows
print(np.append(arr_2D,[[0],[0],[0]],axis=1))    


# Appending to 3D Arrays – Shape Still Matters!
#
# arr3D = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])  # Shape: (2, 2, 2)
# 2 blocks

# each block = 2 rows × 2 columns

# To append a new 3D block (one full 2x2 block):

# new_block = [[[9, 10], [11, 12]]]  # Shape: (1, 2, 2)
# result = np.append(arr3D, new_block, axis=0)
# print(result.shape)  # (3, 2, 2)


# Delete elements

# delete from 1D array
print(np.delete(arr1,2))   
 
#  delete indes no 2


# delete from 2D array
print(np.delete(arr_2D,0,axis=0))
# it delete first row 

print(np.delete(arr_2D,0,axis=1))
# it delete 1 columns

# delete element from 3D array

#[
#         [[1,2,3],[4,5,6]],
#         [[7,8,9],[10,11,12]]
        
# ]

# print(np.delete(arr_3D,0,axis=0))

# print(np.delete(arr_3D,0,axis=1))
# print(np.delete(arr_3D,0,axis=2))



# sorting Arrays------------------------------------------------
# un_sort_1D=np.array([3,4,2,1,5])
# Sorted_1D=np.sort(un_sort_1D)
# print(Sorted_1D)


unsort_2D=np.array([[3,6,1],[5,4,6]])
# sorted_2D=np.sort(unsort_2D,axis=1)  #  row wise sorted
sorted_2D=np.sort(unsort_2D,axis=0)  #  col wise sorted

print(sorted_2D)


# reshape Array-----------------------------------

# arr.reshape() will give a new shape to an array without changing the data.

arr1=np.arange(1,13)
print(arr1)

reshape=arr1.reshape(4,3)
print(reshape)


# ?????-------------------------------------------------
# np.newaxis, np.expand_dims
# ?????-------------------------------------------------


# You can easily print all of the values in the array that are less than 5.

# print(a[a < 5])
# [1 2 3 4]
# You can also select, for example, numbers that are equal to or greater than 5, and use that condition to index an array.

# five_up = (a >= 5)
# print(a[five_up])
# [ 5  6  7  8  9 10 11 12]
# You can select elements that are divisible by 2:

# divisible_by_2 = a[a%2==0]
# print(divisible_by_2)
# [ 2  4  6  8 10 12]

# Or you can select elements that satisfy two conditions using the & and | operators:

# c = a[(a > 2) & (a < 11)]
# print(c)
# [ 3  4  5  6  7  8  9 10]
# You can also make use of the logical operators & and | in order to return boolean values that specify whether or not the values in an array fulfill a certain condition. This can be useful with arrays that contain names or other categorical values.

# five_up = (a > 5) | (a == 5)
# print(five_up)
# [[False False False False]
#  [ True  True  True  True]
#  [ True  True  True True]]


# How to create an array from existing data

# a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
# You can create a new array from a section of your array any time by specifying where you want to slice your array.

# arr1 = a[3:8]
# arr1
# array([4, 5, 6, 7, 8])

# You can also stack two existing arrays, both vertically and horizontally. Let’s say you have two arrays, a1 and a2:

# a1 = np.array([[1, 1],
#                [2, 2]])

# a2 = np.array([[3, 3],
#                [4, 4]])
# You can stack them vertically with vstack:

# np.vstack((a1, a2))
# array([[1, 1],
#        [2, 2],
#        [3, 3],
#        [4, 4]])
# Or stack them horizontally with hstack:

# np.hstack((a1, a2))
# array([[1, 1, 3, 3],
#        [2, 2, 4, 4]])


# Let’s say you have this array:

# x = np.arange(1, 25).reshape(2, 12)
# x
# array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
#        [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
# If you wanted to split this array into three equally shaped arrays, you would run:

# np.hsplit(x, 3)
#   [array([[ 1,  2,  3,  4],
#          [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
#          [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
#          [21, 22, 23, 24]])]


# Basic array operations

# You can add the arrays together with the plus sign.

# data = np.array([1, 2])
# ones = np.ones(2, dtype=int)
# data + ones
# array([2, 3])
# array.sum()



# Broadcasting-------------------------------------------------??????






# More useful array operations ------------------------------------------------------------
# This section covers maximum, minimum, sum, mean, product, standard deviation, and more

# NumPy also performs aggregation functions. In addition to min, max, and sum, you can easily run mean to get the average, prod to get the result of multiplying the elements together, std to get the standard deviation, and more.

# data.max()
# 2.0
# data.min()
# 1.0
# data.sum()
# 3.0



# How to get unique items and counts --------------------------------------------
# This section covers np.unique()

# You can find the unique elements in an array easily with np.unique.

# For example, if you start with this array:

# a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
# you can use np.unique to print the unique values in your array:

# unique_values = np.unique(a)
# print(unique_values)
# [11 12 13 14 15 16 17 18 19 20]

#  return_index argument in np.unique() ----------------------------------??????/

#  return_counts argument in np.unique()---------------------------------------?????



# If you want to get the unique rows or columns, make sure to pass the axis argument. To find the unique rows, specify axis=0 and for columns, specify axis=1.


# unique_rows = np.unique(a_2d, axis=0)
# print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# To get the unique rows, index position, and occurrence count, you can use:

# unique_rows, indices, occurrence_count = np.unique(
#      a_2d, axis=0, return_counts=True, return_index=True)
# print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# print(indices)
# [0 1 2]
# print(occurrence_count)
# [2 1 1]


# Transposing and reshaping a matrix------------------------------------
# This section covers arr.reshape(), arr.transpose(), arr.T



# How to reverse an array
# This section covers np.flip()

# NumPy’s np.flip() function allows you to flip, or reverse, the contents of an array 
# along an axis. When using np.flip(), specify the array you would like to reverse and the axis.
#  If you don’t specify the axis, NumPy will reverse the contents along all of the axes of your input array.

# Reversing a 1D array

# If you begin with a 1D array like this one:



# This section covers .flatten(), ravel()---------------------------------------?

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# You can reverse it with:

# reversed_arr = np.flip(arr)
# If you want to print your reversed array, you can run:

# print('Reversed Array: ', reversed_arr)
# Reversed Array:  [8 7 6 5 4 3 2 1]
# Reversing a 2D array

# A 2D array works much the same way.

# If you start with this array:

# arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# You can reverse the content in all of the rows and all of the columns with:

# reversed_arr = np.flip(arr_2d)
# print(reversed_arr)
# [[12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]
# You can easily reverse only the rows with:

# reversed_arr_rows = np.flip(arr_2d, axis=0)
# print(reversed_arr_rows)
# [[ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]
# Or reverse only the columns with:

# reversed_arr_columns = np.flip(arr_2d, axis=1)
# print(reversed_arr_columns)
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]]
# You can also reverse the contents of only one column or row. For example, you can reverse the contents of the row at index position 1 (the second row):

# arr_2d[1] = np.flip(arr_2d[1])
# print(arr_2d)
# [[ 1  2  3  4]
#  [ 8  7  6  5]
#  [ 9 10 11 12]]
# You can also reverse the column at index position 1 (the second column):

# arr_2d[:,1] = np.flip(arr_2d[:,1])
# print(arr_2d)
# [[ 1 10  3  4]
#  [ 8  7  6  5]
#  [ 9  2 11 12]]
# Read more about reversing arrays at flip.


#------------------------------?????-----------------------------sir say discuss karnay hay

# flatten()
#  ravel()
# return_index argument in np.unique() 
#  return_counts argument in np.unique()
# Broadcasting
# np.newaxis
#  np.expand_dims