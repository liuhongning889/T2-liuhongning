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
        'User-Agent': random.choice(user_agent_list),
        "'Referer": "http://scm.xesv5.com/"
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