#第一题
x = 10
y = "10"
z = True
print(f"变量 x 的值是 {x}, 数据类型是 {type(x)}")
print(f"变量 y 的值是 {y}, 数据类型是 {type(y)}")
print(f"变量 z 的值是 {z}, 数据类型是 {type(z)}")

#第二题
# 定义 π 的值
pi = 3.14
radius = float(input("请输入圆的半径："))
# 计算圆的面积（公式：面积 = π × 半径²）
area = pi * radius ** 2
# 输出结果，保留两位小数
print(f"半径为 {radius} 的圆的面积是: {area:.2f}")

#第三题
s = "5.31"
# 字符串 → 浮点数
f = float(s)
print(f"\n字符串 '{s}' 转换为浮点数: {f} (类型: {type(f)})")
# 浮点数 → 整数
i = int(f)
print(f"浮点数 {f} 转换为整数: {i} (类型: {type(i)})")