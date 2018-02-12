# Densenet_FinetuningForX-Ray

We hope to achieve an chest Xray detecting system

## Pretrained DenseNet Models on ImageNet

The top-1/5 accuracy rates by using single center crop (crop size: 224x224, image size: 256xN)

Network|Top-1|Top-5|Theano|Tensorflow
:---:|:---:|:---:|:---:|:---:
DenseNet 121 (k=32)| 74.91| 92.19| [model (32  MB)](https://drive.google.com/open?id=0Byy2AcGyEVxfMlRYb3YzV210VzQ)| [model (32 MB)](https://drive.google.com/open?id=0Byy2AcGyEVxfSTA4SHJVOHNuTXc)
DenseNet 169 (k=32)| 76.09| 93.14| [model (56  MB)](https://drive.google.com/open?id=0Byy2AcGyEVxfN0d3T1F1MXg0NlU)| [model (56 MB)](https://drive.google.com/open?id=0Byy2AcGyEVxfSEc5UC1ROUFJdmM)
DenseNet 161 (k=48)| 77.64| 93.79| [model (112 MB)](https://drive.google.com/open?id=0Byy2AcGyEVxfVnlCMlBGTDR3RGs)| [model (112 MB)](https://drive.google.com/open?id=0Byy2AcGyEVxfUDZwVjU2cFNidTA)

## Usage

First, download the above pretrained weights to the `imagenet_models` folder.

Run `test_inference.py` for an example of how to use the pretrained model to make inference.

```
python test_inference.py
```



for image viewer, write code:



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
        
Feel free to modify the code to your need  
