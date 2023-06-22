# -*- coding: UTF-8 -*-

import base64
import hashlib
import json
import os.path
import random
import string
import time
from hashlib import md5

import requests

from fastposter import __version__

## 常量定义区域
# 客户端版本
CLIENT_VERSION = __version__.__version__

# 客户端类型
CLIENT_TYPE = 'python'

# 默认的用户代理
# USER_AGENT = "fastposter-cloud-client/" + CLIENT_VERSION + " (" + CLIENT_TYPE + ")"

# 接入点地址
ENDPOINT = 'https://api.fastposter.net'


def md5(params):
    """
    md5小写
    :param params:
    :return:
    """
    m = hashlib.md5()
    m.update(params.encode("utf8"))
    data_digest = m.digest()
    return data_digest.hex().lower()


def get_suffix(uri):
    return os.path.splitext(uri)[-1]


class Poster:
    """
    海报对象
    """

    def __init__(self, traceId, type, content, b64):
        """
        初始化海报对象
        :param traceId:
        :param type:
        :param content:
        :param b64:
        """
        self.traceId = traceId
        self.type = type
        self.bytes = content
        self.size = len(content)
        self.b64 = b64

    def saveTo(self, path):
        """
        保存到指定路径
        :param path: 完整的存放路径
        :return: None
        """
        with open(path, 'wb') as f:
            f.write(self.bytes)

    def save(self, filename=None, dirname=None):
        """
        保存海报
        :param filename: 文件名称，默认为随机文件名
        :param dirname: 指定存放目录，默认为当前目录。目录不存在会自动创建
        :return: 文件路径
        """
        path = ''
        if dirname:
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            path = dirname + "/"
        if filename:
            if not get_suffix(filename):
                filename += "." + self.type
            path += filename
        else:
            path += self.traceId[0:16] + "." + self.type
        if self.b64:
            path += ".b64"
        self.saveTo(path)
        return path

    def b64String(self):
        """
        以base64格式输出
        """
        if not self.b64:
            text = """please set b64 is Ture. for example.
client.buildPoster("ced9b1*****d494c", params=params, b64=True).b64String()
            """
            print(text)
            return
        return self.bytes.decode('utf-8')


@DeprecationWarning
class CloudClient:
    """
    海报云服务客户端
    """

    seq = 1

    @staticmethod
    def version():
        return CLIENT_VERSION

    def __init__(self, appKey='', appSecret='', endpoint=ENDPOINT, debug=False, trace=False):
        """
        初始化一个海报云服务客户端
        :param appKey: 应用KEY
        :param appSecret: 应用密钥
        :param endpoint: 接入端地址
        :param debug: 是否开启调试模式
        :param trace: 是否开启着重模式
        """
        debug = True if trace else debug
        self.appKey = appKey
        self.appSecret = appSecret
        self.endpoint = endpoint
        self.debug = debug
        self.trace = trace

    def buildPoster(self, uuid, params={}, type='png', scale=1.0, b64=False, userAgent=None, onlySign=False):
        """
        生成海报
        :param uuid: 海报UUID
        :param params: 海报参数
        :param type: 海报类型
        :param scale: 海报缩放比 0.1 ~ 1.0
        :param b64: 是否返回base64字符串
        :param userAgent: 客户代理
        :param onlySign: 只签名
        :return: 海报|签名对象
        """

        _payload = json.dumps(params, ensure_ascii=False)
        payload = base64.b64encode(_payload.encode(encoding='utf-8')).decode(encoding='utf-8')
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

        if self.trace:
            print(str(self.seq) + " build poster payload=" + _payload)

        userAgent = '' if not userAgent else userAgent

        headers = {
            'Client-Type': CLIENT_TYPE,
            'Client-Version': CLIENT_VERSION,
            'User-Agent': userAgent,
            'cache-control': "no-cache",
        }

        url = self.endpoint + "/v1/build/poster"
        r = requests.post(url, headers=headers, json=body)

        # 请求出现异常
        if r.headers['Content-Type'].startswith('application/json'):
            print(r.json())

        traceId = r.headers.get('fastposter-traceid', timestamp)
        if not traceId:
            traceId = timestamp

        # 计数器累加
        self.seq += 1
        return Poster(traceId, type, r.content, b64)


class Client:
    """
    海报客户端
    """

    seq = 1

    @staticmethod
    def version():
        return CLIENT_VERSION

    def __init__(self, token='', endpoint=ENDPOINT, debug=False, trace=False):
        """
        初始化一个海报客户端
        :param token: token
        :param endpoint: 接入端地址
        :param debug: 是否开启调试模式
        :param trace: 是否开启着重模式
        """
        debug = True if trace else debug
        self.endpoint = endpoint
        self.debug = debug
        self.trace = trace
        self.token = token

    def buildPoster(self, uuid, params={}, type='png', scale=1.0, b64=False, userAgent=None, onlySign=False):
        """
        生成海报
        :param uuid: 海报UUID
        :param params: 海报参数
        :param type: 海报类型
        :param scale: 海报缩放比 0.1 ~ 1.0
        :param b64: 是否返回base64字符串
        :param userAgent: 客户代理
        :param onlySign: 只签名
        :return: 海报|签名对象
        """

        _payload = json.dumps(params, ensure_ascii=False)
        payload = base64.b64encode(_payload.encode(encoding='utf-8')).decode(encoding='utf-8')
        # timestamp = str(int(time.time()))
        # nonce = ''.join(random.sample(string.ascii_letters, 16))
        # pay = payload + timestamp + nonce + self.appSecret
        # sign = md5(pay)

        body = {
            "uuid": uuid,
            # "appKey": self.appKey,
            # "timestamp": timestamp,
            # "nonce": nonce,
            "payload": payload,
            # "sign": sign,
            "type": type,
        }

        if b64:
            body['b64'] = True

        # 校验参数
        if scale != 1.0:
            body['scale'] = scale

        if onlySign:
            return body

        if self.trace:
            print(str(self.seq) + " build poster payload=" + _payload)

        userAgent = '' if not userAgent else userAgent

        headers = {
            'Client-Type': CLIENT_TYPE,
            'Client-Version': CLIENT_VERSION,
            'token': self.token,
            'User-Agent': userAgent,
            'cache-control': "no-cache",
        }

        url = self.endpoint + "/v1/build/poster"
        r = requests.post(url, headers=headers, json=body)

        # 请求出现异常
        if r.headers['Content-Type'].startswith('application/json'):
            print(r.json())

        traceId = r.headers['fastposter-traceid']

        # 计数器累加
        self.seq += 1
        return Poster(traceId, type, r.content, b64)
