import numpy as np
price,bed,bath,street,city,state,zip_code,house_size=np.genfromtxt('work\RealEstate_us\RealEstate-USA.csv',delimiter=',',usecols=(2,3,4,6,7,8,9,10),unpack=True, dtype=None,skip_header=(1))

###############################################################
                    # PRINTING ALL FIELDS
###############################################################
# print('PRICE',price[:10])
# print('BED',bed[:10])
# print('BATH',bath[:10])
# print('STREET',street[:10])
# print('CITY',city[:10])
# print('STATE',state[:10])
# print('ZIP CODE',zip_code[:10])
# print('HOUSE_SIZE',house_size[:10])

##################################################################
            # CREATIN 2D ARRAY BY price AND house_size
##################################################################

array_2D=np.array([price,house_size])
print(array_2D[:,:5])          #printing horizontole

array_2D_T=array_2D.T
print(array_2D_T[:5])           #printing vertically

####################################################################
                        # Array attributes---
####################################################################

print("Array Dimensions :",array_2D.ndim) 
        # The number of dimensions of an array is contained in the ndim attribute.

print("Array Shape :",array_2D.shape) 
        # specify the number of elements along each dimension.

print("Array size :",array_2D.size)
        # The fixed, total number of elements in array is contained in the size attribute.

print("Data type :",array_2D.dtype)
        # Arrays are typically “homogeneous”, meaning that they contain elements 
        # of only one “data type”. The data type is recorded in the dtype attribute.


######################################################################
                # 1. Adding Elements to a NumPy Array
######################################################################

prices=price[:5]                #slicing price column first 5 values 
print(np.append(prices,10000))  # appending 10000 at last of the erray

print(np.insert(prices,0,20000)) # inserting value at particular index 

######################################################################
                # 1. Delete Elements to a NumPy Array
######################################################################
print('---deleting----')

prices=price[:5]                #slicing price column first 5 values 
print(prices)
print(np.delete(prices,-1))  # deleting  last index  of the erray

print(np.delete(prices,0))      # deleting particuler index value


######################################################################
                #  Sort Elements to a NumPy Array
######################################################################

print('---sorting----')

prices=price[:5]                #slicing price column first 5 values 
print(prices)
print(np.sort(prices))  # deleting  last index  of the erray

# print(np.delete(prices,0))      # deleting particuler index value


######################################################################
                #  Access Elements to a NumPy Array
######################################################################

print('---Accessing----')

prices=price[:5]                #slicing price column first 5 values 
print(prices)
print("index 2 value :",prices[2])  # accessing value at index 2  //index start from 0 

print("Slicing first element",prices[:1])
print("Slicing last element",prices[-1])
print("Slicing first two element",prices[:2])
print("Slicing first two element",prices[3:])   # starting from index 3 till end of length


######################################################################
                #  Conditionaly Access Elements to a NumPy Array
######################################################################

print("conditionaly accessing")

print(" print values that are less than 80000:",prices[prices < 80000])
print(" print values that are less than and equal to 80000:",prices[prices <= 80000])

even=prices[prices %2 ==0]
print(even)

######################################################################
                #  Reshape NumPy Array
######################################################################

print("converting 1D to 2D")

arr=np.arange(30)
print(arr)
D2=arr.reshape(5,6)
print(D2)

print("converting 2D to 3D")

D3=arr.reshape(3,2,5)
print(D3)

######################################################################
                #  Getting Unique Elements from NumPy Array
######################################################################

print("get only unique elements from an array")

mixedArray=np.array((1,1,1,2,2,3,4,4,4,5,5,6,7,7,7,7,8,9,9))
print(mixedArray)
print(np.unique(mixedArray))

######################################################################
                #  Flip function  NumPy Array
######################################################################
print("flip function")

array2d=np.arange(6).reshape(2,3)
print("original array",array2d)
print("fliped array",np.flip(array2d))    #if we not provide axis reverse rows and columns both
print("flip array with axis=0",np.flip(array2d, axis=0))    #if we  provide axis=0  it reverse rows
print("flip array with axis=1",np.flip(array2d, axis=1))    #if we  provide axis=1  it reverse columns only


######################################################################
                #  Arithmatic functions
######################################################################

headings=np.array(["price","bed","bath","house_size","city","pri * bed"]).T
mul=np.array(price * bed)


arr=np.array([price,bed,bath,house_size,city,mul]).T

print(headings)
print(arr)



######################################################################
                #  Trignomatric functions
######################################################################

headings=np.array(["price","bed","bath","house_size"]).T



arr=np.array([price,bed,bath,house_size]).T
costhita=np.cos(arr)
sinthita=np.sin(arr)
tanthita=np.tan(arr)
print(headings)
print(arr)
print(costhita)
print(sinthita)
print(tanthita)

# copy vs view ?

original_array=np.array([1,2,3,4,5])
copy=original_array.copy()
copy[0]=23
print(original_array)

vew=original_array.view()
vew[0]=55
print(original_array)


# flatten() ?
#  ravel() ?
# return_index argument in np.unique() ?
#  return_counts argument in np.unique() ?
# Broadcasting ?
# np.newaxis ?
#  np.expand_dims ?