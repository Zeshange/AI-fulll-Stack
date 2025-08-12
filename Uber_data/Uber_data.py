import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file = pd.read_csv('Uber_data\\UberDataset.csv', delimiter=",")

df=pd.DataFrame(file)
# print(df.info())

# handling missing values----------------------
# print(df.isnull().sum())            # it show the total null values in every columns

# df['PURPOSE'].fillna('NOT',inplace=True)    #   fill null values of purpose column with NOT
# print(df.isnull().sum())

# removing all row containing nan
# df.dropna(inplace=True)
# # changing start date and end date formate  object to dateTime

# df['START_DATE']=pd.to_datetime(df['START_DATE'],errors='coerce')
# df['END_DATE']=pd.to_datetime(df['END_DATE'],errors='coerce')
# print(df.info())

# print(df.isnull().sum())


# # seperating date and time by creating seperate columns 
# df['date']=pd.DatetimeIndex(df['START_DATE']).date
# df['time']=pd.DatetimeIndex(df['START_DATE']).hour
# print(df.info())


# # converting hours into category like morning,afternoon,evening,night

# df['day_night']=pd.cut(x=df['time'],bins=[0,10,15,19,24],labels=['morning','afternoon','evening','night'])
# print(df.info())
# print(df.head())
# print(df.shape)

# # data visualization 
# print(df['CATEGORY'].value_counts())
# plt.figure(figsize=(3,3))

# sns.countplot(x='CATEGORY' ,data=df)
# plt.show()


# print(df['PURPOSE'].value_counts())
# plt.figure(figsize=(6,3))


# sns.countplot(x='PURPOSE' ,data=df)
# plt.title("purpose to use Uber")
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()



# print(df['day_night'].value_counts())
# plt.figure(figsize=(4,3))


# sns.countplot(x='day_night' ,data=df)
# plt.title("Time to use Uber d ")
# # plt.xticks(rotation=90)
# # plt.tight_layout()
# plt.show()




# line plot
    # hue
    # palette
    # markers
# bar plot
    # order paramater ['one','two']
    # color   same color to all bars
    # palette     for different collors for bar category using hue
    # hue_order
    # saturation     for color adjust    (0 to 1)

# displot
    # bins[10,20,30]
    # kde=True,false



#     seaborn.lineplot() – Complete Explanation with Examples
# The seaborn.lineplot() function is used to draw a line chart,
#  which is great for visualizing trends over a continuous variable,
#  typically time series or any kind of continuous x-axis.

# 📉 Real-World Use Case:
# Line plots are ideal for:

# Stock price over time

# Temperature over a week

# Sales across quarters

# Growth of website traffic

# What It Is
# countplot() is used to show the count (frequency) of each category in a categorical feature.

# ✅ It’s the bar plot version for categorical data — showing how many times each category appears in a column.
# sns.countplot(x='column_name', data=df)
# plt.show()


# ✅ Use Cases:
# Count how many observations are in each category

# Compare category distributions

# Explore class imbalance (e.g., in classification tasks)

# Parameter	Description
# x / y	Column to plot (use x for vertical, y for horizontal)
# data	The DataFrame
# hue	Separate bars by another category
# order	Custom order of categories
# hue_order	Custom order of hue categories
# palette	Color scheme
# color	Same color for all bars
# saturation	Brightness of color (0–1)
# dodge	Separate bars for hue (True/False)


# What is a Pie Chart (Pie Plot)?
# A pie chart is a circular chart divided into slices to illustrate numerical proportions. Each slice represents a category, and its size shows the percentage (or proportion) of that category.

# ✅ Best Use Cases:
# Showing part-to-whole relationships

# Comparing percentages

# Displaying market share, survey results, etc.

# Simple data with a few categories

# ⚠️ Not ideal for too many categories or for detailed comparisons. Use bar plots or donut charts instead in such cases.

# 📌 Pie Plot Using Matplotlib (since Seaborn doesn’t support it natively)
# python
# Copy
# Edit
# import matplotlib.pyplot as plt

# labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
# sizes = [30, 25, 20, 25]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.title("Fruit Distribution")
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
# 🧠 Parameters Explained:
# Parameter	Description
# sizes	Values for each slice
# labels	Names for each category
# autopct	Display percentage on slices (e.g., '%1.1f%%')
# startangle	Rotates the start of the pie chart
# colors	List of custom colors
# explode	"Pops out" slices to highlight them
# shadow	Adds shadow effect
# radius	Size of the pie

