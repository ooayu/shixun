# Matplotlib 基础应用小结
#### -日期：2025年7月1日

## 一、核心概念
- #### Figure（画布）：所有图表的容器，通过 `plt.figure()` 创建。

- #### Axes（坐标系）：承载具体图表的区域（含坐标轴、标题等），通过 `fig.add_subplot()` 或 `plt.subplots()` 创建。

- #### Axis（坐标轴）：控制数据范围、刻度及标签。

## 二、基本绘图流程

```
import matplotlib.pyplot as plt
fig, ax = plt.subplots()          # 创建画布和坐标系
ax.plot(x, y, label='Line', color='blue', linestyle='--')  # 绘制折线图
ax.set_title("Title")              # 设置标题
ax.set_xlabel("X-axis")            # 设置坐标轴标签
ax.legend()                       # 显示图例
plt.savefig("plot.png")           # 保存图像
plt.show()                        # 显示图像
```

## 三、常用图表类型
- **折线图：** `ax.plot(x, y)`

- **散点图：** `ax.scatter(x, y, s=size, c=color)`

- **柱状图：** `ax.bar(categories, values)`

- **直方图：** `ax.hist(data, bins=10)`

- **饼图：** `ax.pie(sizes, labels=labels, autopct='%1.1f%%')`

## 四、样式定制技巧
- **颜色/线型：** `color='red'、linestyle='dotted'、marker='o'`

- **网格/刻度：** `ax.grid(True)、ax.set_xticks([0,1,2])`

- **多子图布局：**
```
fig, axes = plt.subplots(nrows=2, ncols=2)  # 2x2子图
axes[0,0].plot(x1, y1)                   # 操作左上子图
```

## 五、注意事项
 - 面向对象（OO）风格（直接操作 `ax`）比函数式（`plt.plot()`）更推荐，便于复杂图表控制。

 - 使用 `plt.tight_layout()` 自动调整子图间距，避免重叠。

 - 通过 `plt.style.use('ggplot')` 快速应用主题（如 `seaborn`、`ggplot`）。
___
___
### 总结：
Matplotlib 是 Python 数据可视化的核心工具，掌握画布-坐标系结构、基础图表绘制和样式定制，即可高效创建清晰图表。进阶可结合 Pandas 数据直接绘图，或集成 Seaborn 优化统计图形。


**收获：** 掌握了从数据到可视化图表的完整流程，后续将尝试组合图表和样式优化。

**待探索：** 子图布局、3D绘图、动画功能。