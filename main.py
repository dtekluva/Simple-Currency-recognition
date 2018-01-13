from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce
import mem_io as write

i = Image.open('training/503.jpg')
iar = np.asarray(i)
iar.setflags(write=1)

# print(iar)


def threshold(imageArray):
    balancearr = []
    newarr = imageArray

    for eachRow in imageArray:
      
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y,eachPix[:3])/ len(eachPix[:3])
            balancearr.append(avgNum)

    balance = (reduce(lambda x, y: x + y, balancearr)/len(balancearr))+70

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
            
    # for arr in newarr:
    #     reduce(lambda x, y: x + y,eachPix[:3]/ len(eachPix[:3]))
    #     print(arr)
    return newarr


new_img = threshold(iar)
write.sync(new_img)

plt.imshow(new_img)
plt.show()