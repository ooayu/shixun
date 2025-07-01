import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv('D:\\数据\jupyter\\实训\\一线城市2015-2017经济数据.csv')  # 替换为你的CSV文件路径

# 提取城市列表（去重）
cities = data['地区'].unique()
 
# 提取各年份的GDP数据
gdp_2015 = []
gdp_2016 = []
gdp_2017 = []
 
for city in cities:
    # 筛选特定城市和年份的数据
    data_2015 = data[(data['地区'] == city) & (data['年份'] == 2015)]
    data_2016 = data[(data['地区'] == city) & (data['年份'] == 2016)]
    data_2017 = data[(data['地区'] == city) & (data['年份'] == 2017)]
    
    # 提取GDP值，假设GDP列名为'GDP'
    gdp_2015.append(data_2015['国内生产总值'].values[0] if not data_2015.empty else 0)
    gdp_2016.append(data_2016['国内生产总值'].values[0] if not data_2016.empty else 0)
    gdp_2017.append(data_2017['国内生产总值'].values[0] if not data_2017.empty else 0)
 
# 绘制2015-2017年各个地区国内生产总值的直方图
x = range(len(cities))  # 横坐标为城市索引
width = 0.25  # 柱状图的宽度

plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12, 6))
plt.bar([i - width for i in x], gdp_2015, width, label='2015年')
plt.bar(x, gdp_2016, width, label='2016年')
plt.bar([i + width for i in x], gdp_2017, width, label='2017年')
 
plt.xlabel('城市')
plt.ylabel('GDP（亿元）')
plt.title('2015-2017年各个地区国内生产总值')
plt.xticks([i for i in x], cities)  # 设置横坐标标签为城市名称
plt.legend()
plt.show()
 
# 绘制2015年各个地区生产总值的饼图
plt.figure(figsize=(8, 8))
plt.pie(gdp_2015, labels=cities, autopct='%1.1f%%', startangle=140)
plt.title('2015年各个地区生产总值占比')
plt.show()

plt.savefig('chengshi.png')