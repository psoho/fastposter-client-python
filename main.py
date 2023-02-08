from fastposter import CloudClient

client = CloudClient('1f5aa8d75f2d4bc4', '8a395182a41e41ad9318cea4e1018cdc', trace=True)
params = {
    'name': '你好',
    'age': '18'
}
r = client.buildPoster("ced9b1d5337d494c", params=params).b64String()
print(r)
# client.buildPoster("ced9b1d5337d494c", params=params)
# client.buildPoster("ced9b1d5337d494c", params=params)
# client.buildPoster("ced9b1d5337d494c", params=params)

if __name__ == '__main__':
    pass
