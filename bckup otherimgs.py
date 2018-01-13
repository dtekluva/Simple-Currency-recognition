from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce


i = Image.open('5.png')
iar = np.asarray(i)
iar.setflags(write=1)

# print(iar)

f= open("guru99.txt","a")

for i in range(20):
     f.write("This is line %d\r\n" % (i+1))
f.close() 

def threshold(imageArray):
    balancearr = []
    newarr = imageArray
    test = []
    
    test.append(newarr[0])
    print(test)



    #balance = (reduce(lambda x, y: x + y, balancearr)/len(balancearr))+70

    # for eachRow in newarr:
    #     #print(newarr)
    #     for eachPix in eachRow:
    #         if reduce(lambda x, y: x + y,eachPix[:3]/ len(eachPix[:3])) > balance :
    #             eachPix[0] = 255
    #             eachPix[1] = 255
    #             eachPix[2] = 255
            
    #         else:
    #             eachPix[0] = 0
    #             eachPix[1] = 0
    #             eachPix[2] = 0
    return newarr

# plt.imshow(iar)
#print(iar)
# plt.show()

fig = plt.figure()
#time.sleep(3)
#ax = plt.subplot2grid((8,6), (0,0), rowspan = 4, colspan = 3)
#ax.imshow(iar)
#plt.show()
new_img = threshold(iar)

ax = plt.subplot2grid((8,6), (0,0), rowspan = 4, colspan = 3)
ax.imshow(iar)
# ax2 = plt.subplot2grid((8,6), (0,4), rowspan = 4, colspan = 3)
# ax2.imshow(new_img)

# plt.imshow(new_img)
plt.show()