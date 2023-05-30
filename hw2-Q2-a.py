import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('hw1.csv', encoding='big5', thousands=',')
data['日期'] = pd.to_datetime(data['日期'])
data.set_index('日期', inplace=True)
data = data.apply(pd.to_numeric, errors='coerce')

daily_total = data.sum(axis=1)

for day in range(len(daily_total)):
    if daily_total[day] == max(daily_total):
        label= (data.loc[data.index[day]])
        plt.pie(label,autopct='%1.1f%%')
        plt.title(str(daily_total.index[day].date())+"確診分布")
        plt.axis("equal")
        plt.legend(label.index, loc="best")
        break
plt.show()