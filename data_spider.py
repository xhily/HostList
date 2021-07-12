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
    fname = os.getcwd()+"\\json\\" +"weibo.json"
    weibo_ssrd = "https://s.weibo.com/top/summary?cate=realtimehot"
    weibo = "https://s.weibo.com"
    r = requests.get(weibo_ssrd)
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
    fname = os.getcwd() + "\\json\\" + "baidu.json"
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
    fname = os.getcwd() + "\\json\\" + "toutiao.json"
    url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    news = data['data']
    str_list = ""
    for i in news:
        title = i["Title"]
        url = i["Url"]
        str_list = str_list + str1 + title + str2 + url + str3 + "\n"
    with open(fname,"w+",encoding='utf-8') as f:
        f.write(str_list)

#神马搜索榜单
def shenma():
    fname = os.getcwd() + "\\json\\" + "shenma.json"
    shenmahot = "https://m.sm.cn/s?q=%E7%A5%9E%E9%A9%AC%E6%96%B0%E9%97%BB%E6%A6%9C%E5%8D%95&ext=request_smbd_channel%3Asm_index&from=smor"
    r = requests.get(shenmahot)
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

# #央视新闻榜单
# def cctv_news():
#     fname = os.getcwd() + "\\json\\" + "cctv.json"
#     cctvhot = "https://news.cctv.com/"
#     r = requests.get(cctvhot)
#     soup = etree.HTML(r.text)
#     str_list = ""
#     for soup_a in soup.xpath("//*[@id='newslist']/li/div/h3[@class='title']/a"):
#         cctv_name = soup_a.text
#         cctv_url = soup_a.get('href')
#         str_list = str_list + str1 + cctv_name + str2 + cctv_url + str3 + "\n"
#     with open(fname,"w+",encoding='utf-8') as f:
#         f.write(str_list)

#知乎热搜榜
def zhihu():
    fname = os.getcwd() + "\\json\\" + "zhihu.json"
    zhihurl = "https://api.zhihu.com/topstory/hot-lists/total?limit=10"
    response = urllib.request.urlopen(zhihurl)
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
def chinanews():
    fname = os.getcwd() + "\\json\\" + "chinanews.json"
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
    fname = os.getcwd() + "\\json\\" + "weixinnews.json"
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
    while True:
        try:
            baidu_hot()
            parse_weibo()
            jr_toutiao()
            shenma()
            weixinnew()
            chinanews()
        except:
            print("采集出现一个错误，请及时更新规则！")
        time.sleep(600) #每隔600秒也即十分钟更新一次
