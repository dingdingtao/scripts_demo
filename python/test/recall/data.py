'''
Author: dingdingtao
Date: 2021-04-01 14:38:29
LastEditTime: 2021-04-01 15:16:21
LastEditors: dingdingtao
Description: 
'''
import os

CURRENT_PATH = os.path.dirname(__file__)

def run():
    d = ''
    with open(os.path.join(CURRENT_PATH,'data.txt'),'r',encoding='utf-8') as f:
        d = f.read()
    f.close()

    r = """
            import requests,random\
            from bs4 import BeautifulSoup\
            \
            #获得静态的界面\
            def get_static_html(site_url):\
                print('开始加载', site_url, '静态页面')\
                headers_list = [\
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',\
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 ',\
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',\
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'\
                ]\
                headers = {\
                    'user-agent': headers_list[random.randint(0,len(headers_list))-1],\
                    'Connection': 'keep - alive'\
                }\
                try:\
                    resp = requests.get(site_url, headers=headers)\
                except Exception as inst:\
                    print(inst)\
                    requests.packages.urllib3.disable_warnings()\
                    resp = requests.get(site_url, headers=headers,verify=False)\
                soup = BeautifulSoup(resp.text, 'html.parser')\
                return soup\
            \
            \
            \
            if __name__ == '__main__':\
                #谷歌在线表格链接，需要保证你的链接所有人可见\
                url = 'https://docs.google.com/spreadsheets/d/1OLLuQMeX6Ghz4QOTnY4vMS2g6DYK-lQM_3IZ8C7MvkM/edit#gid=0'\
                #开始一系列的处理\
                soup = get_static_html(url)\
                tab_tr_arr = soup.find_all('tr')\
                for tab_tr in tab_tr_arr:\
                    content = []\
                    s0_tr_th_arr = tab_tr.select('.s0')\
                    s1_tr_th_arr = tab_tr.select('.s1')\
                    if len(s0_tr_th_arr) != 0:\
                        for tr_th in s0_tr_th_arr:\
                            content.append(tr_th.text)\
                    if len(s1_tr_th_arr) != 0:\
                        for tr_th in s1_tr_th_arr:\
                            img_src = tr_th.select_one('img').attrs['src']\
                            content.append(img_src.split('=')[0])\
                    #输出每行的数据\
                    if len(content) != 0:\
                        print(content)"""

    print(exec(r))


if __name__ == '__main__':
    run()