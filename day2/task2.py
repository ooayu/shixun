class Car:
    def __init__(self, brand, speed=0):
        """
        初始化 Car 类
        
        参数:
            brand (str): 汽车品牌
            speed (int): 初始速度，默认为 0
        """
        self.brand = brand
        self.speed = speed
 
    def accelerate(self, m):
        """
        加速方法：速度增加 m 次，每次增加 10
        
        参数:
            m (int): 加速次数
        """
        for _ in range(m):
            self.speed += 10
            print(f"{self.brand} 加速中... 当前速度: {self.speed} km/h")
 
    def brake(self, n):
        """
        刹车方法：速度减少 n 次，每次减少 10，但速度不低于 0
        
        参数:
            n (int): 刹车次数
        """
        for _ in range(n):
            if self.speed >= 10:
                self.speed -= 10
            else:
                self.speed = 0
            print(f"{self.brand} 刹车中... 当前速度: {self.speed} km/h")
 
    def __str__(self):
        """返回汽车的品牌和当前速度"""
        return f"{self.brand} (当前速度: {self.speed} km/h)"
    

# 创建 Car 类的实例
my_car = Car("Tesla", 20)  # 品牌为 Tesla，初始速度 20 km/h
print("初始状态:", my_car)
# 调用 accelerate() 方法加速 3 次
print("\n加速 3 次:")
my_car.accelerate(3)
# 调用 brake() 方法刹车 2 次
print("\n刹车 2 次:")
my_car.brake(2)
# 再次加速 1 次
print("\n再加速 1 次:")
my_car.accelerate(1)

print("\n最终状态:", my_car)


class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        """
        初始化 ElectricCar 类（继承 Car）
        
        参数:
            brand (str): 汽车品牌
            speed (int): 初始速度，默认为 0
            battery (int): 初始电量（百分比），默认为 50
        """
        super().__init__(brand, speed)  # 调用父类的 __init__
        self.battery = battery  # 新增 battery 属性
 
    def charge(self):
        """
        充电方法：电量增加 20，不超过 100
        """
        self.battery = min(self.battery + 20, 100)
        print(f"{self.brand} 充电中... 当前电量: {self.battery}%")
 
    def __str__(self):
        """返回电动车的品牌、速度和电量"""
        return f"{self.brand} (速度: {self.speed} km/h, 电量: {self.battery}%)"
    
     
# 测试 ElectricCar 类
if __name__ == "__main__":
    # 创建一辆电动车，初始速度 30，电量 40%
    my_electric_car = ElectricCar("Tesla Model S", speed=30, battery=40)
    print("初始状态:", my_electric_car)
 
    # 加速 2 次
    print("\n加速 2 次:")
    my_electric_car.accelerate(2)
 
    # 充电
    print("\n充电:")
    my_electric_car.charge()
 
    # 刹车 1 次
    print("\n刹车 1 次:")
    my_electric_car.brake(1)
 
    # 再次充电（测试电量不超过 100%）
    print("\n再次充电:")
    my_electric_car.charge()  # 40 + 20 = 60
    my_electric_car.charge()  # 60 + 20 = 80
    my_electric_car.charge()  # 80 + 20 = 100
    my_electric_car.charge()  # 100 + 20 → 仍为 100
 
    # 最终状态
    print("\n最终状态:", my_electric_car)