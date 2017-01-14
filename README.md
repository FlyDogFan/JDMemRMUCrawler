# JD Phone Crawler Backup
Merchandise Crawler on JD.com

    京东商品信息爬虫，在手机版访问域名m.jd.com/ 下，爬取手机商品（任意类型商品）的介绍信息和用户评论。
    备注：1.需要调用firefox driver，请添加至相应路径下。详询google；
         2.手机版页面访问时，每个商品的用户评论中，好评、中评和差评只能各拿到310条，即首页10条，再翻页30次；
         3.只有在m.jd.com 下才能够看到每个商品具体的评论数量，jd.com 的数值是约数，不精确。这也是为什么本project是在m.jd.com下做的。
## .py的功能：
    JDcrawler.py实现了商品title、详细介绍列表和好、中、差评内容的搜集。
    JDcrawler_mp.py是对上段程序的make up，因为很简单就不想写到一起了，补充拿到每个商品的好、中、差和有图评论的总条数。
