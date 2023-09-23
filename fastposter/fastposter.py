# -*- coding: UTF-8 -*-

import base64
import hashlib
import json
import os.path

import requests

from fastposter import __version__

CLIENT_VERSION = __version__.__version__
CLIENT_TYPE = 'python'
ENDPOINT = 'https://api.fastposter.net'


def md5(params):
    m = hashlib.md5()
    m.update(params.encode("utf8"))
    data_digest = m.digest()
    return data_digest.hex().lower()


def get_suffix(uri):
    return os.path.splitext(uri)[-1]


class Poster:

    def __init__(self, uuid, type, content, b64):
        self.uuid = uuid
        self.type = type
        self.bytes = content
        self.size = len(content)
        self.b64 = b64

    def saveTo(self, path):
        with open(path, 'wb') as f:
            f.write(self.bytes)

    def save(self, filename=None, dirname=None):
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
            path += self.uuid + "." + self.type
        if self.b64:
            path += ".b64"
        self.saveTo(path)
        return path

    def b64String(self):
        if not self.b64:
            text = """please set b64 is Ture. for example.
client.buildPoster("ced9b1*****d494c", params=params, b64=True).b64String()
            """
            print(text)
            return
        return self.bytes.decode('utf-8')


class Client:

    @staticmethod
    def version():
        return CLIENT_VERSION

    def __init__(self, token='', endpoint=ENDPOINT):
        self.endpoint = endpoint
        self.token = token

    def buildPoster(self, uuid, params={}, type='png', scale=1.0, b64=False, userAgent=None):
        _payload = json.dumps(params, ensure_ascii=False)
        payload = base64.b64encode(_payload.encode(encoding='utf-8')).decode(encoding='utf-8')
        body = {
            "uuid": uuid,
            "payload": payload,
            "type": type,
        }
        if b64:
            body['b64'] = True
        if scale != 1.0:
            body['scale'] = scale
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
        return Poster(uuid, type, r.content, b64)
