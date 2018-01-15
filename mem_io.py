""" **MEM_IO** \n Reads and Writes training data  """
import pickle
import vectorize as vectorize
from os import walk

def io(itemlist = [], action = 'r', label = "unlabeled"):

    """check if name exists using exists() and then if exists increment the 
        name by 1 to differentiate the created traiining files """

    mem_path = 'memory/'
    ext = ""
    if action == "w" or action == "w":
        if exists(label):
            ext = 1
            while exists(label, ext) :
                ext += 1    
   
        with open('memory/'+label + str(ext), 'wb') as fp:
                pickle.dump(itemlist, fp)

    if action == "r" or action == "r":
        """read memory folder for all traiining files the read training data from 
            files and log into a dictionary and return the dictionary """

        file_list = []
        memory = {}
        for (filenames) in walk('memory'):
            file_list.extend(filenames)
            break
        
        for filename in file_list[2]:
            with open ('memory/'+ filename, 'rb') as fp:
                itemlistn = pickle.load(fp)
                memory[filename] = itemlistn
        return memory

def sync(imageArray, label):
    """**SYNC**  Writes Training data as vectors"""
    newarr = imageArray
    newimg = []
    targ = []
    for pix in imageArray:
        newimg.append(vectorize.scale(pix))
    
    for pix in newimg:
        targ.append(vectorize.further_reduce(pix))

    io(targ,"w",label)

    #temp = io()

def exists(label, ext = ""):
    """check if name exists and return a true or false response"""
    try:
        with open ('memory/' + label+str(ext), 'rb') as fp:
            return True
    except:
        return False
