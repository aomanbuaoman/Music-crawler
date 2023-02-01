import requests
import re

s=input('请输入歌手和歌名')
header = {
        'Cookie': 'kw_token=0JDQ8SC4NQCV; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1675232039; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1675234709; _ga=GA1.2.998170658.1675232040; _gid=GA1.2.1303447569.1675232040; _gat=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Csrf': '0JDQ8SC4NQCV',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://kuwo.cn/search/list?key={}'.format(s)
    }
prox = {
        'http':'61.216.156.222:60808'
    }
params={
        'key':s,  
        'pn':'1',
        'rn':'30',
        'httpsStatus':'1',
        'reqId':'e16601f0-a1fd-11ed-bd4a-9f5d4cdbab1d'
}
data=requests.get('https://kuwo.cn/api/www/search/searchMusicBykeyWord',headers=header,proxies=prox,params=params)
kuwosz=re.compile('"rid":(.*?),',re.S)
kuwos=re.findall(kuwosz,data.text)
param={
    'mid':kuwos[0], 
    'type':'music',
    'httpsStatus':'1', 
    'reqId':'1636af31-a1f7-11ed-89d2-c9d76452665b' 
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
kuwudata=requests.get('https://kuwo.cn/api/v1/www/music/playUrl',headers=headers,proxies=prox,params=param)
print(kuwudata.text)
kuwomz=re.compile('"url":"(.*?)"',re.S)
kuwom=re.findall(kuwomz,kuwudata.text)
print(kuwom)