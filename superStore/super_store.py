import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('superStore\\super_store.xlsx', sheet_name='Orders')
# print(df)
print(df.shape)
print(df.head(2))
print(df.columns)

# order priority
print(df['Order Priority'].value_counts())
df['Order Priority'].replace('Critical ','Critical',inplace=True)
print(df['Order Priority'].unique())

# plt.figure(figsize=(5,3))
# sns.countplot(x='Order Priority',data=df)
# plt.title("count of Order Priority")
# # plt.savefig("count of order priority.jpg")
# plt.show()

# # shipping mode
# df['Ship Mode'].value_counts()
# x=df['Ship Mode'].value_counts().index
# y=df['Ship Mode'].value_counts().values

# plt.pie(y ,labels=x ,startangle=60, autopct='%0.2f%%')
# plt.legend(loc=2)
# plt.show()


# customer segment

# plt.figure(figsize=(5,3))
# sns.countplot(x='Customer Segment',data=df)
# plt.title("customer segment")

# plt.show() 


# # product category
# plt.figure(figsize=(5,3))
# sns.countplot(x='Product Category',data=df)
# plt.title("product category")

# plt.show() 

# print(df['Product Category'])

# plt.figure(figsize=(5,3))
# sns.countplot(x='Product Category',data=df[df['Product Category']=='Office Supplies'],hue='Product Sub-Category')
# plt.title("Office Supplies With Sub Category")

# plt.show() 


# plt.figure(figsize=(5,3))
# sns.countplot(x='Product Category',data=df[df['Product Category']=='Technology'],hue='Product Sub-Category')
# plt.title("Technology With Sub Category")

# plt.show() 

# plt.figure(figsize=(5,3))
# sns.countplot(x='Product Category',data=df[df['Product Category']=='Furniture'],hue='Product Sub-Category')
# plt.title("Furniture With Sub Category")

# plt.show() 




# Customer Segment with product category
# plt.figure(figsize=(5,3))
# sns.countplot(x='Customer Segment',data=df,hue='Product Category')
# plt.title("Customer Segment with product category")

# plt.show()

# df['years']=df['Order Date'].dt.year

# print(df['years'].value_counts())




# category wisw profit
# plt.figure(figsize=(6,4))
# sns.barplot(x='Product Category',y='Profit',data=df,estimator='sum')
# plt.title("Category wise Profit")
# plt.show()

# print(df['State or Province'].value_counts()[:5])
# # state wise total sale
# plt.figure(figsize=(12,5),dpi=100)
# sns.countplot(x='State or Province',data=df)
# plt.title("state wise sales")

# plt.xticks( rotation=90)
# plt.tight_layout()
# plt.show()
