# 1.
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print("1-100 的所有偶数：", even_numbers)

# 2.
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
my_list = [3, 1, 2, 1, 4, 2, 5, 3]
result = remove_duplicates(my_list)
print("\n",result)  # 输出: [3, 1, 2, 4, 5]

# 3.
keys = ["a", "b", "c"]
values = [1, 2, 3]
# 使用 zip() 合并键值对，并用 dict() 转换为字典
result_dict = dict(zip(keys, values))
print("\n",result_dict)  # 输出: {'a': 1, 'b': 2, 'c': 3}

# 4.
# 定义元组存储学生信息（姓名, 年龄, 成绩）
student = ("张三", 20, 95.5)
# 解包元组
name, age, score = student
print("姓名:", name)
print("年龄:", age)
print("成绩:", score)