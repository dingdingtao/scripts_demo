'''
Author: dingdingtao
Date: 2021-03-09 10:17:21
LastEditTime: 2021-04-08 17:31:30
LastEditors: dingdingtao
Description: QQ音乐下载
'''

import requests
import json
import pandas as pd

headers = {
    'Host': 'c.y.qq.com',
    'Referer': 'http://c.y.qq.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 '
    'Safari/537.36 '
}
def douqq_post(mid):
        """
    返回歌曲下载url
    :param mid:歌曲mid
    :return: 字典
    """
        try:
            post_url = 'http://www.douqq.com/qqmusic/qqapi.php'
            data = {'mid': mid}
            res = requests.post(post_url, data=data)
            get_json = json.loads(res.text)
            return eval(get_json)
        except Exception as e:
            return None
 
 
def download_file(src, file_path):
        """
    歌曲下载
    :param src: 下载链接
    :param file_path: 存储路径
    :return: 文件路径
    """
        r = requests.get(src, stream=True)
        f = open(file_path, "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
        return file_path
 
def choice_download(dic):
        # print('1. m4a视频')
        # print('2. mp3普通品质')
        # print('3. mp3高品质')
        # print('4. ape高品无损')
        # print('5. flac无损音频')
        # select = int(input("请输入您的选择:"))
        select = 2
        src = ''
        postfix = ''
        if select == 1:
            src = dic['m4a']
            postfix = '.m4a'
        if select == 2:
            src = dic['mp3_l']
            postfix = '.mp3'
        if select == 3:
            src = dic['mp3_h']
            postfix = '.mp3'
        if select == 4:
            src = dic['ape']
            postfix = '.ape'
        if select == 5:
            src = dic['flac']
            postfix = '.flac'
        return postfix, src.replace('\/\/', '//').replace('\/', '/')
 
def find_song(word,singer):
        """
    查找歌曲
    :param word: 歌曲名
    :return: 返回歌曲mid
    """
        get_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n' \
        '=20&w=' + word
        try:
            res1 = requests.get(get_url, headers=headers)
            get_json = json.loads(res1.text.strip('callback()[]'))
            jsons = get_json['data']['song']['list']
            songmid = []
            media_mid = []
            song_singer = []
            # i = 1
            flag = False
            for song in jsons:
                # print(i, ':' + song['songname'], '---', song['singer'][0]['name'], song['songmid'], song['media_mid'])
                # print(i, ':' + song['songname'], '---', song['singer'][0]['name'])
                if song['songname'] == word and song['singer'][0]['name'] == singer:
                    songmid.append(song['songmid'])
                    # media_mid.append(song['media_mid'])
                    song_singer.append(song['singer'][0]['name'])
                    flag = True
                # i = i + 1
            if flag:
                select = 0
                return songmid[select], song_singer[select]
            else:
                return None, None
        except Exception as e:
            return None, None
 
 
if __name__ == '__main__':
    # songname = '叹云兮'
    datas = pd.read_excel("C:\\Users\\Administrator\\Desktop\\侵权歌单.xlsx",sheet_name="sheet",header=None,names=None,usecols = None)

    dlist = datas.values.tolist()
    print(dlist)

    fail_list = []

    counter = 0
    for music in dlist:
        singer = music[1]
        songname = music[2]
        song_mid, singer = find_song(songname, singer)
        if song_mid == None:
            fail_list.append([songname,singer])
            continue
        dic = douqq_post(song_mid)
        if dic == None:
            fail_list.append([songname,singer])
            continue
        # {
        # "mid":"004FjJo32TISsY",
        # "m4a":"http:\/\/dl.stream.qqmusic.qq.com\/C400004FjJo32TISsY.m4a?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=38",
        # "mp3_l":"http:\/\/dl.stream.qqmusic.qq.com\/M500004FjJo32TISsY.mp3?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
        # "mp3_h":media_mid"http:\/\/dl.stream.qqmusic.qq.com\/M800004FjJo32TISsY.mp3?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
        # "ape":"http:\/\/dl.stream.qqmusic.qq.com\/A000004FjJo32TISsY.ape?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
        # "flac":"http:\/\/dl.stream.qqmusic.qq.com\/F000004FjJo32TISsY.flac?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
        # "pic":"https:\/\/y.gtimg.cn\/music\/photo_new\/T002R300x300M000003NZyTh4eMMsp.jpg?max_age=2592000"
        # }
        # print('mid:'+dic['mid'])
        postfix, url = choice_download(dic)
        save_path = "D:\\Music\\"
        download_file(url, save_path + songname + ' - ' + singer + postfix)
        counter += 1

    print("total:", len(dlist), "success:", counter, "fail:", len(fail_list))

    if len(fail_list) != 0:
        print("fail_list:")
    for fail in fail_list:
        print(fail[0],fail[1])