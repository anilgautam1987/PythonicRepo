
def ListwithinvsListPrinter(outerlist , *args , **kwargs):
    for innerlist in outerlist:
        for item in innerlist:
            print (item)

def RecursiveListPrinter(outerlist , *args , **kwargs):
    if outerlist and type(outerlist) == list:
        for innerlist in outerlist:
            if type(innerlist) == list:
                RecursiveListPrinter(innerlist)
            else:
                print(innerlist)

def BestRecursiveList(*args , **kwargs):    
    for outerlist in list(args) + list(kwargs.values()):
        if type(outerlist) == list:
            for innerlist in outerlist:
                if type(innerlist) == list:
                    BestRecursiveList(innerlist)
                else:
                    print innerlist
                    
if __name__=='__main__':
    L1 = [[1,2], [4,5]]
    #ListwithinvsListPrinter(L1)
    #RecursiveListPrinter(L1)
    BestRecursiveList(myList = L1)
    
