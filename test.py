from fastposter import Client


client = Client('07657854eb3858269c76')
client.buildPoster('2ef32fb23c6d458b', params={'nickname': '这奇怪的世界'}).save('aaa.jpg')

if __name__ == '__main__':
    # pip config get global.index-url
    pass
