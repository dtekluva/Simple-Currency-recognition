from functools import reduce


def scale(arr):
    list =[]

    for pix in arr:
        pix_avg = reduce(lambda x, y: x + y,pix[:3])
        list.append(int(pix_avg))
        
    return list

def further_reduce(arr):
    list =[]

    pix_avg = reduce(lambda x, y: x + y,arr)
    list.append(int(pix_avg))

    return list

def vec_direction(list):
    new_list = []
    #print(list[1])
    i = 0
    for item in range(len(list)-1):
        new_list.append(list[i]-list[i + 1])
        i +=1
    
    return new_list