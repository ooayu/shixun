import requests
import re
import time
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://movie.douban.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9'
    }
def get_douban_top10():
    url = "https://movie.douban.com/chart"
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功
    response.encoding = 'utf-8'  # 豆瓣使用utf-8编码
        
    html_content = response.text
    movies = []
        
        # 使用正则表达式提取电影信息（前10名）
        # 匹配电影名称、链接、评分、评价人数
    pattern = re.compile(
        r'<a href="(https://movie.douban.com/subject/\d+/)" class="">\s*(.*?)\s*</a>.*?<span class="rating_nums">(.*?)</span>.*?<span class="pl">\((\d+)\)</span>',
        re.S  # 让 `.` 匹配换行符
        )
        
    matches = pattern.findall(html_content)
        
    for i, match in enumerate(matches[:10], 1):
        link, name, rating, votes = match
        name = name.replace('\n', '').replace(' ', '').split('/')[0].strip()  # 清理名称
            
        movies.append({
                '排名': i,
                '电影名称': name,
                '评分': rating,
                '评价人数': votes,
                '链接': link
            })
        
    return movies
    

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