def Sequential_Search(myList , item):
    pos = 0 
    found = False
    while (pos < len(myList) and not found):
        if myList[pos] == item:
            found = True            
        else:
            pos = pos + 1 
    return (pos , found)
print Sequential_Search([11,23,58,31,56,77,43,12,65,19],31)

def binary_search(myList, item):
    first = 0
    last = len(myList) - 1
    found = False
    
    while first <= last and not found:
        mid = (first+last) // 2
        if myList[mid] == item:
            found = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1 
    return found

print(binary_search([1,2,3,5,8], 5))
print(binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))

def bubbleSort(nList):    
    for passnum in range(len(nList)-1, 0 , -1):
        for i in range(passnum):
            if nList[i] > nList[i+1]:
                temp = nList[i]
                nList[i] = nList[i+1]
                nList[i+1] = temp            
    return nList 
nlist = [14,46,43,27,57,41,45,21,70]
print bubbleSort(nlist)
    
# selection sort works on swaping of adjustent elements
def selectionSort(nlist):
    for fillslot in range(len(nlist)-1, 0 , -1):
        maxpos = 0 
        for location in range(1,fillslot+1):
            if nlist[location] > nlist[maxpos]:
                maxpos = location 
            nlist[fillslot] , nlist[maxpos] = nlist[maxpos] , nlist[fillslot]
    return nlist
        
nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)


def insertionSort(nlist):
    #shift to right if element is greater
    for index in range(1, len(nlist)):
        currentvalue = nlist[index]
        position = index
        #shift to right if element is greater
        while position > 0 and nlist[position-1] > currentvalue:
            nlist[position] = nlist[position-1]
            position = position - 1
            nlist[position] = currentvalue
            #insert in the right place - starts from zero      
            
    return nlist
nlist = [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)





