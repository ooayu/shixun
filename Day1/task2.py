#第一题
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 只需检查到 √n
        if n % i == 0:
            return False
    return True

print("\n1 到 100 之间的素数有：")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")

#第二题
def fibonacci_sequence(n):
    """生成斐波那契数列的前 n 项"""
    sequence = []
    a, b = 1, 1  # 初始化前两项
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # 更新为下一项
    return sequence

# 计算前 20 项
def fibonacci_sequence(n):
    """生成斐波那契数列的前 n 项"""
    sequence = []
    a, b = 1, 1  # 初始化前两项
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # 更新为下一项
    return sequence
fib_sequence = fibonacci_sequence(20)
print("\n\n斐波那契数列的前 20 项是：")
print(fib_sequence)

#第三题
total = 0  # 初始化总和
num = 1    # 从 1 开始遍历
while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1  # 移动到下一个数

print("\n1 到 10000 之间能被 3 或 5 整除但不能被 15 整除的数的和是：", total)