# cleanint data set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sas
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) 
file=pd.read_csv('Assignments\week_4\Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',')
df=pd.DataFrame(file)
print(df.head(100))


