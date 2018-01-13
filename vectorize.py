from functools import reduce

def scale(arr):

    pix_avg = reduce(lambda x, y: x + y,arr[:3])
    #print(len(pix_avg))