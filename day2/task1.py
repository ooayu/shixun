# 1.
def is_palindrome(x):
    """
    判断一个整数是否为回文数
    """
    # 负数不是回文数
    if x < 0:
        return False
    
    # 将数字转换为字符串，便于比较
    str_x = str(x)
    
    # 比较字符串与其反转是否相同
    return str_x == str_x[::-1]
# 测试示例
print(is_palindrome(121))  # 输出: True
print(is_palindrome(123))  # 输出: False

# 2.
def calculate_average(*args):
    """
    计算任意数量参数的平均值
    
    参数:
        *args: 任意数量的数值参数
        
    返回:
        float: 参数的平均值。如果没有参数，返回 None。
    """
    if not args:  # 如果没有传入参数
        return None
    total = sum(args)
    average = total / len(args)
    return average
# 测试示例
print(calculate_average(1, 2, 3, 4, 5))  # 输出: 3.0
print(calculate_average(10, 20, 30))     # 输出: 20.0
print(calculate_average())               # 输出: None

# 3.
def find_longest_string(*args):
    if not args:
        return None
    return max(args, key=lambda s: len(s))

# 测试示例
print(find_longest_string("apple", "banana", "cherry"))  # 输出: "banana"

# 4.
# 导入 rectangle 模块
import rectangle
 
# 定义矩形的长和宽
length = 5.0
width = 3.0
# 计算面积和周长
area = rectangle.calculate_area(length, width)
perimeter = rectangle.calculate_perimeter(length, width)
# 打印结果
print(f"矩形的长: {length}, 宽: {width}")
print(f"面积: {area}")
print(f"周长: {perimeter}")