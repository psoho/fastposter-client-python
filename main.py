from fastposter import CloudClient

client = CloudClient('1f5aa8d75f2d4bc4', '8a395182a41e41ad9318cea4e1018cdc', trace=True)
params = {
    'name': '你好',
    'age': '18'
}

# 保存图片
path = client.buildPoster("ced9b1d5337d494c", params=params).save()
print(path)

# 保存图片到指定路径
client.buildPoster("ced9b1d5337d494c", params=params).saveTo('xxx.png')

# 获取Base64图片格式
r = client.buildPoster("ced9b1d5337d494c", params=params, b64=True).b64String()
print(r)

if __name__ == '__main__':
    pass
