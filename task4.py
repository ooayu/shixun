# 1.
s1 = "Python is a powerful programming language"
words = s1.split()  # 默认按空格分割成列表
last_word = words[-1]  # 取最后一个元素
print(last_word)  # 输出: language

s2 = "Let's learn together"
combined = s1 + " " + s2  # 合并两个字符串（中间加空格）
print((combined + "\n") * 3)  # 加换行符并重复 3 次

words = s1.split()
p_words = [word for word in words if word.lower().startswith('p')]
print(p_words)  # 输出: ['powerful', 'programming']