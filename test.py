"""**Test memory data against input data"""
import mem_io as write
from functools import reduce

def resolve(imageArray):
    import vectorize as vectorize

    newarr = imageArray
    newimg = []
    targ = []
    for pix in imageArray:
        newimg.append(vectorize.scale(pix))
    
    for pix in newimg:
        targ.append(vectorize.further_reduce(pix))

    return targ

def deviation(test_img):

    mem = write.io() 
    deviated_copy = mem
    newimg = resolve(test_img)

    for key in mem:
        
        i = 0
        mean_dev = []
        for val in newimg:
            dev = newimg[i][0] - mem[key][i][0]
            mean_dev.append(dev)
            i+=1

        deviated_copy[key] = mean_dev

    return deviated_copy

def test(newarr, mem):
    mem = ""
    newarr = deviation(newarr)
    result = newarr #copying newarr so thet result can maintain a similar dict structure as newarr for easy compilation
    
    for key in newarr:
        i = 0
        for item in range(len(newarr[key])):
            if newarr[key][i] < 0:
                newarr[key][i] = newarr[key][i] * -1
            i +=1

            
        tot_dev = reduce(lambda x, y: x + y,newarr[key])
        newarr[key] = (1-((2284800 - tot_dev)/2284800))

    decision = min(result.items(),key = lambda x:x[1])


    if "20" in decision[0]:
        print("20 Naira note, " + " decision confidence  "+ confidence(decision[1]) + "%")
    elif "100" in decision[0]:
        print("100 Naira note, " + " decision confidence  "+ confidence(decision[1]) + "%")
    elif "200" in decision[0]:
        print("200 Naira note, " + " decision confidence  "+ confidence(decision[1]) + "%")
    elif "500" in decision[0]:
        print("500 Naira note, " + " decision confidence  "+ confidence(decision[1]) + "%")
    elif "1000" in decision[0]:
        print("1000 Naira note, " + " decision confidence  "+ confidence(decision[1]) + "%")
    elif "50" in decision[0]:
        print("50 Naira note, " + " decision confidence  "+ confidence(decision[1]) + "%" )

def confidence(val):
    if val > 1:
        val = int(val)
    conf = (1 - val) * 100

    return str(conf)