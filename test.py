from fastposter import CloudClient, Client

#
# # client = CloudClient('1f5aa8d75f2d4bc4', '8a395182a41e41ad9318cea4e1018cdc', trace=True)
# client = CloudClient('1f5aa8d75f2d4bc4', '8a395182a41e41ad9318cea4e1018cdc', trace=True)
# params = {
#     'name': '你好，中国',
#     'age': '108'
# }
#
#
# client = CloudClient('c08dc617e3654820', '122a584d934c454b889dbb0300c60543')
#
# # 保存图片
# # path = client.buildPoster("ced9b1d5337d494c", params=params).save()
# # print(path)
#
# # 保存图片到指定路径
# client.buildPoster("ced9b1d5337d494c", params=params).saveTo('xxx.png')
#
# # 获取Base64图片格式
# # r = client.buildPoster("ced9b1d5337d494c", params=params, b64=True).b64String()
# # print(r)


# client = CloudClient('c08dc617e3654820', '122a584d934c454b889dbb0300c60543')
# client.buildPoster('8c4ab34a843e480b', params={'qrcode': '1231233213'}).save('aaa.jpg')

client = Client('07657854eb3858269c76')
client.buildPoster('2ef32fb23c6d458b', params={'nickname': '这奇怪的世界'}).save('aaa.jpg')

if __name__ == '__main__':
    # pip config get global.index-url
    pass
