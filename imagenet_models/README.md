Please download pretrained weights


for loading image try code:

d1 = dict[b'data'][1]
        print(d1)
        NewImage = Image.new('RGB', (32, 32))
        print(d1[0])
        pixelList = []

        for i in range(0, 1024):
            pixel = (d1[i], d1[i + 1024], d1[i + 2048])
            pixelList.append(pixel)
        print(pixelList)
        NewImage.putdata(pixelList)
        NewImage.save('test5.jpg')