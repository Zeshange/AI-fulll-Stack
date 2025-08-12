import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
# print(np.__version__)

# address,keys,latitude,longitude,name,postalCode = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(0,3,4,5,6,7), unpack=True, dtype=None,skip_header=(1))
# print(address)
# print(keys)
# print(latitude)
# print(longitude)
# print(name)
# print(postalCode)

# print("mean of latitude is: ",np.mean(latitude))
# print("Average of latitude is: ",np.average(latitude))
# print("Std of latitude is: ",np.std(latitude))
# print("median of latitude is: ",np.median(latitude))
# print("min of latitude is: ",np.min(latitude))
# print("max of latitude is: ",np.max(latitude))

# print("square of latitude is: ",np.square(latitude))
# print("sqrt of latitude is: ",np.sqrt(latitude))
# print("sqrt of latitude is: ",np.power(latitude,latitude))
# print("sqrt of latitude is: ",np.abs(latitude))


# print("addition: ",latitude + longitude)
# print("subtraction: ",latitude - longitude)
# print("multiplication: ",latitude * longitude)
# print("divition: ",latitude / longitude)


# latitudePie = (latitude/np.pi) +1
# print("sine",np.sin(latitudePie)) 
# print("cose",np.cos(latitudePie)) 
# print("tan",np.tan(latitudePie)) 




# df = pd.read_csv('FastFoodRestaurants.csv',delimiter=",")
# print(df.head(5))

# # print("df - data types" , df.dtypes)

# print("df.info():   " , df.info() )
# print("Summary of Statistics of DataFrame using describe() method", df.describe())
# print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)



status,price,bed = np.genfromtxt('RealEstate-USA.csv', delimiter=',', usecols=(1,2,3), unpack=True, dtype=None,skip_header=(1))


print(price)
print(bed)

print(np.mean(price))
print(np.min(price))
print(np.max(price))
print(np.average(price))
print(np.square(price))
print(np.power(price,price))
print(np.sign(price))
print(np.tan(price))



df = pd.read_csv('RealEstate-USA.csv',delimiter=",")


print(df)
print(df.head(5))
print(df.describe)
print(df.shape)


data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')

sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show()


sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})


sns.lineplot(x='x', y='y', data=data)
plt.show()
