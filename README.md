# HostList

修改自https://github.com/dbdoer/hotspot-online源码

![sy.png](https://i.loli.net/2021/07/13/bDGfsIK3Q86nZeC.png)

hotspot-online 不在维护，耗时一天改进下来

演示地址： [https://www.xhily.com/api/hot/](https://www.xhily.com/api/hot/)

数据 Python 每十分钟更新一次数据

数据记录在json文件夹下

接口文件  hotapi.php 会将本地json文件读取并按照需求返回为json格式接口


前端采用Bootstrap4 来展示，用jsonp从远程接口获取数据，来渲染页面。
所以，你可以直接将html拿去做前端，直接填写我的接口地址就行。

###重要
搭建到**linux**下时 需要将data_spider.py 文件放入json下，
修改data_spider.py里**每个**热搜下
fname = os.getcwd()+"\\json\\" +"weibo.json"
改为
fname = "weibo.json"
**windows下一切正常** 


