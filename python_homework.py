# -*- coding: utf-8 -*-
import requests,random
import json #格式化数据用

user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    ]
headers = {
        {
        'Proxy-Connection' : 'keep-alive',
        'Accept':'application/json, text/plain, */*',
        'User-Agent': random.choice(user_agent_list),
        'Referer': 'http://scm.xesv5.com/',
        'token' : '1832b85ff6bc7d1a321cd27ff9d4abc1',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie' :'Sign=f6c9d31c879d889a737f380c28d07ae4; From-User=xuezhenhua; UM_distinctid=1766a97c004b3a-05008f93baef8f-c791039-144000-1766a97c005bd6; token=eyJhcHBpZCI6IjExMyIsInRva2VuIjoiYTkwYWIzNWZmZmQ1NWM0OTM0ZDlkYjRmZGNmNjYzYjkifQ%3D%3D; pmaUser=%7B%22iv%22%3A%22vgd%2BkishMyrpiZ8KQsMAnQ%3D%3D%22%2C%22mac%22%3A%228d428e35fa0de12a78d3e5390c8f0d594efab774%22%2C%22payload%22%3A%22r6%2Bs7bRcCSJGR3NWrZkm%5C%2Fw%3D%3D%22%7D; pmaAuth=%7B%22iv%22%3A%22%5C%2Fgv8BiLMKwDggUMejuKHOA%3D%3D%22%2C%22mac%22%3A%222915b4ccf8feb0d99163cef01bc00fc2d9678c85%22%2C%22payload%22%3A%22Dv7dBs5r8Ici6fryJBANkVF2g2B91k0Z4I3qNI%5C%2FZmMA%3D%22%7D; wx=d74f2fc6f78f28cdf09dfb6390e1548709yfybbsfm'
    }
def getData(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            content = response.content
            # json格式转为字典
            result = json.loads(content)
            # 获取响应的信息列表
            info = result['data']['list']
            for list in info:
                # 分条写入txt文件
                # print("********", len(info), list, type(list))
                with open('scm.xesv5.com.txt', 'a', encoding='utf-8') as f:
                    f.write(str(list) + '\n')
    except Exception as e:
        with open("error.log", "a", encoding="utf-8") as err:
            err.write(url + '\n')
            err.write(str(e) + '\n')
def getUrl():
    # 构建url，每页20条，获取100条需要5页
    for i in range(1,6): # range(1,6) --> 1,2,3,4,5
        url = "http://erpadmin.xesv5.com/Supply/Course/getCourseList?page=" + str(
            i) + "&limit=20&is_test=0&course_struct_id=1"
        getData(url)



if __name__ == "__main__":
    getUrl()
