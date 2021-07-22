# -*- coding:utf-8 -*-
import os
import time
import requests
import urllib.request
import json
from urllib import parse
from lxml import etree

str1 ='''{"name":"'''
str2 ='''","url": "'''
str3 ='''"},'''
try:
    os.mkdir("json")
except:
    print("json文件夹已经存在！")


#微博热点排行榜
def parse_weibo():
    fname = "weibo.json"
    weibo_ssrd = "https://s.weibo.com/top/summary?cate=realtimehot"
    weibo = "https://s.weibo.com"
    zhihu_all = "https://www.zhihu.com/hot"
    headers = {'user-agent':'Baiduspider',
               'cookie':'_s_tentry=-; Apache=3536830018100.7607.1626435767316; SINAGLOBAL=3536830018100.7607.1626435767316; ULV=1626435767321:1:1:1:3536830018100.7607.1626435767316:'          
    }
    r = requests.get(weibo_ssrd,headers = headers)
    r.encoding='utf-8'
    soup = etree.HTML(r.text)
    str_list=""
    for soup_a in soup.xpath("//td[@class='td-02']/a"):
        wb_title = soup_a.text
        wb_url = weibo + soup_a.get('href')
        #过滤微博的广告，做个判断
        if "javascript:void(0)" in wb_url:
            str_list = str_list
        else:
            str_list = str_list + str1 + wb_title + str2+ wb_url+ str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#百度热度榜单
def baidu_hot():
    fname = "baidu.json"
    baiduhot = "https://top.baidu.com/board?tab=realtime"
    r = requests.get(baiduhot)
    soup = etree.HTML(r.text)
    str_list = ""
    for soup_a in soup.xpath("//div[@class='container-bg_lQ801']/div[2]/div/div[@class='content_1YWBm']/a"):
        hot_name = soup_a.text
        hot_url = soup_a.get('href')
        str_list = str_list + str1 + hot_name + str2 + hot_url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#今日头条榜单
def jr_toutiao():
    fname = "toutiao.json"
    url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    news = data['data']
    str_list = ""
    for i in news:
        title = i["Title"].replace('"', "'")
        url = i["Url"]
        str_list = str_list + str1 + title + str2 + url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#神马搜索榜单
def shenma():
    fname = "shenma.json"
    shenmahot = "https://m.sm.cn/s?q=%E7%A5%9E%E9%A9%AC%E6%96%B0%E9%97%BB%E6%A6%9C%E5%8D%95&ext=request_smbd_channel%3Asm_index&from=smor"
    headers = {'user-agent':'Mozilla/5.0 (Linux; Android 8.0; MI 6 Build/OPR1-wesley_iui-19.01.24; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044408 Mobile Safari/537.36 MMWEBID/1394 MicroMessenger/7.0.3.1400(0x27000334) Process/tools NetType/WIFI Language/zh_CN',
               'cookie':'cna=Nl94Gejb2VcCAaZvBGQys15b; isg=BDEx7Oeq9THOcFkl8sQY-IiFQL3LHqWQsuxkpxNGLfgXOlGMW261YN9IWshc6T3I; l=eBrur1pIjtc3sHP9BOfanurza77OSIRYYuPzaNbMiOCP_Q1B53tNB6TfMwY6C3GRh6kWR35v8Wk8BeYBqQAonxvOySKKKvDmn; tfstk=cOGVB7blbId2AoN6pSNN5uvZSd3AwUinbTzbnY6LwginOrfD1GUkberzVOdTn'          
    }
    r = requests.get(shenmahot,headers=headers)
    soup = etree.HTML(r.text)
    str_list = ""
    for soup_a in soup.xpath("//*[@id='sc_news_top_list_lg_1_1']/div/a/div/span/span"):
        hot_name = soup_a.text
        hot_name_z = hot_name.replace('"', "'")
        url_name = parse.quote(hot_name)
        hot_url = "https://quark.sm.cn/s?q=" + url_name
        str_list = str_list + str1 + hot_name_z + str2 + hot_url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)



#知乎热搜榜
def zhihu():
    fname = "zhihu.json"
    zhihurl = "https://api.zhihu.com/topstory/hot-lists/total?limit=10"
    response = urllib.request.urlopen(zhihurl,proxies={'http':'42.57.151.71:9999'})
    data = json.loads(response.read())
    zhihudata = data['data']
    str_list = ""
    for i in zhihudata:
        zhihuhot = i['target']
        title = zhihuhot['title']
        url = zhihuhot['url'].replace("https://api.zhihu.com/questions", "https://www.zhihu.com/question")
        str_list = str_list + str1 + title + str2 + url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#中国新闻网
def chinanew():
    fname = "chinanews.json"
    chinanews = "https://www.chinanews.com/scroll-news/news1.html"
    r = requests.get(chinanews)
    r.encoding = 'utf-8'
    soup = etree.HTML(r.text)
    str_list = ""
    for soup_a in soup.xpath("//*[@id='content_right']/div/ul/li/div[@class='dd_bt']/a"):
        chinanews_name = soup_a.text
        chinanews_url = soup_a.get('href')
        str_list = str_list + str1 + chinanews_name + str2 + chinanews_url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#微信热门文章
def weixinnew():
    fname ="weixinnews.json"
    weixinnews = "https://weixin.sogou.com/"
    r = requests.get(weixinnews)
    r.encoding = 'utf-8'
    soup = etree.HTML(r.text)
    str_list = ""
    for soup_a in soup.xpath("//*[@id='pc_0_0']/li/div/h3/a"):
        weixinnews_name = soup_a.text
        weixinnews_url = soup_a.get('href')
        str_list = str_list + str1 + weixinnews_name + str2 + weixinnews_url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

if __name__ == "__main__":
    baidu_hot()
    parse_weibo()
    jr_toutiao()
    shenma()
    weixinnew()
    chinanew()
