import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import base64
import re

class wangyiyun:   
    def __init__(self):
       self

    def create16RandomBytes(self):
        a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        generate_string = random.sample(a, 16)
        generated_string = ''.join(generate_string)
        return generated_string
    def AESEncrypt(self,clear_text, key):
        #AES加密, 对应函数b
        biv = '0102030405060708'  #偏移量
        clear_text = pad(data_to_pad=clear_text.encode(), block_size=AES.block_size)
        key = key.encode()
        iv = biv.encode()
        aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
        cipher_text = aes.encrypt(plaintext=clear_text)
        # 字节串转为字符串
        cipher_texts = base64.b64encode(cipher_text).decode()
        return cipher_texts
    def RSAEncrypt(self,i, e, n):
        #RSA加密, 对应函数c
        num = pow(int(i[::-1].encode().hex(), 16), int(e, 16), int(n, 16))
        result = format(num, 'x')
        return result
    def resultEncrypt(self,input_text):
        #对应函数d
        d = '010001'  #["流泪", "强"]
        dm ='00e0b509f6259df8642dbc35662901477df22677ec152b' \
            '5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417' \
            '629ec4ee341f56135fccf695280104e0312ecbda92557c93' \
            '870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b' \
            '424d813cfe4875d3e82047b97ddef52741d546b8e289dc69' \
            '35b3ece0462db0a22b8e7'
        dn ='0CoJUm6Qyw8W8jud'  #["爱心", "女孩", "惊恐", "大笑"]
        i = self.create16RandomBytes()
        encText = self.AESEncrypt(input_text, dn)
        encText = self.AESEncrypt(encText, i)
        encSecKey = self.RSAEncrypt(i, d, dm)
        from_data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return from_data
def data():    
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    prox = {
        'http':'61.216.156.222:60808'
    }
    id_d = {
        "hlpretag": "<span class=\"s-fc7\">",
        "hlposttag": "</span>",
        "s": input("请输入歌名与歌手: "),
        "type": "1",
        "offset": "0",
        "total": "true",
        "limit": "30",
        "csrf_token": ""
    }
    encrypt = wangyiyun()
    id_from_data = encrypt.resultEncrypt(str(id_d))
    data = requests.post("https://music.163.com/weapi/cloudsearch/get/web?csrf_token=",headers=header,proxies=prox,data=id_from_data)
    datatext=data.text
    idb=re.compile('"id":(\d{10})',re.S)
    id=re.findall(idb,datatext)
    music={"ids":str([id[0]]),"level":"higher","encodeType":"aac", "csrf_token": ""}
    encrypta= wangyiyun()
    music_from_data = encrypta.resultEncrypt(str(music))
    find=requests.post("https://music.163.com//weapi/song/enhance/player/url/v1?csrf_token=",headers=header,proxies=prox,data=music_from_data)
    findtext=find.text
    urld=re.compile('"url":"(.+?)",',re.S)
    url=re.findall(urld,findtext)
    print(url)
data()


# with open('mi.txt','w',encoding='utf-8') as f:
#         for DIP in findtext:
#             f.write(DIP+"/n")
