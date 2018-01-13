from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce

i = Image.open('20.jpg')
iar = np.asarray(i)
iar.setflags(write=1)

for row in iar:
    for i in row:
        
        print(len(i))
    break