import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fileread = pd.read_csv('activity.csv')
fileread['date'] = pd.to_datetime(fileread['date'])
fileread.info()
fileread.head(10)

fileread['weekday'] = np.where(fileread['date'].dt.dayofweek < 5, 'weekday' , 'weekend' )
fileread.head(1500)

interval_sets = set() # 
for index, row in fileread.iterrows():
    interval_sets.add(row["interval"])

interval_mean_weekday = {}
interval_mean_weekend = {}

for i in sorted(interval_sets):
    interval_mean_weekday.append(fileread.loc[(fileread["interval"] == i) & (fileread["type of day"] == "weekday")]["steps"].mean())
    interval_mean_weekend.append(fileread.loc[(fileread["interval"] == i) & (fileread["type of day"] == "weekend")]["steps"].mean())


plt.plot(sorted(interval_sets), interval_mean_weekday, label="weekday")
plt.plot(sorted(interval_sets), interval_mean_weekend, label="weekend")
plt.legend()
plt.show()