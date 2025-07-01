from matplotlib import pyplot as plt
import numpy as np
# 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
 
# 金牌个数
gold_medal = np.array([16, 12, 9, 8, 8])
 
# 银牌个数
silver_medal = np.array([8, 10, 4, 10, 5])
 
# 铜牌个数
bronze_medal = [13, 5, 2, 7, 5]
 
x = np.arange(len(countries))
# 恢复x轴的坐标值
plt.xticks(x, countries)
 
# 绘图
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold")
plt.bar(x, silver_medal, width=0.2, color="silver")
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown")
 
# 显示文本标签
# 金牌
# 更正后的循环方式：
for i in range(len(x)):
    plt.text(x[i] - 0.2, gold_medal[i], str(gold_medal[i]),
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i], silver_medal[i], str(silver_medal[i]),
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i] + 0.2, bronze_medal[i], str(bronze_medal[i]),
             va='bottom', ha='center', fontsize=8)
 
# 由于原代码在文本标签循环中存在错误，上述已更正为使用range(len(x))进行遍历，并将奖牌数转换为字符串显示
plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False
# 显示图形
plt.show()