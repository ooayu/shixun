import requests
from bs4 import BeautifulSoup
import time
import random

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://movie.douban.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

def get_douban_top10():
    url = 'https://movie.douban.com/chart'
    
    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = response.apparent_encoding  # 设置正确的编码
        
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到电影列表 - 根据实际网页结构调整选择器
        movies = []
        items = soup.select('.pl2')  # 电影标题的CSS选择器
        
        for i, item in enumerate(items[:10], 1):  # 只取前10个
            # 提取电影名称
            name = item.a.get_text(strip=True).replace('\n', '').replace(' ', '')
            name = name.split('/')[0].strip()  # 处理名称中的额外信息
            
            # 提取详情链接
            link = item.a['href']
            
            # 提取评分（可能在另一个选择器中）
            rating_tag = item.find_next('span', class_='rating_nums')
            rating = rating_tag.get_text(strip=True) if rating_tag else '暂无评分'
            
            # 提取评价人数（可选）
            votes_tag = item.find_next('span', class_='pl')
            votes = votes_tag.get_text(strip=True).replace('(', '').replace(')', '') if votes_tag else '暂无评价人数'
            
            movies.append({
                '排名': i,
                '电影名称': name,
                '评分': rating,
                '评价人数': votes,
                '链接': link
            })
            
        return movies
    
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    except Exception as e:
        print(f"解析出错: {e}")
        return None

if __name__ == '__main__':
    # 添加随机延迟，避免请求过于频繁
    time.sleep(random.uniform(1, 3))
    
    top10_movies = get_douban_top10()
    
    if top10_movies:
        print("豆瓣电影排行榜Top10:")
        print("-" * 60)
        for movie in top10_movies:
            print(f"排名: {movie['排名']}")
            print(f"电影名称: {movie['电影名称']}")
            print(f"评分: {movie['评分']}")
            print(f"评价人数: {movie['评价人数']}")
            print(f"链接: {movie['链接']}")
            print("-" * 60)
    else:
        print("未能获取电影排行榜数据")