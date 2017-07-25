import sys
sys.setrecursionlimit(10000)

def insertionSort(seq):
    return isort(seq , len(seq))
    
def isort(seq , k):
    if k > 1:
        isort(seq, k-1)
        insert(seq , k-1) 
    return seq

def insert(seq , k):
    pos = k 
    while pos > 0 and seq[pos] < seq[pos - 1]:
        (seq[pos] , seq[pos -1]) = (seq[pos -1] , seq[pos])
        pos = pos -1 
    return seq

print insertionSort([2, 4, 7, 8, 78])
''' 
Note : sorting - more then 1000 element python will through error , hence we need to manually set the recussion limit ,
with upper bound sys.setrecursionlimit(10000) 
'''
print insertionSort(range(1000, 0 , -1))


