import numpy as np
from pprint import pprint 
import sys  
file = 'FL_insurance_sample.csv'
#ary2d = np.genfromtxt(file, delimiter=',', skip_header=1, skip_footer=0, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8','col9', 'col10', 'col11', 'col12', 'col13', 'col14', 'col15', 'col16', 'col17', 'col18',])


#print(type(ary2d))
#cnt = 0 
#for x in np.nditer(ary2d , order='F'):
#    print x
#    if cnt == 5:
#        sys.exit()
#   cnt = cnt + 1
    
import mmap
import time
def mmapUsage():
    start=time.time()
    with open(file, "r+b") as f:
        # memory-mapInput the file, size 0 means whole file
        mapInput = mmap.mmap(f.fileno(), 0)
        # read content via standard file methods
        L=list()
        for s in iter(mapInput.readline, ""):
            L.append(s)
        print "List length: " ,len(L)
        #print "Sample element: ",L[1]
        mapInput.close()
        end=time.time()
        print "Time for completion",end-start
    return L
L = mmapUsage()
print L[0]

