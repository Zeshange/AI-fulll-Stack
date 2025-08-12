import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
  
# https://github.com/mwaskom/seaborn-data      seaborn dataset

# days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# temperature=[45,46,50,40,41,45,47,49,30,35,40,41,42,40,30]
# tem_df=pd.DataFrame({"days":days,"temperature":temperature})
# print(tem_df)

# sns.lineplot(x="days",y="temperature",data=tem_df)
# plt.show()

tips_df=sns.load_dataset('tips')
print(tips_df)

sns.lineplot(x="total_bill",y="tip",data=tips_df)
plt.show()