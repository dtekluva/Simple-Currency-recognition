""" **MEM_IO** \n Reads and Writes training data  """
import pickle
import vectorize as vectorize

def io(itemlist, action):
    if action == "w" or action == "w":
        with open('memory/outfile', 'wb') as fp:
            pickle.dump(itemlist, fp)

    if action == "r" or action == "r":
        with open ('memory/outfile', 'rb') as fp:
            itemlistn = pickle.load(fp)
            return itemlistn

def sync(imageArray):
    """**SYNC**  Writes Training data"""
    newarr = imageArray
    test = []
    for pix in imageArray:
        test.append(pix)
        vectorize.scale(pix)

    io(test,"w")

    temp = io(0, "r")
    if temp in newarr:
        print("known note")
    elif temp not in newarr:
        print("Unknown note")