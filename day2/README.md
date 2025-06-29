# Python学习笔记
## python基础知识
- 导入模块
```
import rectangle  #导入rectangle.py
from rectangle import calculate_area  #导入特定函数
```
- 类和继承
```
class Cars:  #父类Cars
    def __init__(self,name):
    def speak(self):
        pass   #抽象方法，由子类实现

class ElectricCar(Cars):
    def charge(self):
        return
```
-文件操作
```
with open(text_file, "r", encoding="utf-8") as f:   #读取文件
            new_names = [line.strip() for line in f if line.strip()]  #跳过空行
```
--异常处理
   -try-except-finally
___
### *numpy* 的用法
#### 1.数组的构建
```
import numpy as np
array = np.array([1,2,3])
arr = np.arange(1:7).reshape(2,3)
```

#### 2.数组的索引
>array[:,1]
>array[1,2]
>array[1:,2]

布尔索引
```
array = np.array([19,9,12,16,17])
mask = array >15  # mask = [True,False,False,True,True]
print("大于15的元素：",array[mask])

mask2 = (array > 6) & (array < 17)   #多条件筛选
print("大于6小于17的元素：",array[mask2])
```

#### 3.数组的运算
```
np.dot(a,b)  #点积
a * b   #逐个乘
a @ b   #矩阵乘法
```

>向量的**点积**：定义两个长度相同的向量 **u**=(*u1,u2,...un*)  **v**=(*v1,v2,...vn*)，则点积为：
        **u·v** = *u1v1 + u2v2 +... + unvn = ∑uivi*


#### 4.数组拼接与分割
```
np.vstack((a,b))  #垂直拼接
np.hstack((a,b))  #水平拼接
np.split(arr,2,axis=1)  # axis=1垂直分割
```

- ### 附：
 ```
#实现特定排序规则
def convert(text):
        if text.isdigit():
            num_val = int(text)
            # 如果是以0开头的数字，返回一个特殊的元组使其排在普通数字之前
            if text.startswith('0') and len(text) > 1:
                return (num_val - 0.5, text)
            return (num_val, text)
        return text.lower()
 ```