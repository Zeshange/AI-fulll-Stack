import pandas as pd
# 1. Load above CVS file above, into DataFrame variable , with Pandas, following columns 
# With default – auto indexing . 
# Print DataFrame. 

file=pd.read_csv('Assignments\week2\RealEstate-USA (1).csv')
df=pd.DataFrame(file)

# 2. Call following method/properties of DataFrame, print output and analyze the output. 
# .info() 
# .dtypes 
# .describe() 
# .shape 
# print(df.head(5))
# print(df.info())
# print(df.dtypes)
# print(df.shape)
# print(df.describe())


# 3. Explore  
# https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/ 
# Use , DataFrame method -  .to_string() 
# Use, debug, trace and play with following paramters. 
# Parameters: 
#  buf: Buffer to write the output string to (e.g., a file). Defaults to None, which means the output 
# is returned as a string. 
#  columns: Specifies a subset of columns to include in the output. If None, all columns are printed. 
#  col_space: Defines the minimum width of each column. 
#  header: Whether to print column names. Can also accept a list of column name aliases. 
#  index: Whether to include index labels. Default is True. 
#  na_rep: String representation for missing values (NaN). Default is ‘NaN’. 
#  formatters: Dictionary or list of functions to apply to columns for formatting their output. 
#  float_format: Formatter function to apply specifically to floating-point numbers. 
#  sparsify: Controls hierarchical index formatting. If False, prints every multi-index key at each 
# row. 
#  index_names: Whether to print index names. Default is True. 
#  justify: Alignment of column headers (‘left’, ‘right’, ‘center’, ‘justify’ or ‘justify-all’). 
#  max_rows: Maximum number of rows to display. If exceeded, truncates output. 
#  max_cols: Maximum number of columns to display. If exceeded, truncates output. 
#  show_dimensions: If True, displays the shape (rows x columns) of the DataFrame. 
#  decimal: Specifies the character for decimal separation (e.g., ‘,’ for European formatting). 
#  line_width: Defines the maximum character width of a row before wrapping text."""





# 4. On given DataFrame – select top 7 rows, and print
# print(df.head(7))

# 5. On given DataFrame – select bottom 9 rows, and print
# print(df.tail(9))


# 6. On Given DataFrame – access the Name column for “city” and print whole column
# Then next, access the name column for “street” and print whole column

# print(df['city'])
# print(df['street'])


# 7. On Given DataFrame – access access multiple columns like “street” and “city”
# Print it.

# print(df[['street','city']])

# 8. Selecting a single row using .loc
# With index value 5 , print the returned row and analyze results

# print(df.loc[5])




# Selecting multiple rows using .loc
# With index – value 3 and 5 , 7 , print the returned rows and analyze results.

# print(df.loc[[3,5,7]])

# 10. Selecting a slice of rows using .loc
# With index – value range of 3 and 9, print the returned row and analyze results.

# print(df.loc[3:9])

# 11. Conditional selection of rows using .loc
# “price” greater then “100000”
# , print the returned row and analyze results.

# print(df.loc[df['price'] > 100000])


# 12. Conditional selection of rows using .loc
# “city” equal to “Adjuntas”
# , print the returned row and analyze results.

# print(df.loc[df['city']== 'Adjuntas'])

# 13. Conditional selection of rows using .loc
# “city” equal to “Adjuntas” and “price” is equal to - less then 180500
# , print the returned row and analyze results

# print(df.loc[(df['city'] == 'Adjuntas')&(df['price'] < 80050)])


# 14. Selecting a single column using .loc
# With index value 7 , only select following columns
# “city”,”price” , ”street” , ” zip_code” , ” acre_lot”
# , print the returned row and analyze results.

# print(df.loc[7,['city','price','street','zip_code']])

# 15. Selecting a slice of columns using .loc
# Form “city” to “zip_code”
# , print the returned row and analyze results.

# print(df.loc[ :,'city':'zip_code'])

# 16. Combined row and column selection using .loc
# “city” equal to “Adjuntas” and Form “city” to “zip_code”
# , print the returned row and analyze results

# print(df.loc[df['city'] == 'Adjuntas','city':'zip_code'])


# 17. Selecting a single row using .iloc
# Select 5th row
# , print the returned row and analyze results.

# print(df.iloc[5])


# 18. Selecting multiple rows using .iloc
# Select – 7
# th row, 9th row and 15th row
# , print the returned row and analyze results


# print(df.iloc[[5,7,9]])


# 19. Selecting a slice of rows using .iloc
# Select from 5th to 13th row
# , print the returned row and analyze results.

# print(df.iloc[5:9])


# 20. Selecting a single column using .iloc
# Select 3rd column
# , print the returned row and analyze results.

# print(df.iloc[ :,2])


# 21. Selecting multiple columns using .iloc
# Select 2nd column, 4th column, 7th columns 
# , print the returned row and analyze results.


# print(df.iloc[:,[3,5,7]])

# 22. Selecting a slice of columns using .iloc
# Range: Select from 2nd column to 5th columns 
# , print the returned row and analyze results.

# print(df.iloc[:,2:5])

# 23. Combined row and column selection using .iloc
# Select – 7
# th row, 9th row and 15th row
# Select 2nd column, 4th column
# , print the returned row and analyze results.

# print(df.iloc[[3,5,7],[2,4]])

# 24. Combined row and column selection using .iloc
# Select range : 2
# nd
#  row, 6
# th row
# Select range : 2
# nd column to 4
# th column
# , print the returned row and analyze results.

# print(df.iloc[[2,6],2:4])

# 25. Add a New Row to a Pandas DataFrame
#  print the returned dataFrame and analyze results.

# new_row=pd.DataFrame([{'price':'40000'}])
# print(new_row)

# df=pd.concat([df,new_row],ignore_index=True)

# print(df.tail(5))


# 26. delete row with index 2
# print the returned dataFrame and analyze results

# df=df.drop(index=2)
# print(df)

# 27. delete row with index from 4 to 7th row
# print the returned dataFrame and analyze results

# df=df.drop(index=range(2,6))
# print(df.head(10))

# 28. Delete “house_size” column
# print the returned dataFrame and analyze results.

# df.drop(columns='house_size',inplace=True)
# print(df.head(5))


# 29. Delete “house_size” and “state” columns
# print the returned dataFrame and analyze results.

# df=df.drop(columns=['house_size','state'])
# print(df)

# 30. Rename column “state” to “state_Changed”
# Print the returned dataFrame and analyze results.

# df.rename(columns={'state':'state_change'},inplace=True)
# print(df)

# 31. Rename label from 3 to 5
# Print the returned dataFrame and analyze results.

# df.rename(index={2: 5}, inplace=True)
# print(df)

# 32. query() to Select Data
# where: "price” < 127400
# “city” not equal to “Adjuntas

# df=df.query('price < 127300 & city != "Adjuntas"' )
# print(df)


# 33. sort DataFrame by price in ascending order column “price

# df=df.sort_values(by="price")
# print(df)



# 34. “group the DataFrame by the “city” column and calculate the sum of “price” for each category
# Print the returned dataFrame and analyze results

# ????/

# 35. use dropna() to remove rows with any missing values
# Print the returned dataFrame and analyze results.

# df.dropna(inplace=True)
# print(df)


# 36. filling NaN values with 0

# df.fillna(0,inplace=True)
# print(df)



