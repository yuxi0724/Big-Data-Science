import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('hw1.csv', encoding='big5', thousands=',')
data['日期'] = pd.to_datetime(data['日期'])
data.set_index('日期', inplace=True)
data = data.apply(pd.to_numeric, errors='coerce')

daily_total = data.sum(axis=1)

fig, ax = plt.subplots()
ax.plot(daily_total.index, daily_total)

date_formatter = DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_formatter)

plt.xticks(rotation=90, ha='center')  

sns.set_style("darkgrid", {"axes.axisbelow": False})

plt.show()