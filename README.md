### 豆瓣电影内容爬取和图片下载
> 由于豆瓣电影的数据都是ajax请求获得，是动态数据无法直接爬取，所以有两种方式可以爬取。

> 使用技术：scrapy + selenium
- 直接请求其服务器：适合于url地址并没有加密，url地址也没有过多的处理的情况
- 使用selenium来获取html页面，从而使用xpath来爬取页面数据
- 本实例主要实现了使用selenium，因为直接请求数据库较为简单
---
- 几个重要的点
    - chrome浏览器驱动设置为无界面
    ```
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    ```
    - 
