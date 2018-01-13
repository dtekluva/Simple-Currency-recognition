from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce

i = Image.open('20.jpg')
iar = np.asarray(i)
iar.setflags(write=1)
#imageArray = iar
#print(iar)


def threshold(imageArray):
    balancearr = []
    newarr = imageArray

    for eachRow in imageArray:
        print("Please wait ....")

        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y,eachRow)/ len(eachRow)
            balancearr.append(avgNum)
    balance = (reduce(lambda x, y: x + y, balancearr)/len(balancearr))

    for eachRow in newarr:
        print("Please wait ....")
        for eachPix in eachRow:
            if (reduce(lambda x, y: x + y,eachRow)/ len(eachRow) > balance).any()  :
                #print((eachPix))
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
            
            else:
                #print(len(eachRow))
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
    return newarr

# plt.imshow(iar)
# print(iar)
# plt.show()

#fig = plt.figure()
#time.sleep(3)
#ax = plt.subplot2grid((8,6), (0,0), rowspan = 4, colspan = 3)
#ax.imshow(iar)
#plt.show()
#ax = plt.subplot2grid((8,6), (0,0), rowspan = 4, colspan = 3)
#ax2 = plt.subplot2grid((8,6), (0,4), rowspan = 4, colspan = 3)
#ax.imshow(iar)
#ax2.imshow(new_img)
#ax.imshow(new_img)
#print(new_img)
new_img = threshold(iar)
plt.imshow(new_img)
plt.show()