# scrapy
最近在入门python，半生不熟用scrapy框架写了个小姐姐站的抓包，踩到几个坑，记录一下。

## 1.下载图片之前调试时先不要配置ImageItem

暂时还没找到原因，不过多次尝试发现，如果提前配置下载图片的相关文件（items.py、setting.py、pipelines.py）就不能再读取css的解析结果了，所以先把解析弄对了，再加下载模块为好。
## 2.下载用到的item函数的输入值是一次性输入一个数组

item函数输入的是一个完整url数组，如果append添加之后立即执行item的yield会将本地图片下了删删了下，严重浪费资源

运行环境：python2.7
