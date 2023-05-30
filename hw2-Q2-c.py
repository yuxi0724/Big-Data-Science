import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('hw1.csv', encoding='big5', thousands=',')
data['日期'] = pd.to_datetime(data['日期'])
data.set_index('日期', inplace=True)
data = data.apply(pd.to_numeric, errors='coerce')

daily_total = data.sum(axis=1)

area_proportions = pd.Series({'台北市': 0.27, '新北市': 2.05, '基隆市': 0.13, '宜蘭縣': 2.14, '桃園市': 1.22, '新竹市': 0.10,
                              '新竹縣': 1.42, '苗栗縣': 1.82, '台中市': 2.21, '彰化縣': 1.07, '南投縣': 4.10, '雲林縣': 1.29,
                              '嘉義市': 0.06, '嘉義縣': 1.90, '台南市': 2.19, '高雄市': 2.95, '屏東縣': 2.77, '花蓮縣': 4.62,
                              '台東縣': 3.51, '連江縣': 0.02, '金門縣': 0.15})

for day in range(len(daily_total)):
    if daily_total[day] == max(daily_total):
        label = data.loc[data.index[day]]  # 該日期的各縣市的數值

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        ax2=ax1.twinx()
        ins1=ax1.plot(data.loc[data.index[day]], marker='o', markersize=5, label='確診人數',color='red')
        ax1.set_xlabel("縣市")
        ax1.set_xticklabels(label.index, rotation=90)
        ax1.set_ylabel("確診人數")

        ins2=ax2.plot(area_proportions.index, area_proportions , label='面積',color='green')
        ax2.set_ylabel("面積")
       
        ins=ins1+ins2
        labs = [l.get_label() for l in ins]
        ax1.legend(ins, labs, loc="best")

        ax1.set_title("縣市確診人數 vs 縣市面積 (" + str(data.index[day].date()) + ")")
        # 圓餅圖
        ax3 = plt.subplot(1, 2, 2, aspect='equal')
        ax3.pie(label, autopct='%1.1f%%')
        ax3.set_title(str(data.index[day].date()) + "確診分布")
        ax3.legend(label.index, loc="best")