import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy import stats
from hampel import hampel

#Reading in the CSV
csv = pd.read_csv("recent_datadownload_ab.csv")

csv['date'] = pd.to_datetime(csv['date'])

df = pd.DataFrame(csv)

dfSeries = pd.Series(df['bear'].values)

outliersremoved = hampel(dfSeries, window_size=2, n_sigma=10.0)

date = []
bear = []
print("Outlier indices:")
for i in outliersremoved.outlier_indices:
    print(df['date'][i])
    date.append(df['date'][i])

    print(df['bear'][i])
    bear.append(df['bear'][i])

data_cleaned = outliersremoved.filtered_data


plt.figure(figsize=(18, 6))

plt.plot(df['date'], df['bear'], color="red")
plt.plot(df['date'], data_cleaned, color='blue')
plt.scatter(date, bear)

print(data_cleaned)


plt.show()


#dropping all columns not of wl

dfWells = df.drop('date', axis=1)
dfWells = dfWells.drop('id', axis=1)

'''for col in dfWells.columns:
    dfWells[col] = dfWells[col][dfWells[col] <= ceiling & dfWells[col][dfWells[col] >= floor]]'''

############GRAPH############
'''
#Setting up the graph 

plt.figure(figsize=(18, 6))

for col in dfWells.columns:
    color = (np.random.random(), np.random.random(), np.random.random())

    plt.plot(df['date'], dfWells[col], c=color, label=col)

plt.xlim(df['date'][0], df['date'][len(df) - 1])

plt.subplots_adjust(bottom=0.4)
plt.legend(loc='upper center', bbox_to_anchor=(.5, -.2), ncol=3)

plt.title("Angola Bay WL (" + str(df['date'][0]) + " - " + str(df['date'][len(df) - 1]) + ")", fontweight='bold')
plt.xlabel("Date", fontweight='bold')
plt.ylabel("Elevation (ft)", fontweight='bold')

plt.show()'''


