# #list----------------
# print("Creating list")
# lst=[1,3.3,"list"]
# print(lst)

# print(type(lst))

# print("Ending list")

# #tuple----------------

# print("Creating Tuple")
# tup=(1,3.3,"tuple")
# print(type(tup))
# print(tup)

# print("Ending Tuple")


# #set-------------

# print("Creating Set")
# stt={1,2.2,"set"}

# print(type(stt))
# print(stt)

# print("Ending Set")




import numpy as np
a=np.array([1,2,3,4,5])
print(a)


address,city,country,latitude,longitude,name= np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(0,1,2,4,5,6), unpack=True, dtype=None,skip_header=1)
# print(address)
# print(city)
# print(country)
print(latitude)
print(longitude)
# print(name)

add=np.add(latitude,longitude)
print(add)