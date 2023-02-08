import base64
import hashlib
import json
import random
import string
import time
from hashlib import md5

import requests

import __version__

## 常量定义区域
CLIENT_VERSION = __version__.__version__
CLIENT_TYPE = 'python'
USER_AGENT = "fastposter-cloud-client/" + CLIENT_VERSION + " (" + CLIENT_TYPE + ")"


##

def md5(params):
    m = hashlib.md5()
    m.update(params.encode("utf8"))
    data_digest = m.digest()
    return data_digest.hex()


def get_time(f):
    def inner(*arg, **kwarg):
        s_time = time.time()
        res = f(*arg, **kwarg)
        e_time = time.time()
        print('耗时：{}秒'.format(e_time - s_time))
        return res

    return inner


class Poster:

    # Poster(traceId, type, r.content, b64)
    def __int__(self, traceId, type, content, b64):
        self.traceId = traceId
        self.type = type
        self.content = content
        self.size = len(content)
        self.b64 = b64

    def save(self, path):
        with open(path, 'wb') as f:
            f.write(self.content)
            print('保存海报')

    def save(self):
        path = self.traceId[0:16] + "." + type;
        if self.b64:
            path += ".b64"
        self.save(path)
        return path


class FastposterCloudClient:
    url = 'https://api.fastposter.net/v1/build/poster'

    def __init__(self, appKey='', appSecret=''):
        self.appKey = appKey
        self.appSecret = appSecret

    @get_time
    def buildPoster(self, uuid, params={}, type='png', scale=1.0, b64=False, userAgent=None, onlySign=False):

        # 准备参数
        payload = json.dumps(params, ensure_ascii=False)
        payload = base64.b64encode(payload.encode(encoding='utf-8')).decode(encoding='utf-8')
        timestamp = str(int(time.time()))
        nonce = ''.join(random.sample(string.ascii_letters, 16))
        pay = payload + timestamp + nonce + self.appSecret
        sign = md5(pay)

        body = {
            "uuid": uuid,
            "appKey": self.appKey,
            "timestamp": timestamp,
            "nonce": nonce,
            "payload": payload,
            "sign": sign,
            "type": type,
        }

        if b64:
            body['b64'] = True

        # 校验参数
        if scale != 1.0:
            body['scale'] = scale

        if onlySign:
            return body

        ## 设置请求头
        userAgent = userAgent if userAgent else USER_AGENT
        headers = {
            'Client-Type': CLIENT_TYPE,
            'Client-Version': CLIENT_VERSION,
            'User-Agent': userAgent,
            'cache-control': "no-cache"
        }

        r = requests.post(self.url, headers=headers, json=body)

        # 请求出现异常
        if r.headers['Content-Type'].startswith('application/json'):
            print(r.json())

        traceId = r.headers['fastposter-cloud-traceid']
        print(traceId)
        return Poster(traceId, type, r.content, b64)


def main():
    client = FastposterCloudClient('1f5aa8d75f2d4bc4', '8a395182a41e41ad9318cea4e1018cdc')
    params = {
        'name': '你好'
    }
    client.buildPoster("ced9b1d5337d494c", params=params).save();


if __name__ == '__main__':
    main()
