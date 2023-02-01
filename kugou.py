import requests
import hashlib
import time
import re

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
prox = {
        "http":"61.216.156.222:60808"
    }
n=input("请输入歌手和歌名")
s = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt", 
    "appid=1014", 
    "bitrate=0", 
    "callback=callback123", 
    "clienttime={}".format(int(time.time() * 1000)), 
    "clientver=1000", 
    "dfid=08xrxO05ksAE43juSd28o92H", 
    "filter=10", 
    "inputtype=0", 
    "iscorrection=1", 
    "isfuzzy=0", 
    "keyword={}".format(n), 
    "mid=f952480a8705aa8efb36735fe792bece", 
    "page=1", 
    "pagesize=30", 
    "platform=WebFilter", 
    "privilege_filter=0", 
    "srcappid=2919", 
    "token=", 
    "userid=0", 
    "uuid=f952480a8705aa8efb36735fe792bece", 
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]
o="".join(s) 
md5 = hashlib.md5(o.encode(encoding="utf-8")).hexdigest() #md5加密
param={
    "callback":"callback123",
    "srcappid":"2919",
    "clientver":"1000",
    "clienttime":int(time.time() * 1000),
    "mid":"f952480a8705aa8efb36735fe792bece",
    "uuid":"f952480a8705aa8efb36735fe792bece",
    "dfid":"08xrxO05ksAE43juSd28o92H",
    "keyword": f"{n}",
    "page":"1",
    "pagesize":"30",
    "bitrate":"0",
    "isfuzzy":"0",
    "inputtype":"0",
    "platform":"WebFilter",
    "userid":"0",
    "iscorrection":"1",
    "privilege_filter":"0",
    "filter":"10",
    "token":"",
    "appid":"1014",
    "signature": md5
}
data=requests.get('https://complexsearch.kugou.com/v2/search/song',headers=header,proxies=prox,params=param)
kugous=re.compile('"EMixSongID":"(.+?)".',re.S)
kugouid=re.findall(kugous,data.text)

params={
    'r':'play/getdata',
    'callback':'jQuery19105511680469461328_1675129023355',
    'dfid':'08xrxO05ksAE43juSd28o92H',
    'appid':'1014',
    'mid':'f952480a8705aa8efb36735fe792bece',
    'platid':'4',
    "encode_album_audio_id":kugouid[0],
    '_':'1675129023356'
}
kugoudata=requests.get('https://wwwapiretry.kugou.com/yy/index.php?',headers=header,proxies=prox,params=params)
kugoud=re.compile('"play_url":"(.+?)"',re.S) #还有一个备份地址，正则为 "play_backup_url":"(.+?)"
kugoudm=re.findall(kugoud,kugoudata.text)
kugoum = eval(repr(str(kugoudm)).replace('\\', ''))
print(kugoum)
