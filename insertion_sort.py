import sys
sys.setrecursionlimit(100000)
def selection_sort(sequence):
    
    for start in range(len(sequence)):        
        for i in range(start, len(sequence)):
            minimum_pos = start 
            if sequence[i] < sequence[minimum_pos]:
                minimum_pos = i 
                # start will be replaced by minimum_position
                (sequence[start], sequence[minimum_pos]) = (sequence[minimum_pos] , sequence[start])
    return sequence

#print 'Selection Sort =:' , selection_sort([2,8,4,78,7])

def insertion_sort(sequence): 
    
    for current_pos in range(len(sequence)):
        pos = current_pos
        print 'Position =: {0}'.format(pos)
        while pos > 0 and (sequence[pos] < sequence[pos-1]):
            print sequence[pos] ,  sequence[pos-1]           
            (sequence[pos] , sequence[pos -1]) = (sequence[pos -1] , sequence[pos]) 
            pos = pos -1
    return sequence

print insertion_sort([2,8,4,78,7])
#print 'Insertion Sort =:' , insertion_sort(range(500, 0 , -1))

def bubbleSort(myList):
    ''' need to learn '''
    # number of elements in list 
    for i in range(0 , len(myList)-1):
        for j in range(0 , len(myList)-1-i):
            if myList[j] > myList[j+1]:
                myList[j] , myList[j+1] = myList[j+1] , myList[j]
    return myList
print 'Bubble Sort=:' , bubbleSort([34,6,7,81,1,0])


def mergeSort(aList):
    ''' need to learn
        Two step process :
        1 -: split the list into Two Halves
        2 -: Merge: Each item in a List will be prcoessed and placed on the sorted list
    '''
    mid = len(aList) // 2
    lefthalf = aList[mid:]
    righthalf = aList[:mid]

    mergeSort(lefthalf)
    mergeSort(righthalf)

    i = 0 # i - left
    j = 0 # j - right
    k = 0 # k - main list
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            aList[k] = lefthalf[i]
            i = i + 1
        else:
            aList[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        aList[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        aList[k] = righthalf[j]
        j = j + 1
        k = k + 1
    print("Merging Sort" , aList)

myList = [23,45,6,765,45,32]
mergeSort(myList)
print(myList)



def quickSort():
    ''' need to learn ''' 

def length(L):    
    if L == []:
        return 0
    else:
        return ( 1 + length( L[1:] ) )

print 'Length =:' , length([1,3,5,5])

def sumList(L):    
    if L == []:
        return 0 
    else:
        return (L[0] + sumList(L[1:]))
print 'Sum =:' , length([1,3,5,5])


