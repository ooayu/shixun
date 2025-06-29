# rectangle.py

def calculate_area(length, width):
    """
    计算矩形的面积
    
    参数:
        length (float): 矩形的长度
        width (float): 矩形的宽度
        
    返回:
        float: 矩形的面积
    """
    return length * width

def calculate_perimeter(length, width):
    """
    计算矩形的周长
    
    参数:
        length (float): 矩形的长度
        width (float): 矩形的宽度
        
    返回:
        float: 矩形的周长
    """
    return 2 * (length + width)