## Python 爬虫
- ### 网络状态码

    - #### 1xx（信息性状态码）
        100 Continue :服务器已收到请求的初始部分，客户端应继续发送剩余部分
        101 Switch Protocols :服务器统一切换协议

    - #### 2xx（成功状态码）
        200 OK :请求成功
        201 Created :请求成功，并创建了新资源
        204 No content :请求成功，但无返回内容

    - #### 3xx（重定向状态码）
        301 Moved Permanently :资源永久移动到新URL
        302 Found :资源临时移动到新URL
        304 Not Modified :资源未修改，客户端可使用缓存版本

    - #### 4xx（客户端错误状态码）
        400 Bad Request :请求无效
        401 Unauthorized :未认证，需提供凭据
        403 Forbidden :服务器拒绝请求（无权限）
        404 Not Found :请求的资源不存在
        405 Method Not Allowed :请求方法不被允许

    - #### 5xx（服务器错误状态码）
        500 Internal Server Error :服务器内部错误
        502 Bad Gateway :服务器作为网关时收到无效响应
        503 Service Unavailable :服务器暂时不可用

-  ### **requests**
```
rs = requests.get(url)
print(rs.text)  # response对象的text属性获取网页源码
print(rs.status_code)  #状态码
```
-  ### **lxml**
```
from lxml import etree
html = etree.HTML(rs.text)  #用于将 HTML 字符串 解析为一个可操作的 元素树（Element Tree）对象
```

## Pandas

- df = read_csv()
- df.to_csv()

- 时间戳

##### 1.创建
```
ts = pd.Timestamp('2023-11-15')   # format='%Y/%m/%d %H:%M' 指定格式解析
ts = pd.Timestamp(year=2023, month=11, day=15, hour=14, minute=30)   #从时间组件创建
```

##### 2.属性访问
```
ts.year
ts.month
ts.minute
ts.dayofweek   # 周几
```

##### 3.时间偏移
```
# 加 1 天
print(ts + pd.Timedelta(days=1))  # 2023-11-16 00:00:00
```

- 数据合并

>  #### ***merge***
```
merged_df = pd.merge(df1,df2,on='ID', how='inner')  #how='outer'/'left'/'right'
```

>  #### ***concat***
```
concat_df = pd.concat([df1, df3], ignore_index=True)  #垂直拼接
```

#### 总结：
  今天有学习用Python爬取网站的数据，主要困难的地方在于如何处理反爬机制，也做了一个关于爬取文献引用的小小的项目，虽然没有运行成功，但是很有趣的是用模拟人工检索。对于numpy和pandas中dataframe对象的操作方法，关注要操作的对象变量类型，会影响选择处理方法，比如pd.to_csv()处理的是dataframe对象，而不能是dict对象。matplotlib在进行绘图时，有丰富的属性参数可以根据需求进行修改。