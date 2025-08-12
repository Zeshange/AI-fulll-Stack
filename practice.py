# student_info=['zeshan',30,3.20,True,[60,50,90]]


# student_info.append('abdul jabbar')

# # print(student_info)
# student_info.insert(2,1995)
# del student_info[0]
# for x in student_info:
#     print(x)

# print(type(student_info))
# print(type(student_info[1]))

# student_info[1]=55
# print(student_info)

# tup=('zeshan',30,3.20,True,[60,50,90])
# print(tup)

# print(type(tup))
# print(type(tup[1]))


# s={20,40,"zeeshan"}
# print(s)

# print(type(s))

# s.add(90)
# print(s)
# # s.discard(1)
# print(s)


# d={'name':'zeeshan','age':30}
# print(d)

# d['marks']=90
# print(d)


# drop nan data------------------------------------
import pandas as pd
df=pd.read_csv('RealEstate-USA.csv')
import seaborn as sas
import matplotlib.pyplot as plt
dataFrame=pd.DataFrame(df)


print(dataFrame.shape)

# print((dataFrame.isnull().sum()/dataFrame.shape[0])*100)

# print("total empty cells :",dataFrame.isnull().sum().sum())
# print("total empty cells % age :",round((dataFrame.isnull().sum().sum())/(dataFrame.shape[0]*dataFrame.shape[1])*100,2))
# print("total cells in data frame :",dataFrame.shape[0]*dataFrame.shape[1])

# print("total non empty cells :",(dataFrame.shape[0]*dataFrame.shape[1])-(dataFrame.isnull().sum().sum()))
 
# sas.heatmap(dataFrame.isnull())
# plt.show()

# dataFrame=dataFrame.drop(columns=['prev_sold_date'])
# print(dataFrame)

# sas.heatmap(dataFrame.isnull())
# plt.show()

# # handling nan values by filling  

# dataFrame=dataFrame.fillna(0)    # it is not a good way to fill we should fill accourding dtype
# sas.heatmap(dataFrame.isnull())
# plt.show()

# filling  data by forward_fill and backword_fill

# dataFrame=dataFrame.fillna(method='bfill') 
# dataFrame=dataFrame.fillna(method='ffill') 

# fill categorical nan values by mode

# print(dataFrame.info())
print(dataFrame['city'].mode()[0])    #getting mode

# print(dataFrame['city'].fillna(dataFrame['city'].mode()[0],inplace=True))

# print(dataFrame.select_dtypes(include='object').columns)

# for i in dataFrame.select_dtypes(include='object').columns:   # it will fill alll null values in categoricall data with its mode
#     dataFrame[i].fillna(dataFrame[i].mode()[0], inplace=True)


# print(dataFrame.head(50))




# order priority check karna
# low high medium

dataFrame['orderpriority'].value_counts()

# unique function 
dataFrame['orderpriority'].unique()

# replace function

dataFrame['orderpriority'].replace('category ','category')


# show figure for order priority

plt.figure(figsize=(5,3))
sas.countplot(x='order priority',data=dataFrame)
plt.title("count of order priority")
plt.savefig("count of order priority.jpg")
plt.show()


dataFrame['shipmode'].value_counts()
x=dataFrame['shipmode'].value_counts().index      # all colums heading
y=dataFrame['shipmode'].value_counts().values      # all colums data  without heading



plt.pie(y ,labels=x ,startangle=60, autopct='%0.2f%%')
plt.legend(loc=2)
plt.show()










