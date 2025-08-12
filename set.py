import pandas as pd
data_file=pd.read_csv('RealEstate-USA.csv')
data_frame=pd.DataFrame(data_file)
print(data_frame)


data_frame = data_frame.drop('prev_sold_date', axis=1)
data_frame=data_frame.dropna()
print(data_frame)
