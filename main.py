from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import test as label
from functools import reduce
import mem_io as write



def preprocess(imageArray):
    balancearr = []
    newarr = imageArray

    for eachRow in imageArray:
      
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y,eachPix[:3])/ len(eachPix[:3])
            balancearr.append(avgNum)

    balance = (reduce(lambda x, y: x + y, balancearr)/len(balancearr))+30

    for eachRow in newarr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y,eachPix[:3]/ len(eachPix[:3])) > balance :
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
            
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
            
    for arr in newarr:
        for pix in arr:
            #print
            (reduce(lambda x, y: x + y,pix[:3]))
            #print(pix)
    return newarr

def train(label_name, file_name):

    i = Image.open('training/'+ file_name)
    iar = np.asarray(i)
    iar.setflags(write=1)

    new_img = preprocess(iar)
    write.sync(new_img, label_name)
    #plt.imshow(new_img)
    #plt.show()

def test_img(file_name):

    i = Image.open('training/'+ file_name)
    iar = np.asarray(i)
    iar.setflags(write=1)

    new_img = preprocess(iar)
    label.test(new_img, [])

#train("20", "20.jpg")#train as follows train("label of data", "name of target file with extension")
test_img("200.jpg")#test as follows test_img("name of target file with extension")